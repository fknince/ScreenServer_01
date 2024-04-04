from flask import Flask, request, jsonify
from pyngrok import ngrok
from idle_screen import showScreen
import random
import threading
import atexit

app = Flask(__name__)
SERVER_PORT = 5000
SCREEN_ID="PCE_001"
NGROK_URL=""

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming JSON payload
    data = request.json
    print("Received webhook data:", data)
    
    # Process the data as needed
    
    # Respond back to the sender
    return jsonify({"status": "success", "message": "Data received"}), 200

if __name__ == '__main__':
    http_tunnel = None
    try:
        # Create a flag to indicate if the ngrok thread is running
        ngrok_running = False

        # Create a function to stop the ngrok tunnel
        def stop_ngrok():
            global ngrok_running
            if ngrok_running:
                ngrok.disconnect()
                ngrok_running = False

        # Register the stop_ngrok function to be called at interpreter shutdown
        atexit.register(stop_ngrok)

        print("Server is running on port 5000")
        # Start the Flask app
        # Create a function to run the Flask app in a separate thread
        def run_flask_app():
            app.run(port=5000)

        # Start the Flask app in a separate thread
        flask_thread = threading.Thread(target=run_flask_app)
        flask_thread.start()

        # Setup ngrok
        # Start ngrok in a separate thread
        def start_ngrok():
            global ngrok_running
            ngrok_running = True
            ngrok.connect(5000)

        # Start the ngrok thread
        ngrok_thread = threading.Thread(target=start_ngrok)
        ngrok_thread.start()

        # Join the ngrok thread to ensure it is properly finished before interpreter shutdown
        ngrok_thread.join()

        ngrok_thread = threading.Thread(target=start_ngrok)
        ngrok_thread.start()
        NGROK_URL=ngrok.get_tunnels()[0].public_url
        print("NGROK Tunnel URL:", NGROK_URL)

        # Generate a random two-digit number
        safety_code = random.randint(10, 99)
        # Call the showScreen method
        showScreen(SCREEN_ID, NGROK_URL, str(SERVER_PORT), safety_code, NGROK_URL + "/webhook")
        
    
      

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Clean up the ngrok tunnel
        if http_tunnel:
            ngrok.disconnect(NGROK_URL)
            print("NGROK tunnel disconnected")
