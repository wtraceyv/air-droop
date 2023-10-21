from flask import Flask, jsonify, request
from flask_cors import CORS

import db_actions
import bundle_html

app = Flask(__name__)
CORS(app)

@app.get('/hello')
def hello():
	return "Hi, you have reached the api."

@app.get('/getlinks')
def getlinks():
	links = db_actions.get_all_links()
	return links

# send me json in body with "url" param
@app.post('/addlink')
def addlink():
	newlink = request.json["url"]
	db_actions.insert_link(newlink)
	bundle_html.bundle_full()
	return f'New link added: {newlink}'

@app.post('/deletelink')
def deletelink():
	todelete = request.json["url"]
	db_actions.delete_link(todelete)
	bundle_html.bundle_full()
	return f'Link deleted: {todelete}'

@app.post('/resetdb')
def resetdb():
	db_actions.reset_db()
	bundle_html.bundle_full()
	return "Links database reset."