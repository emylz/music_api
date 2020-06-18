#Import flask to run the Api and send requests
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

#Access to the MongoDB database
app.config['MONGO_DBNAME'] = 'music_store'
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:dbUserPassword@music-wrace.mongodb.net/music_store?retryWrites=true&w=majority'

mongo = PyMongo(app)



def remove_all_artists():

    #Get the collection of artists
    artists = mongo.db.artists
    
    #Remove all records in the database
    artists.remove()

    #Response by the Api
    return jsonify({'remove':'ok'})



def get_all_artists():

    #Get the collection of artists
    artists = mongo.db.artists

    #Output where results will be stored
    output = []

    #Find all artists and get their attributs : type, ID and tags
    for a in artists.find():
        output.append({'type':a['type'], 'id':a['_id'], 'tags':a['tags']})

    #Response by the Api
    return jsonify({'result':output})



def add_artist():

    #Get the collection of artists
    artists = mongo.db.artists

    #Get information from the json file used as input
    id_artist = request.json['id']
    tags_artist = request.json['tags']
    type_artist = request.json['type']

    
    #Check if the type the item is good
    if(type_artist != "artist"):
        return  "Wrong type", 400

    #Insert the artist in the database
    #insert function return the id
    artist_id = artists.insert({'type':type_artist, '_id' : id_artist, 'tags' : tags_artist})

    #Get the artist information from the database with its id (artist_id)
    new_artist = artists.find_one({'_id' : id_artist})

    #Check if the information are corrects in the database
    output = {'type':new_artist['type'], 'id' : new_artist['_id'], 'tags' : new_artist['tags']}

    #Show the content of the artist inserted as response
    #to check if the information are corrects
    return jsonify({'result': output})



def add_tags_artists(id_artist):

    #Get the collection of artists    
    artists = mongo.db.artists

    #Id passed in the url request
    id_artist = int(id_artist)

    #Search the record with the id in parameters
    current = artists.find_one({'_id' : id_artist})
    
    #Get its current tags
    tags = current['tags']

    #Add new tags to the current list of tag if they are not already in
    for tag in request.json:
        if(tag not in tags):
            tags.append(tag)

    #Update the database with the new information
    artists.update({'_id' : id_artist}, {'$set' : {'tags' : tags}})
    
    #Get the updated artist to check if the tags have been add
    updated_artist = artists.find_one({'_id' : id_artist})

    #The output result with the information of the updated artist
    output = {'type':updated_artist['type'], 'id' : updated_artist['_id'], 'tags' : updated_artist['tags']}

    #Show the content of the updated artist as response
    #to check if the information are corrects
    return jsonify({'result':output})



def search_by_tag_artists(): 

    #Get the collection of artists
    artists = mongo.db.artists

    #Get all the tags from the url request
    tags = request.args.getlist('tags[]')

    #Preparing the response body
    output = []

    #Find and get all the artists having the matching tags
    for artist in artists.find({"tags":{"$all":tags}}):
        output.append(artist['_id'])

    #Response from the Api
    return jsonify(output)

    
