# Music Api

## Introduction

This is a json web service that allow to manage an online music store. The items are stored in a MongoDB database. I have used MongoDB Atlas to store my data. There are three collections inside the database : albums, artists and trakcs. Each collection contain the data type of their name (the collection albums contains albums).

The format of the data is : 

 - type : the type of the data. This is the name of the collection where the data is stored (ex: track).
 
 - id : the id of the data inside the database. The id is mainly used to find item make difference between the data (ex: 123).
 
 - tags : this is a list which contains all tags associated to the item. We can use the Api to add tags to the item we want (ex: tag_a)
 

## Solution used

The items are store in a MongoDB cloud database. To communicate with this database, I have designed Python scripts and I have used the Flask library. This allow me to make PUT, POST or GET request to manage the database.

I have created four Python scripts : 
 
 - api.py is the main script. This is the script which take the request and use several functions to get data from the database.
 
 - albums.py has all functions which interact with the albums collection.
 
 - artists.py has all functions which interact with the artists collection.

 - tracks.py has all functions which interact with the tracks collection.
 
 
 ## Setup
 
 You have to get following packages installed on your machine:
 
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
