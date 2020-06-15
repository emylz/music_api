#Import flask to run the Api et send requests
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

from json import dumps

#These are the scripts where the funtions are
from artists import *
from albums import *
from tracks import *


app = Flask(__name__)

#Access to the MongoDB database
app.config['MONGO_DBNAME'] = 'music_store'
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:dbUserPassword@music-wrace.mongodb.net/music_store?retryWrites=true&w=majority'

mongo = PyMongo(app)

#Artists urls and functions
@app.route('/artists/all', methods=['GET'])
def all_artists():
	return get_all_artists()

@app.route('/artists/remove', methods=['POST'])
def artists_remove():
	return remove_all_artists()

@app.route('/artists/add', methods=['POST'])
def artists_add():
	return add_artist()

@app.route('/artists/<id_artist>', methods=['POST'])
def tag_artists(id_artist):
	return add_tags_artists(id_artist)

@app.route('/artists')
def artist_by_tag():
    return search_by_tag_artists()

#Albums urls and function
@app.route('/albums/all', methods=['GET'])
def all_albums():
    return get_all_albums()

@app.route('/albums/remove', methods=['POST'])
def albums_remove():
    return remove_all_albums()

@app.route('/albums/add', methods=['POST'])
def album_add():
    return add_album()

@app.route('/albums/<id_album>', methods=['POST'])
def tag_albums(id_album):
    return add_tags_albums(id_album)

@app.route('/albums')
def album_by_tag():
    return search_by_tag_albums()


#Tracks urls and fuctions
@app.route('/tracks/all', methods=['GET'])
def all_tracks():
    return get_all_tracks()

@app.route('/tracks/remove', methods=['POST'])
def tracks_remove():
    return remove_all_tracks()

@app.route('/tracks/add', methods=['POST'])
def tracks_add():
    return add_track()

@app.route('/tracks/<id_track>', methods=['POST'])
def tag_tracks(id_track):
    return add_tags_tracks(id_track)

@app.route('/tracks')
def tracks_by_tag():
    return search_by_tag_tracks()

#Write a json file line by line without json array
def exportJson(results, path):
    n = len(results)
    tmp = ""
    for i in range(n):
        tmp += "{\"type\":\""+results[i]['type']+"\", \"id\":"+str(results[i]['_id'])+", \"tags\":"+dumps(results[i]['tags'])+"}\n"
    open(path + ".json", "w").write(tmp)

@app.route('/export')
def export():

    #Get all data collections
    artists = mongo.db.artists
    albums = mongo.db.albums
    tracks = mongo.db.tracks

    #Get all data from all collections
    results = list(artists.find())
    results += list(albums.find())
    results += list(tracks.find())

    #This is our output result
    output = []

    #Store results in an array to write a json file and send a response
    for r in results:
        output.append({'type':r['type'], 'id':r['_id'], 'tags':r['tags']})

    #Write localy a json file
    exportJson(results, "export")
    print("Json file has been wrote in your directory")


    #This is the response send by the Api
    return jsonify([r for r in results])




if __name__ == '__main__':
    app.run(debug = True)