import json
from revolut.cli.nest import parse_json, parse_args

def test_parse_json():
    json_data = str([
        {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
        },
        {
        "country": "UK",
        "city": "London",
        "currency": "FBP",
        "amount": 10.9
        },
    ])
    json_data = json_data.replace("\'", "\"")
    nest_data = ['currency', 'country', 'city']
    res = parse_json(json_data, nest_data)
    assert res == {
        "GBP": {
        "UK": {
        "London": [
            {
            "amount": 12.2
            }
        ]
        }
        },
        "FBP": {
        "UK": {
        "London": [
            {
            "amount": 10.9
            }
        ]
        }
        },
    }

def test_parse_args():
    json_data, nest_data = parse_args(
        ['--filename', 'example_input.json', 'currency', 'country', 'city'])
    assert nest_data == ['currency', 'country', 'city']
    json_data = json.loads(json_data)
    assert json_data == [
    {
        "country": "US",
        "city": "Boston",
        "currency": "USD",
        "amount": 100
    },
    {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
    },
    {
        "country": "FR",
        "city": "Lyon",
        "currency": "EUR",
        "amount": 11.4
    },
    {
        "country": "ES",
        "city": "Madrid",
        "currency": "EUR",
        "amount": 8.9
    },
    {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
    },
    {
        "country": "UK",
        "city": "London",
        "currency": "FBP",
        "amount": 10.9
    }
]