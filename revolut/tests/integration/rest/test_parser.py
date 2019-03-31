

def test_can_parse_json(client_with_db, auth):
    currency_data = [
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
    ]
    expected_json = {
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
    response = client_with_db.post('/parse?nest=currency,country,city', json=currency_data, headers=auth)
    assert response.status_code == 200
    assert response.json == expected_json

def test_can_not_parse_json_due_authentication(client):
    currency_data = [
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
    ]
    
    response = client.post('/parse?nest=currency,country,city', json=currency_data)
    assert response.status_code == 401  