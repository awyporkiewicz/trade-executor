import websocket
import rel


def _on_message(ws, message):
    print(message)


def _on_error(ws, error):
    print(error)


def _on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def _on_open(ws):
    print("Opened connection")


def get_book_ticker_stream():
    order_book_websocket = "wss://stream.binance.com:9443/ws/bnbusdt@bookTicker"
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        order_book_websocket,
        on_close=_on_close,
        on_error=_on_error,
        on_message=_on_message,
        on_open=_on_open,
    )
    ws.run_forever(dispatcher=rel, reconnect=10)
    rel.signal(2, rel.abort)
    rel.dispatch()
