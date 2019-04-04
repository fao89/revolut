import pytest 
from revolut.use_cases.json_parser import ParseJson


NEST = ['currency', 'country', 'city']

def test_add_one_currency():
    currency = ParseJson([
        {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
    },
    ], NEST)

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
    currency = ParseJson([
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
    ], NEST)

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

def test_add_two_countries_with_same_currency():
    currency = ParseJson([
        {
        "country": "ES",
        "city": "Madrid",
        "currency": "EUR",
        "amount": 8.9
        },
        {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
        },
    ], NEST)

    currency.parse()
    assert currency.output == {
        "EUR": {
            "ES": {
            "Madrid": [
                {
                "amount": 8.9
                }
            ]
            },
            "FR": {
            "Paris": [
                {
                "amount": 20
                }
            ]
            }
        },
    }

def test_add_two_cities_with_same_country():
    currency = ParseJson([
        {
        "country": "FR",
        "city": "Lyon",
        "currency": "EUR",
        "amount": 11.4
        },
        {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
        },
    ], NEST)

    currency.parse()
    assert currency.output == {
        "EUR": {
            "FR": {
                "Lyon": [
                    {
                    "amount": 11.4
                    }
                ],
                "Paris": [
                    {
                    "amount": 20
                    }
                ]
            },
        },
    }


def test_add_two_currencies_for_same_country():
    currency = ParseJson([
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
    ], NEST)

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
    

def test_raise_error_for_duplicated_key():
    with pytest.raises(KeyError):
        currency = ParseJson([
            {
            "country": "UK",
            "city": "London",
            "currency": "GBP",
            "amount": 12.2
        },
        ], ['currency', 'city', 'city'])


def test_raise_error_for_key_not_found():
    with pytest.raises(KeyError):
        currency = ParseJson([
            {
            "country": "UK",
            "city": "London",
            "currency": "GBP",
            "amount": 12.2
        },
        ], ['currency', 'fabricio', 'city'])
