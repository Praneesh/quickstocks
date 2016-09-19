#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"
#
#   Responsible for starting the required number of processes and threads

import threading
import time
from qs_backend.workers.worker_fetch_stock import StockWorker
from qs_backend.publisher.publish_stock import PublishStock

# Start FetchStock Threads
fetch_test = StockWorker()
stock_key = 'INTU'
ft_stock_thread = threading.Thread(target=fetch_test.fetch_stock_price, args=(stock_key,))
#ft_stock_thread.daemon = True
ft_stock_thread.start()

time.sleep(5)


# Start PublishStock Threads
pub_stock = PublishStock()
pub_stock_thread = threading.Thread(target=pub_stock.start_publishing())
#pub_stock_thread.daemon = True
pub_stock_thread.start()