# Music Api

## Introduction

This is a json web service that allow to manage an online music store. The items are stored in a MongoDB database. I have used MongoDB Atlas to store my data. There are three collections inside the database : albums, artists and trakcs. Each collection contain the data type of their name (the collection albums contains albums).

The format of the data is : 

 - type : the type of the data. This is the name of the collection where the data is stored (ex: track).
 
 - id : the id of the data inside the database. The id is mainly used to find item make difference between the data (ex: 123).
 
 - tags : this is a list which contains all tags associated to the item. We can use the Api to add tags to the item we want (ex: tag_a)
 
This api has been implemented in Python 3.

## Solution used

The items are store in a MongoDB cloud database. To communicate with this database, I have designed Python scripts and I have used the Flask library. This allow me to make PUT, POST or GET request to manage the database.

I have created four Python scripts : 
 
 - api.py is the main script. This is the script which take the request and use several functions to get data from the database.
 
 - albums.py has all functions which interact with the albums collection.
 
 - artists.py has all functions which interact with the artists collection.

 - tracks.py has all functions which interact with the tracks collection.
 
 
 ## Setup
 
 You have to get following packages installed on your machine. You get them with the following Linux commands:
 
 - Flask restful
 ```bash
 sudo apt install python3-flask-restful
 ```
 
  - Flask PyMongo
  ```bash
 python3 -m pip install flask_pymongo
 ```
 
   - PyMongo
  ```bash
 pip3 install pymongo
 ```
 
 - DNSPython
 ```bash
 python3 -m pip install dnspython
 ```
 
 Then use the REST Client Insomnia to make rest request.
 
 ## Run
 
 ### Run the Api
 
 The Api runs on Linux. Open a konsole and go to the directory where your project is. This directory must contain the four Python scripts. 
 
 Run: 
  ```bash
 python3 api.py
 ```
 The Api will run on the port 5000. You will have a message to tell you that the server is running.
 
 ### Make requests
 
 Open Insomnia and type the following request:
 
 ```bash
GET http://127.0.0.1:5000/artists/all
 ```
 This request will return all the artists in database. This works in replacing artists by albums or tracks too.
 
 You can also add a new artist or remove all the artists from the database.
 
 1. Add tags to content
 
 2. Get content list from a tag set
 
 3. Export all the tagged content
