from revolut.domain.json_parser import CurrencyJson

def test_add_one_currency():
    currency = CurrencyJson([
        {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
    },
    ])

    currency.parse()
    assert currency.output == {
        "GBP": {
        "UK": {
        "London": [
            {
            "amount": 12.2
            }
        ]
        }
    },
    }

def test_add_two_currencies():
    currency = CurrencyJson([
        {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
        },
        {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
        },
    ])

    currency.parse()
    assert currency.output == {
        "GBP": {
        "UK": {
        "London": [
            {
            "amount": 12.2
            }
        ]
        }
        },
        "EUR": {
        "FR": {
        "Paris": [
            {
            "amount": 20
            }
        ]
        }
        },
    }

    
