from os import abort
from flask import Blueprint, jsonify, make_response

class Dog:
    def __init__(self, id, name, breed, age, gender):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

# hardcoded database
DOGS = [
    Dog(1, 'John Cena', "pug", 34, "Male"),
    Dog(2, 'Snoop', "hair doberman", 14, "Female"),
    Dog(3, "Doug 'the Doctor', M.D.", "pompom", 10, "Male")
]

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@dogs_bp.route('', methods=['GET'])
def get_all_dogs():
    dog_response = [vars(dog) for dog in DOGS]
    return jsonify(dog_response)

@dogs_bp.route('/<id>', methods = ['GET'])
def get_one_dog(id):
    dog = validate_dog(id)
    return dog
    

    #Validation function
def validate_dog(id):
    #handle invalid data types such as non-ints
        
    try:
        dog_id = int(dog_id)
    except ValueError:
        return {
                "message":f"dog{dog_id} invalid"
        }, 400
        #if id is not found
    for dog in DOGS:
        if dog.id ==dog_id:
            return vars(dog)
    abort(make_response(jsonify(description ="Resource not found"),404))

   


    # print(type(dog_response))
    # print(type(jsonify(dog_response)))
    # return jsonify(dog_response)