from pymongo import MongoClient

# MongoDB connection using ec2 instance publc ip and standard MondoDB port 
client = MongoClient('mongodb://localhost:27017/')

# DBs
auth_db = client['myflix_auth']
video_db = client['myflix_video']
watchlist_db = client['myflix_watchlist']

# Insert test data into users collection
auth_db['users'].insert_many([
    {
        "id": "0001",
        "username": "johndoe",
        "firstname": "john",
        "surname": "doe",
        "password": "password123",
        "email": "johndoe@example.com",
        
    },
    {
        "id": "0002",
        "username": "brucewayne",
        "firstname": "bruce",
        "surname": "wayne",
        "password": "batman",
        "email": "wayne@email.com",    
    },
    {
        "id": "0003",
        "username": "donaldduck",
        "firstname": "donald",
        "surname": "duck",
        "password": "password",
        "email": "donaldduck@address.com",   
    },
    {
        "id": "0004",
        "username": "robertsmith",
        "firstname": "robert",
        "surname": "smith",
        "password": "12345678",
        "email": "smith@example.com",   
    },
    {
        "id": "0005",
        "username": "peterstewart",
        "firstname": "peter",
        "surname": "stewart",
        "password": "password123",
        "email": "pete@emailacc.com",   
    },
    {
        "id": "0006",
        "username": "janemurdoch",
        "firstname": "jane",
        "surname": "murdoch",
        "password": "password123",
        "email": "johndoe@example.com",   
    },
    {
        "id": "0007",
        "username": "lucymckenzie",
        "firstname": "lucy",
        "surname": "mckenzie",
        "password": "passwordpassword",
        "email": "lucy@example.com",    
    }
])

video_db['videos'].insert_many([
    {
        "video": {
            "server": 1,
            "Name": "Big Buck Bunny",
            "file": "bbb.mp4",
            "thumb": "bbb-th.png",
            "pic": "bbb.png",
            "uuid": "380613d5-71b3-4f24-8a58-ca1a260b49d3",
            "category": ["animation", "demo"]
        }
    },
    {
        "video": {
            "server": 1,
            "Name": "Python Learning",
            "file": "python-basics.mp4",
            "thumb": "python-th.png",
            "pic": "python.png",
            "uuid": "7c462d8a-9b2e-4f3d-bc64-d8aa7bce5291",
            "category": ["animation", "shorts"]
        }
    },
    {
        "video": {
            "server": 1,
            "Name": "Database Design",
            "file": "db-design.mp4",
            "thumb": "db-th.png",
            "pic": "db.png",
            "uuid": "9f523e7c-8cd4-4dc1-9e9a-54f7ae3f0a82",
            "category": ["animation", "demo"]
        }
    }
])

# Insert data into watchlists collection
watchlist_db['watchlists'].insert_many([
    {
        "username": "johndoe",
        "videos": ["mongodb-intro", "docker-advanced"],
    },
    {
        "username": "janedoe",
        "videos": ["docker-advanced"],
    }
])

print("Test data inserted successfully!")
