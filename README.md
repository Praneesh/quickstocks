# quickstocks
Quickstock is a full stack stock ticker application. This is developed for experimentation and is a playground project. No commercial use intended.

## The Application

The application is built on Python and heavily relies on Publish and Subscribe mechanisms.The services are intended to be deployed independently to achieve the cloud scale.

## Moving Parts

This semi-hybrid monolithic and micro-service application has 3 major moving parts.
- qs_backend
    - Holds the core functionality of the QuickStocks application, and does the heavy lifting.
    - It has 3 sub services that run independently exchanging information using Python Queues and Crossbar router
        - backend.py  : Responsible for invoking threads for stock quotes as per all user preferences. Stock Worker threads invoke Yahoo Finance APIs to fetch stock quotes. A thread is spawned per stock quote which is responsible for fetching stock information and prepares it for consumption. Thread pool could have been an ideal one here (TO DO). Along with spawning Stock Workers, backend.py also starts one instance of a Publisher. Publisher is responsible for pulling the stock packets, that were put in StockDeliverQueue(Python queue) by Stock Worker threads, and publishes them to a topic on a Crossbar.io router instance.

        - api.py : Holds the APIs responsible for managing the state of the entire system. REST APIs allow to set user stock preferences into the system along with a few other book keeping operations.

        - pgcm/gcm_forwarder.py : Google Cloud Messaging service allows sending desktop notifications via a browser. Quickstocks has a built in web site as a GUI which would let users view their stock-picks. Hence GCM Push notifications support is included as a part of the application which today notifies users on a change in stock value. Extending it a little more further to support Firebase Cloud Messaging would have enabled us to send the updated stock information via a notification without the user having to navigate to the website (TO DO).

- qs_dispatcher
    - Responsible for dispatching stock packets to all the subscribers. The current mode of dispatching is via WAMP + Crossbar routing. Dispatcher listens for messages from Publisher (in qs_backend) for stock updates. This service unwraps the stock message packets, finds out the destinations and places the respective stock packets in associated topics - on which the hungry subscribers (like our website - qs_web) is listening on.
    - This service can later be extended to support multiple dispatching options, like SMS, E Mail Notifications, cloud to mobile push etc. qs_backend/pgcm/gcm_forwarder should be yet another dispatcher ideally, but is grouped in qs_backend module for simplicity and reaching to a faster solution.

- qs_web
    - Web application would help a user to search and pick a company and to follow its stock trends. This application is dependent on the qs_dispatcher to receive updates and stock data. qs_dispatcher uses a demo instance of Crossbar router and can not be run 24 X 7. Hence the landing page would look empty initially with the dispatcher turned off.
    - A screen shot of the running application is available in demo directory - https://github.com/Praneesh/quickstocks/blob/master/demo/QuickStocks_UI.png
