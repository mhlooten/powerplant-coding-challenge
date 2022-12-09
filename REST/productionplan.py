from flask import request
from flask_restful import Resource
from jsonschema import validate, exceptions
from Objects.Powerplant import Powerplant
from Objects.PowerplantBuilder import PowerplantBuilder
from Algorithms.Solver import solve_greedy
import json

# Schema of expected productionplan json input
productionSchema = {
    "type": "object",
    "properties": {
        "load": {"type": "number"},
        "fuels": {
            "type": "object", 
            "properties": {
                "gas(euro/MWh)": {"type": "number"},
                "kerosine(euro/MWh)": {"type": "number"},
                "co2(euro/ton)": {"type": "number"},
                "wind(%)": {"type": "number"}
            },
            "required": [ "gas(euro/MWh)", "kerosine(euro/MWh)", "co2(euro/ton)", "wind(%)"]
        },
        "powerplants": {
            "type": "array", 
            "items": {
                "type": "object", 
                "properties": {
                    "name": {"type": "string"},
                    "type": {"type": "string"},
                    "efficiency": {"type": "number"},
                    "pmin": {"type": "number"},
                    "pmax": {"type": "number"}
                },
                "required": [ "name", "type", "efficiency", "pmin", "pmax"]
            },
            "minItems": 1,
            "uniqueItems": True
        }
    },
    "required": [ "load", "fuels", "powerplants" ]
}

class Productionplan(Resource):
    def post(self):
        #Only json bodies allowed
        if request.content_type != 'application/json':
            return "Content must be in a json format.", 400
        content = request.json

        #Validate json body
        try:
            validate(instance=content, schema=productionSchema)
        except exceptions.ValidationError as err:
            return err.message, 400

        #Convert json body
        load = content['load']
        fuels = content['fuels']
        payload = list(map(lambda x: PowerplantBuilder.build_powerplant(x["name"], x["type"], x["efficiency"], x["pmin"], x["pmax"], fuels), content['powerplants'])) #List of payload objects
        result_payload, achieved_load, total_load = solve_greedy(payload, load)
        if achieved_load < total_load: #Since we're using a greedy algorithm, some solutions cannot be found
            return "Could not be solved with the greedy algorithm. The maximum load that could be reached was {} MWh (goal: {} MWh)".format(achieved_load, total_load), 400

        return result_payload, 200


