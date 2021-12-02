# guess.py

A web application where you guess at pictures.

## Setup

Clone the repo and run the following in the base directory (assuming your
web server runs under the `www-data` user):

```sh
mkdir answers static/pictures
sudo chgrp www-data answers static/pictures
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
deactivate
```

You will also need to configure your web server to serve the app. An 
apache example server config is provided, it requires `mod_wsgi`.
 
## Design
 
The application is built around a json-based REST API called via ajax.
`static/index.html` loads `static/script.js`, which calls the python 
application `guess.py` via XMLHttpRequest.

Uploads are accepted at `static/upload.html`. Uploaded files are stored 
in `static/pictures`, and corresponding answers are stored in `answers`.
