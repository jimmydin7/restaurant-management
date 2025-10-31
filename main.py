from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



def app_run(alt_port, dev_mode=False):
    if dev_mode:
        app.debug = True
    port = int(os.getenv("PORT", alt_port))
    app.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    app_run(5000, dev_mode=True)