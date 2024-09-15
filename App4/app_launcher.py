import bottle
import app
import webbrowser
import threading
import time

# def start_browser():
#     time.sleep(1)  # Wait for 1 second to ensure the server has started
#     webbrowser.open('http://localhost:8080')

if __name__ == '__main__':
    # Start the browser-opening function in a new thread
    # threading.Thread(target=start_browser, daemon=True).start()
    
    # Run the Bottle application
    bottle.run(host='localhost', port=8080)
    
    # todo: display program title as site name in the browser title
