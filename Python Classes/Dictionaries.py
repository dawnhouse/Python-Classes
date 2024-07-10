"""
Dictionary is a collection of key value pairs.

insta_account = {
    name : "John",
    lastName: "Doe",
    password: 123456,
    username: "jone"
    posts: [img1, img2, img3]
}

{
    "name": "Hello",
    "name": "World"
}


{
    "key" : 123456,
    "iters" : 123456
}

insta_account[username] = "Jonas"

It is unordered
It is mutable
Cannot contain duplicate keys

"""

"""

//////////////// WORKING WITH DICTIONARY ////////////

"""

dicti = {
    "name" : "Code Class",
    "username": "code_class_123",
    "posts": [1,2,3,4,5]
}

length_of_dicti = len(dicti) #Getting Length of Keys
dictionary_username =  dicti["username"] #Getting value of a dictionary key
dicti["friends"] = 50 #This is how we add new value in dictionary
dicti["subjects"] = ["English", "Maths", "Hindi"] #This is how we add new value in dictionary

# Get Method
data = dicti.get("likes", ["This is a list type"])


#Pop Method ~ almost like delete
dicti.pop("subjects")

#Pop-item method
#from 3.7 ver popitem only deletes the last key-value pair
popped_item_that_was_deleted = dicti.popitem()


#Delete method



del dicti["posts"]




#Dictionary Traversal

instagram = {
    "user": {
        "Code_Class": ["Username", "Password"],
        
        "Honey Singh": ["Songs"],
        
        "T-series": {
            "Movie-Album": 123456,
            "Solo-Album": 78456
        }
    }
}


facebook = [
    {"user1" : {
            "name": "Lorem",
            "address": "Dipsum",
            "password": 789456,
            "friends": 123}},
    
    {"user2" : {
        "name": "Tamatiya",
        "address": "Sabzi Mandi",
        "password": "nimbu mirchi",
        "friends": 465}}
]

"""
//// REFERENCE COPY AND SHALLOW COPY ////
"""

mark = {
    "Maths": 91,
    "Eng": 81,
    "Sci": 85,
    "SST": 70,
}

# mark["Hindi"] = 88

mark.update({"Hindi": 88, "Game": "A"})

mark.clear() #deletes every key value pair

print(mark)



"""
H.W

=> Make a Twitter Dictionary and add atleast 10 key value pairs and apply every method that is mentioned in the class.

=> Also, prepare verbally to explain your HW in next class

"""




