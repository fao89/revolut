Revolut Challenge
==========================
[![Build Status](https://api.travis-ci.com/fao89/revolut.svg?branch=master)](https://travis-ci.com/fao89/revolut)
![Revolut CI](https://github.com/fao89/revolut/workflows/Revolut%20CI/badge.svg)
[![codecov](https://codecov.io/gh/fao89/revolut/branch/master/graph/badge.svg)](https://codecov.io/gh/fao89/revolut)
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/download/releases/3.7.2/)


A Flask REST API for parsing json



Installation
------------

#### 1. Install Project

``` {.sourceCode .bash}
$ make install
$ make start_db
```


How to run the app locally
------------

To run the rest project locally do:
``` {.sourceCode .bash}
$ cd revolut/
$ make rest_run
```
The dev server will spin up and will be available at: http://127.0.0.1:5000/

For parse the json:
you can pass the parameters like this: `?nest=nesting1,nesting2` or `?nest=nesting1&nest=nesting2`
``` {.sourceCode .bash}
$ curl -u revolut:challenge2019 -vX POST http://localhost:5000/parse?nest=currency,country,city -d @example_input.json \
--header "Content-Type: application/json"
```

To run the cli project locally do:
``` {.sourceCode .bash}
$ python revolut/cli/nest.py --filename example_input.json currency country city
or
$ cat example_input.json | python revolut/cli/nest.py currency country city
```
