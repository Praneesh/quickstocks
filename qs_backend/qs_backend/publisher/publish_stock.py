#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"
#
#   Step 1: Reads the Stock Delivery Queue for messages
#   Step 2: Creates a dispatch packet and sends it on to Dispatcher Queue

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from asyncio import coroutine, sleep

from qs_backend.queues.stock_delivery_queue import StockDeliveryQueue


class PublishStock:
    class PublishStockRunner(ApplicationSession):
        @coroutine
        def onJoin(self, details):
            print("WAMP + Crossbar - Publisher Session Available")
            # Step 1: Get the instance of queue
            stock_d_queue_instance = StockDeliveryQueue()
            stock_d_queue = stock_d_queue_instance.get_queue()
            # TO DO: Logging, Exception Handling Here !
            while True:
                con_topic_to_publish = u'com.quickstocks.publisher.b6b7a9887'
                stock_data_from_queue = stock_d_queue.get()
                if stock_data_from_queue is None:
                    continue
                self.publish(con_topic_to_publish, stock_data_from_queue)
                stock_d_queue.task_done()
                yield from sleep(1)

    def start_publishing(self):
        runner = ApplicationRunner(url=u"wss://demo.crossbar.io/ws", realm=u"realm1")
        runner.run(PublishStock.PublishStockRunner)

if __name__ == '__main__':
    pub_stock = PublishStock()
    pub_stock.start_publishing()
