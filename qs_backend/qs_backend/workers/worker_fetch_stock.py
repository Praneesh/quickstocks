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


class StockWorker:
    def __init__(self):
        # Get the logger instance !!
        qs_logger_instance = QSDefaultLogger()
        self.qs_logger = qs_logger_instance.get_logger(name=__name__)

    def fetch_stock_price(self, stock_unit_key):
        # Step 1: Make HTTP Call to fetch the Stock Details
        # Step 2: Once received, create it into its corresponding model
        # Step 2.1 : Between the models, exchange packet as a native dictionary, rather as a JSON object

        st_model = StockModel()
        st_model.stock_unit = stock_unit_key
        st_model.stock_price = '112.0 USD'
        st_model.stock_deviation = '-1.83 (-1.59%)'
        st_model.stock_deviation_status = 'Decline'
        st_model.stock_equity = 'NYSE - NYSE Real Time Price.'
        st_model.stock_last_update_time = 'At close: 4:01 PM EDT'

        self.push_stock_to_delivery_queue(st_model)

    def push_stock_to_delivery_queue(self, stock_model):
        # Step 3 : Push this packet into a common queue
        stock_d_queue_instance = StockDeliveryQueue()
        stock_d_queue = stock_d_queue_instance.get_queue()
        self.qs_logger.info(msg='Got instance of Stock Delivery Queue')
        try:
            stock_d_queue.put_nowait(stock_model.__dict__)
            self.qs_logger.debug(msg='Added Stock Item into Stock Delivery Queue : {}'.format(stock_model.stock_unit))
        except Queue.full as queue_full_exception:
            self.qs_logger.exception(msg='Queue Full Exception {}'.format(queue_full_exception))
            print("Queue Full Exception {}".format(queue_full_exception))
        except Exception as general_exception:
            self.qs_logger.exception(msg="General Exception {}".format(general_exception))

if __name__ == '__main__':
    fetch_test = FetchStockWorker()
    fetch_test.fetch_stock_price('H')
