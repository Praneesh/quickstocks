#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

from flask import Flask,jsonify
from flask_swagger import swagger

from qs_backend.controllers.subscriptions_controller import SubscriptionsAPI

app = Flask(__name__, static_url_path='/static')

@app.route("/qs/spec")
# Instantiating "spec" route for Swagger API Documentation
def spec():
    swag = swagger(app)
    swag['info']['version'] = "0.1"
    swag['info']['title'] = "Quick Stocks APIs"
    return jsonify(swag)

# Instantiating SubscriptionsAPI class for all the helpers !
subscriptionsAPI = SubscriptionsAPI()
app.add_url_rule('/qs/subscribe',
                 view_func=subscriptionsAPI.register_qs_client)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
