# guess.py

A web application where you guess at pictures.

## Setup

```sh
mkdir answers static/pictures
sudo chgrp www-data answers static/pictures
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
deactivate
```

The above assumes that your web server runs under the user `www-data`.

You will also need to configure your web server. An apache example server 
config is provided, it requires `mod_wsgi`.
 
## Design
 
The application is built around a json-based REST API called via ajax.
`static/index.html` loads `static/script.js`, which calls the python 
application `guess.py` via XMLHttpRequest.

Uploads are accepted at `static/upload.html`. Uploaded files are stored 
in `static/pictures`, and corresponding answers are stored in `answers`.
