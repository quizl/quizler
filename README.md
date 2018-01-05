[![Requirements Status](https://requires.io/github/lancelote/quizler/requirements.svg?branch=master)](https://requires.io/github/lancelote/quizler/requirements/?branch=master)
[![Build Status](https://travis-ci.org/quizl/quizler.svg?branch=master)](https://travis-ci.org/quizl/quizler)
[![Coverage Status](https://codecov.io/gh/quizl/quizler/branch/master/graph/badge.svg)](https://codecov.io/gh/quizl/quizler)

# quizler

Collection of utils for Quizlet flash cards

## Requirements

Tested on:

- macOS / Python 3.6.1
- Ubuntu 14.04 / Python 3.5.3

To install Python requirements (virtualenv is recommended):

```bash
pip install -r requirements.txt
```

## Usage

Quizler relies onto environment variables to operate. Currently there're two:

- `USER_ID` - your username on quizlet, it can be viewed right at your avatar in the top right on quizlet.com
- `CLIENT_ID` - Quizlet Client ID can be obtained in [Quizlet API dashboard](https://quizlet.com/api-dashboard)

Set this two before using the script. To work with quizler just invoke CLI, e.g.:

```bash
python main.py common
```

<a href="https://quizlet.com/"><img src="https://quizlet.com/static/ThisUsesQuizlet-White.png" alt="Powered by Quizlet" align="right"/></a>
