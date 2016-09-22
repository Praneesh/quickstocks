#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.2.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"
#
#   Responsible for starting the required number of processes and threads

import threading
import time
from qs_backend.workers.worker_fetch_stock import StockWorker
from qs_backend.publisher.publish_stock import PublishStock
from qs_backend.dal.user_stock_pref_dal import UserStockPrefDAL


class Backend:
    def __init__(self):
        pass

    def start_stock_tickers(self):
        # Fetch all the stocks that users have chosen.
        while True:
            user_stock_pref_dal_obj = UserStockPrefDAL()
            stock_exception, available_stocks = user_stock_pref_dal_obj.get_all_stock_preferences()
            for stock in available_stocks:
                stock_key = stock
                # Start FetchStock Threads
                stock_worker_obj = StockWorker()
                ft_stock_thread = threading.Thread(target=stock_worker_obj.fetch_stock_price, args=(stock_key,))
                ft_stock_thread.daemon = True
                ft_stock_thread.start()
            time.sleep(60)

if __name__ == '__main__':
    backend_process = Backend()
    # Start all the Stock Worker Threads
    stock_ticker_thread = threading.Thread(target=backend_process.start_stock_tickers)
    stock_ticker_thread.start()

    time.sleep(5)
    # Wait for sometime, before you start the publisher.
    # The below makes a blocking call !
    pub_stock = PublishStock()
    pub_stock.start_publishing()






