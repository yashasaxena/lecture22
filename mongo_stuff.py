from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask,request, jsonify
import json

app = Flask(__name__)
connect("mongodb://localhost:27017/lec22_db")

class User(MongoModel):
    name = fields.CharField()
    age = fields.IntegerField()
    bmi = fields.FloatField()



@app.route("/api/new_patient", methods=['POST'])
def new_patient():
    patient_dict = request.json
    patient_name = patient_dict['name']
    patient_age = patient_dict['age']
    patient_bmi = patient_dict['bmi']

    new_p = User(name = patient_name[0], age = patient_age[0],bmi = patient_bmi[0])
    new_p.save()

    return "You did it!"
