from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import json

app = Flask(__name__)

line_bot_api = LineBotApi('8/hRbrU3sIrSyschT5rROA3op82CuXbNOP+cniUTWT78GCsRmCrKG0kuQio1aL65ss9qXWj3eQNVdyM6U6RWpMUCrfutAWhwQgFUJMvxhLvLqT3mSN3rvRiyWF/pDVT55PQ1WN1PvE58aXG3b60jbAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a122e27d9ed05955063e82042bbc9745')


@app.route("/callback", methods=['POST'])
def callback():
    
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return body

if __name__ == "__main__":
    app.run()