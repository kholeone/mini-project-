from application import app
from flask import request, Response
from random import randint

@app.route('/animal/name', methods = ['GET'])
def animal_name():
    animals = ['cat','dog','cow']
    return Response(animals[randint(0,2)], mimetype = 'text/plain')

#this is determined from information that needs to be sent aka POST method]
@app.route('/animal/noise', methods = ['POST'])
def animal_noise():
    animal = request.data.decode("utf-8")
#the post requests comes in the form above, by changing this to a variable we can see it in plain text
    if animal == "cat":
        noise = "meow"
    elif animal == "dog":
        noise = "woof"
    elif animal == "cow":
        noise = "mood"
    else:
        noise = "We don't know!"
    return Response(noise, mimetype= 'text/plain')
