# Music Api

## Table of contents

- [Introduction](#link1)
- [Solution used](#link2)
- [Setup](#link3)
- [Run](#link4)
   - [Run the Api](#link5)
   - [Make requests](#link6)
        1. [Add tags to content](#link7)
        2. [Get content list from a tag set](#link8)
        3. [Export all the tagged content](#link9)

## Introduction  <a id="link1">

This is a json web service that allow to manage an online music store. The items are stored in a MongoDB database. I have used MongoDB Atlas to store my data. There are three collections inside the database : albums, artists and trakcs. Each collection contain the data type of their name (the collection albums contains albums).

The format of the data is : 

 - type : the type of the data. This is the name of the collection where the data is stored (ex: track).
 
 - id : the id of the data inside the database. The id is mainly used to find item to make a difference between the data (ex: 123).
 
 - tags : this is a list which contains all tags associated to the item. We can use the Api to add tags to the item we want (ex: tag_a).
 
This api has been implemented with Python 3 for Linux.

## Solution used  <a id="link2">

The items are store in a MongoDB cloud database. To communicate with this database, I have designed Python scripts and I have used the Flask library. This allow me to make PUT, POST or GET request to manage the database.

I have created four Python scripts : 
 
 - api.py is the main script. This is the script which take the request and use several functions to get data from the database.
 
 - albums.py has all functions which interact with the albums collection.
 
 - artists.py has all functions which interact with the artists collection.

 - tracks.py has all functions which interact with the tracks collection.
 
 
 ## Setup  <a id="link3">
 
 You have to get following packages installed on your machine. You can get them with the following Linux commands:
 
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
 
 ## Run  <a id="link4">
 
 ### Run the api  <a id="link5">
 
 The Api runs on Linux. Open a console and go to the directory where your project is. This directory must contain the four Python scripts. 
 
 Run: 
  ```bash
 python3 api.py
 ```
 The Api will run on the port 5000. You will have a message to tell you that the server is running.
 
 ### Make requests  <a id="link6">
 
 Open Insomnia and type the following request:
 
 ```bash
GET http://127.0.0.1:5000/artists/all
 ```
 This request will return all the artists in database. This works in replacing artists by albums or tracks too.
 
 To add a new artist in the database use:
  ```bash
POST http://127.0.0.1:5000/artists/add
 ```
 You have to add a json body with the request in Insomnia of this format :
  ```bash
{"type":"artist", "id":id (int), "tags":["tag_1", ... , "tag_n"]}
 ```

 You can also remove all the artists in the database with : 
 
   ```bash
DELETE http://127.0.0.1:5000/artists/remove
 ```
 
 The previous urls requests work with the collections albums and tracks too.
 
 **1. Add tags to content** <a id="link7">
 
 Use the following request:
  ```bash
POST http://127.0.0.1:5000/artists/id
 ```
 where id is the id of the item where you want to add tags. Artists is the collection. This is the same for albums and tracks. Do not forget to pass json array in the body of your request which contains the tags.
 
 **2. Get content list from a tag set** <a id="link8">
 
  Use the following request:
  ```bash
GET http://127.0.0.1:5000/tracks?tags[]=tag_a&tags[]=tag_f
 ```
where tag_a and tag_b are the tags wich must be in the tags list of the returned items. Replace tracks by albums or artists to get the albums or artists items.
There will be a json array of response where the content will be all the id of the items that have the tags in parameters.
 
 **3. Export all the tagged content** <a id="link9">

  Use the following request:
  ```bash
GET http://127.0.0.1:5000/export
 ```
This request will get all data from all the collections. A json file will be created where each line is an item from the database.
There will be a json response in Insomnia with the result of the request.
