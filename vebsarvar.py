import time


def app(environ, start_response):
    # Test:
    # wrk -d30s -t12 -c400 http://localhost:8000
    date = bytes("Today is " + time.asctime(), encoding='utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(date)))
    ])

    return iter([date])
