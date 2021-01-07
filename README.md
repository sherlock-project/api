<img align="right" src="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png"/>

# Sherlock API

[![Python Ver.](https://img.shields.io/badge/python-%3E=_3.6-green.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Api for sherlock module.

## Prerequisites

This REST API is built on top of [Django REST Framework](https://www.django-rest-framework.org/)
(known as DRF). You would need at least the fundamental knowledge about DRF in
order to do development to this project.

### Installation

```sh
# clone the repo
$ git clone https://github.com/sherlock-project/api.git

# change the working directory to api
$ cd api

# install the requirements
$ python3 -m pip install -r requirements.txt
```

*P.S. Please use `python` instead of `python3` if you are on Windows system*

### Run API Server

```sh
# propagate modules
$ python3 manage.py migrate

# in the root of project diretory..
$ python3 manage.py runserver 0.0.0.0:8000
```

Start you browser and type [127.0.0.1:8000](http://127.0.0.1:8000/) in as
your target URL and hit return.

Now you should able to test your Sherlock API through DRF browser interface!

## License

MIT © Sherlock Project

Original Creator - [Shen, Jen-Chieh](https://github.com/jcs090218)
