from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "luu歡迎來到flask"
if __name__ == "__main__":
	app.run()
