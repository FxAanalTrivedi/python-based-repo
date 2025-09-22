# sample_exceptions.py

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def connect_to_server(url):
    if not url.startswith("https://"):
        raise HTTPSException("Only HTTPS connections are allowed")

def process_data(data):
    if data is None:
        raise Exception("Data cannot be None")
    return data.upper()


if __name__ == "__main__":
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Caught: {e}")

    try:
        connect_to_server("http://example.com")
    except Exception as e:
        print(f"Caught: {e}")

    try:
        process_data(None)
    except Exception as e:
        print(f"Caught: {e}")
