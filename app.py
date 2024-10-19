from flask import Flask, jsonify
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()

    # Get server time in IST
    now_ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

    # Get the top output
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode('utf-8')

    # Display the information
    return f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p>Name: Your Full Name</p>
            <p>Username: {username}</p>
            <p>Server Time (IST): {now_ist.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
