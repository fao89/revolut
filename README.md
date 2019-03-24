Revolut Challenge
==========================

A Flask REST API for parsing json



Installation
------------

#### 1. Install Project

``` {.sourceCode .bash}
$ pip install -e "." 
```


How to run the app locally
------------

To run the rest project locally do:
``` {.sourceCode .bash}
$ cd revolut/
$ python app.py
```
The dev server will spin up and will be available at: http://127.0.0.1:5000/

For parse the json:
you have to add the arg `nest_` followed by the nesting levels, separating nesting levels with `__` like this: `nest_nesting1__nesting2`
``` {.sourceCode .bash}
$ curl -u admin:secret -vX POST http://localhost:5000/parse?nest_currency__country__city -d @input.json \
--header "Content-Type: application/json" 
```

To run the cli project locally do:
``` {.sourceCode .bash}
$ cd revolut/cli/
$ python nest.py --filename input.json currency country city
or
$ cat input.json | python nest.py currency country city
```
