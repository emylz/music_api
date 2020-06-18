#Import flask to run the Api and send requests
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

#Access to the MongoDB database
app.config['MONGO_DBNAME'] = 'music_store'
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:dbUserPassword@music-wrace.mongodb.net/music_store?retryWrites=true&w=majority'

mongo = PyMongo(app)



def remove_all_tracks():

    #Get the collection of tracks
    tracks = mongo.db.tracks

    #Remove all records in the database
    tracks.remove()

    #Response by the Api
    return jsonify({'remove':'ok'})



def get_all_tracks():

    #Get the collection of tracks
    tracks = mongo.db.tracks

    #Output where results will be stored
    output = []

    #Find all tracks and get their attributs : type, ID and tags
    for a in tracks.find():
        output.append({'type':a['type'], 'id':a['_id'], 'tags':a['tags']})

    #Response by the Api
    return jsonify({'result':output})



def add_track():

    #Get the collection of tracks
    tracks = mongo.db.tracks

    #Get information from the json file used as  input
    id_track = request.json['id']
    tags_track = request.json['tags']
    type_track = request.json['type']
    

    #Check if the type the item is good
    if(type_track != "track"):
        return  "Wrong type", 400

    #Insert the track in the databse
    #insert function return the id
    track_id = tracks.insert({'type':type_track, '_id' : id_track, 'tags' : tags_track})

    #Get the track information from the database with its id (track_id)
    new_track = tracks.find_one({'_id' : id_track})

    #Check if the information are corrects in the database
    output = {'type':new_track['type'], 'id' : new_track['_id'], 'tags' : new_track['tags']}

    #Show the content of the track inserted as response
    #to check if the information are corrects
    return jsonify({'result': output})



def add_tags_tracks(id_track):

    #Get the collection of tracks  
    tracks = mongo.db.tracks

    #Id passed in the url request
    id_track = int(id_track)

    #Search the record with the id in parameters
    current = tracks.find_one({'_id' : id_track})

    #Get its current tags
    tags = current['tags']

    #Add new tags to the current list of tag if they are not already in
    for tag in request.json:
        if(tag not in tags):
            tags.append(tag)

    #Update the database with the new information
    tracks.update({'_id' : id_track}, {'$set' : {'tags' : tags}})

    #Get the updated track to check if the tags have been add
    updated_track = tracks.find_one({'_id' : id_track})

    #The output result with the information of the updated track
    output = {'type':updated_track['type'], 'id' : updated_track['_id'], 'tags' : updated_track['tags']}

    #Show the content of the updated track as response
    #to check if the information are corrects
    return jsonify({'result':output})



def search_by_tag_tracks():

    #Get the collection of tracks
    tracks = mongo.db.tracks

    #Get all the tags from the url request
    tags = request.args.getlist('tags[]')

    #Preparing the response body
    output = []

    #Find and get all the tracks having the matching tags
    for track in tracks.find({"tags":{"$all":tags}}):
        output.append(track['_id'])
    
    #Response from the Api
    return jsonify(output)
