from flask import Flask , render_template , request,url_for
from response import get_response
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/' )
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/firstFloorMap')
def firstFloorMap():
	return render_template('firstFloorMap.html')


@app.route('/groundFloorMap')
def groundFloorMap():
	return render_template('groundFloorMap.html')

@app.route('/toMap')
def toMap():
	return render_template('toMap.html')

@app.route('/firstFloorTouchMap')
def firstFloorTouchMap():
	return render_template('firstFloorTouchMap.html')


@app.route('/groundFloorTouchMap')
def groundFloorTouchMap():
	return render_template('groundFloorTouchMap.html')


@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    chat =get_response(userText)
    return chat	


if __name__ == "__main__":
	app.run()

