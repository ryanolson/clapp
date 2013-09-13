clapp
=====

## Install

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
python setup develop
samplectl runserver
```
