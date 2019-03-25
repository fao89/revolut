Revolut Challenge
==========================

A Flask REST API for parsing json



Installation
------------

#### 1. Install Project

``` {.sourceCode .bash}
$ make install
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
you have to add the arg `nest_` followed by the nesting levels, separating nesting levels with `__` like this: `nest_nesting1__nesting2`
``` {.sourceCode .bash}
$ curl -u revolut:challenge2019 -vX POST http://localhost:5000/parse?nest_currency__country__city -d @example_input.json \
--header "Content-Type: application/json" 
```

To run the cli project locally do:
``` {.sourceCode .bash}
$ python revolut/cli/nest.py --filename example_input.json currency country city
or
$ cat example_input.json | python revolut/cli/nest.py currency country city
```
