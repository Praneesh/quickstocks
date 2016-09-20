#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.2"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"
#
#   Step 1: Spawned as a thread, fetches the stock price and pushes into a local message queue
#
#   Step 2: Publisher would read this queue, identify the corresponding publish queue, creates
#   a Dispatch packet and pushes onto Crossbar Queue, subscribed by Dispatcher

from queue import Queue
from qs_backend.models.stock_model import StockModel
from qs_backend.queues.stock_delivery_queue import StockDeliveryQueue
from qs_backend.logger.default_logger import QSDefaultLogger
from qs_backend.decorators.stock_publish_payload_to_dict import StockPublishPayloadToDict

from yahoo_finance import Share


class StockWorker:
    def __init__(self):
        # Get the logger instance !!
        qs_logger_instance = QSDefaultLogger()
        self.qs_logger = qs_logger_instance.get_logger(name=__name__)

        # Get the decorator instance !
        self.payload_to_publish_dict = StockPublishPayloadToDict()

    def fetch_stock_price(self, stock_unit_key):
        # Step 1: Make HTTP Call to fetch the Stock Details
        # Step 2: Once received, create it into its corresponding model
        # Step 2.1 : Between the models, exchange packet as a native dictionary, rather as a JSON object

        # Get the share price
        share_item = Share(stock_unit_key)

        if share_item.get_open() is None:
            return

        share_item_dict = share_item.data_set

        st_model = StockModel()
        st_model.stock_unit = stock_unit_key
        st_model.stock_title = share_item_dict['Name']

        # Share Price + Unit of Currency
        st_model.stock_price = share_item.get_price() + " " +share_item_dict['Currency']

        deviation_price = share_item.get_change()
        st_model.stock_deviation = deviation_price + " ("+share_item_dict['ChangeinPercent'] + ") "  # Ex: '-1.83 (-1.59%)'
        if deviation_price[0] == '-':
            st_model.stock_deviation_status = 'Decline'
        else:
            st_model.stock_deviation_status = 'Incline'

        st_model.stock_equity = share_item.get_stock_exchange()
        st_model.stock_last_update_time = 'At close: ' + share_item_dict['LastTradeDateTimeUTC']

        st_model.stock_52wkrange = share_item.get_year_low() + " - " + share_item.get_year_high()
        st_model.stock_open = share_item.get_open()
        st_model.stock_market_cap = share_item.get_market_cap()
        st_model.stock_prev_close = share_item.get_prev_close()
        st_model.stock_peratio_tte = share_item.get_price_earnings_ratio()

        st_model_to_publish = self.payload_to_publish_dict.get_stock_payload_to_publish(st_model)
        self.push_stock_to_delivery_queue(st_model_to_publish, stock_unit_key)

    def push_stock_to_delivery_queue(self, stock_model, stock_key):
        # Step 3 : Push this packet into a common queue
        stock_d_queue_instance = StockDeliveryQueue()
        stock_d_queue = stock_d_queue_instance.get_queue()
        self.qs_logger.info(msg='Got instance of Stock Delivery Queue')
        try:
            stock_d_queue.put_nowait(stock_model)
            self.qs_logger.debug(msg='Added Stock Item into Stock Delivery Queue : {}'.format(stock_model))
        except Queue.full as queue_full_exception:
            self.qs_logger.exception(msg='Queue Full Exception {}'.format(queue_full_exception))
            print("Queue Full Exception {}".format(queue_full_exception))
        except Exception as general_exception:
            self.qs_logger.exception(msg="General Exception {}".format(general_exception))

if __name__ == '__main__':
    fetch_test = StockWorker()
    fetch_test.fetch_stock_price('HON')
