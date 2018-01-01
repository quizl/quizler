[![Build Status](https://travis-ci.org/quizl/quizler.svg?branch=master)](https://travis-ci.org/quizl/quizler)
[![Coverage Status](https://codecov.io/gh/quizl/quizler/branch/master/graph/badge.svg)](https://codecov.io/gh/quizl/quizler)

# quizler

Collection of utils for Quizlet flash cards

## Installation

```bash
$ pip install quizler
```

Tested on:

- macOS / Python 3.6.1
- Ubuntu 14.04 / Python 3.5.3

## Usage

### Command-line interface

On the command-line Quizler can be used to access public information read-only:

```bash
$ export USER_ID=john
$ export CLIENT_ID=Ab0Cd1Ef2G
$ quizler sets --terms
Found sets: 2
    German
        Hello = Hallo
        How are you? = Wie geht's?
    French
        Hello = Bonjour
        How are you? = Comment ça va?
```

- `USER_ID` - Quizlet username whose information you want to access (your own username can be viewed
  right at your avatar in the top right corner on quizlet.com)
- `CLIENT_ID` - Quizlet Client ID which can be obtained on the
  [Quizlet API dashboard](https://quizlet.com/api-dashboard)

### Python library

As a Python library Quizler can also access private information:

```
>>> from quizler.utils import reset_term_stats
>>> reset_term_stats(set_id=123456789, term_id=1234567890, client_id='Ab0Cd1Ef2G', user_id='john', access_token='46a54395f3d1108feca56c7f6ca8dd3d')
Deleting "Hello = Hallo"...
Re-creating "Hello = Hallo"...
Done
```

The access token can be obtained by a web app implementing
[Quizlet's authentication flow](https://quizlet.com/api/2.0/docs/authorization-code-flow).
[Here is an example](https://github.com/quizl/backend).

<a href="https://quizlet.com/"><img src="https://quizlet.com/static/ThisUsesQuizlet-White.png" alt="Powered by Quizlet" align="right"/></a>
