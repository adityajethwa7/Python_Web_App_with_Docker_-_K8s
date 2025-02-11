from flask import Flask
import time
import math

app = Flask(__name__)

@app.route('/cpu-intensive')
def cpu_intensive():
    # Efficient CPU-intensive simulation
    return f"Processed: {sum(math.sqrt(x) for x in range(100000))}\n"

@app.route('/health')
def health():
    return "Healthy\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)