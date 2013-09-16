clapp
=====

## Install

### Requirements

clapp requires the following components to be installed on your server:
* couchdb

### Setup

from a checked out version of clapp

create or use a virtualenv.
```
mkvirtualenv clapp
```

```
workon clapp
```

then install clapp, clappsample and dependencies

```
./setup develop
pip uninstall pytz
pip install --pre pytz
cd sample
python setup.py develop
samplectl runserver
```
