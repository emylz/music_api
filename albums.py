#Import flask to run the Api and send requests
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

#Access to the MongoDB database
app.config['MONGO_DBNAME'] = 'music_store'
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:dbUserPassword@music-wrace.mongodb.net/music_store?retryWrites=true&w=majority'

mongo = PyMongo(app)



def remove_all_albums():

    #Get the collection of albums
    albums = mongo.db.albums

    #Remove all records in the database
    albums.remove() 

    #Response by the Api
    return jsonify({'remove':'ok'})



def get_all_albums():

    #Get the collection of artists
    albums = mongo.db.albums

    #Output where results will be stored
    output = []

    #Find all albums and get their attributs : type, ID and tags
    for a in albums.find():
        output.append({'type':a['type'], 'id':a['_id'], 'tags':a['tags']})
    
    #Response by the Api
    return jsonify({'result':output})



def add_album():

    #Get the collection of artists
    albums = mongo.db.albums

    #Get information from the json file used as input
    id_album = request.json['id']
    tags_album = request.json['tags']
    type_album= request.json['type']
    

    #Check if the type of the item is right
    if(type_album != "album"):
    	return  "Wrong type", 400
    

    #Insert the album in the database
    #insert function return the id
    album_id = albums.insert({'type':type_album, '_id' : id_album, 'tags' : tags_album})

    
    #Get the album information from the database with its id (album_id)
    new_album = albums.find_one({'_id' : album_id})

    
    #Check if the information are correct in the database
    output = {'type':new_album['type'], 'id' : new_album['_id'], 'tags' : new_album['tags']}

    
    #Show the content of the album inserted as response
    #to check if the information are correct
    return jsonify({'result': output})



def add_tags_albums(id_album):

    #Get the collection of artists    
    albums = mongo.db.albums

    #Id passed in the url request
    id_album = int(id_album)

    #Search the record with the id in parameters
    current = albums.find_one({'_id' : id_album})

    #Get its current tags
    tags = current['tags']

    #Add new tags to the current list of tag if they are not already in
    for tag in request.json:
        if(tag not in tags):
            tags.append(tag)

    #Update the database with the new information
    albums.update({'_id' : id_album}, {'$set' : {'tags' : tags}})

    #Get the updated album to check if the tags have been add
    updated_album = albums.find_one({'_id' : id_album})

    #The output result with the information of the updated album
    output = {'type':updated_album['type'], 'id' : updated_album['_id'], 'tags' : updated_album['tags']}

    #Show the content of the updated album as response
    #to check if the information are correct
    return jsonify({'result':output})



def search_by_tag_albums():

    #Get the collection of albums
    albums = mongo.db.albums

    #Get all the tags from the url request
    tags = request.args.getlist('tags[]')

    #Preparing the response body
    output = []

    #Find and get all the albums which have the matching tags
    for album in albums.find({"tags":{"$all":tags}}):
        output.append(album['_id'])

    #Response from the Api
    return jsonify(output)

