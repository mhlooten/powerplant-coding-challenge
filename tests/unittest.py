import pytest
from main import app
import json

@pytest.fixture
def client():

    app.config['TESTING'] = True
    client = app.test_client()

    yield client

#Error when json is empty
def test_post_empty(client):
    response = client.post("/productionplan", json={})
    assert response.status_code == 400 

#Assert a correct input
def test_post_correct(client):
    data = json.dumps({
        "load": 910,
        "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": [
            {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
            },
            {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
            },
            {
            "name": "gasfiredsomewhatsmaller",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 210
            },
            {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
            },
            {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
            },
            {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
            }
        ]
    })
    response = client.post("/productionplan", data=data, content_type="application/json")
    assert response.status_code == 200 

#Error an input with missing fields
def test_post_missing(client):
    data = json.dumps({
        "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": [
            {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
            },
            {
            "name": "gasfiredbig2",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
            },
            {
            "name": "gasfiredsomewhatsmaller",
            "type": "gasfired",
            "efficiency": 0.37,
            "pmin": 40,
            "pmax": 210
            },
            {
            "name": "tj1",
            "type": "turbojet",
            "efficiency": 0.3,
            "pmin": 0,
            "pmax": 16
            },
            {
            "name": "windpark1",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 150
            },
            {
            "name": "windpark2",
            "type": "windturbine",
            "efficiency": 1,
            "pmin": 0,
            "pmax": 36
            }
        ]
    })
    response = client.post("/productionplan", data=data, content_type="application/json")
    assert response.status_code == 400

#Error an input with an empty powerplant list
def test_post_empty(client):
    data = json.dumps({
        "load": 910,
        "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": []
    })
    response = client.post("/productionplan", data=data, content_type="application/json")
    assert response.status_code == 400

#Error an unsolvable input
def test_post_unsolvable(client):
    data = json.dumps({
        "load": 910,
        "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": [
            {
            "name": "gasfiredbig1",
            "type": "gasfired",
            "efficiency": 0.53,
            "pmin": 100,
            "pmax": 460
            }]
    })
    response = client.post("/productionplan", data=data, content_type="application/json")
    assert response.status_code == 400   

#Test that other methods aren't available
def test_post_empty(client):
    data = json.dumps({
        "load": 910,
        "fuels":
        {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": []
    })
    response = client.put("/productionplan", data=data, content_type="application/json")
    assert response.status_code == 405
    response = client.get("/productionplan")
    assert response.status_code == 405
    response = client.delete("/productionplan")
    assert response.status_code == 405