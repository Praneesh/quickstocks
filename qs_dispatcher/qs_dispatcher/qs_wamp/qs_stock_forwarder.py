#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"
#
#   Step 1: Reads the Stock Packets from Dispatcher Queue
#   Step 2: Places the packets in respective queues


from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from asyncio import coroutine, sleep


class SubscriberComponent(ApplicationSession):

    @coroutine
    def onJoin(self, details):
        print("WAMP+Crossbar - Dispatcher ::  Subscriber Session Available")

        con_topic_to_subscribe = u'com.quickstocks.publisher.b6b7'

        def on_stockspacket(stocks_data):
            # Step 0: Iterate through the packet, it may have multiple interested subscribers !
            # Step 1: For each stock packet, pick the stock subscriber topic from the packet and push it !
            if stocks_data is None:
                return
            for user_stock_id in stocks_data:
                stock_publish_topic = stocks_data[user_stock_id]['publish_queue']
                stock_payload_to_publish = stocks_data[user_stock_id]
                self.publish(stock_publish_topic, stock_payload_to_publish)

                print("Forwarded Stock Item to User Queue {} : {}".format(stock_publish_topic,
                                                                          stock_payload_to_publish['stock_unit']))

                yield from sleep(1)

        try:
            yield from self.subscribe(on_stockspacket, con_topic_to_subscribe)
            print("WAMP+Crossbar - Dispatcher ::  Subscriber to Quick Stocks : Stock Queue Default Topic")
        except Exception as e:
            print("Could not subscribe to topic {0}".format(e))


if __name__ == '__main__':
    runner = ApplicationRunner(url=u"wss://demo.crossbar.io/ws",realm=u"realm1")
    runner.run(SubscriberComponent)



