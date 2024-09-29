from flask import Flask, render_template, jsonify
import psutil
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats():
    cpu_info = {
        'cpu_cores': psutil.cpu_count(),
        'cpu_usage_percent': psutil.cpu_percent(interval=1)
    }
    memory_stats = {
        'total_memory': int(psutil.virtual_memory().total / (1024 ** 2)),
        'used_memory': int(psutil.virtual_memory().used / (1024 ** 2)),
        'available_memory': int(psutil.virtual_memory().available / (1024 ** 2)),
    }
    return jsonify(cpu_info=cpu_info, memory_stats=memory_stats)

@app.route('/visual')
def visual():
    return render_template('visual.html')

if __name__ == '__main__':
    app.run(debug=True)
