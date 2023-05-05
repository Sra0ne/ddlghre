# ddlghre
simple webserver in written in Python to send direct download link to the latest release assets of a github repository

#Installation

1.Clone the repo 

2.`python3 -m venv venv`

3.`source venv/bin/activate`

4.`pip3 install -r requirements.txt`


5.`FLASK_APP=app.py flask run`
This will start the web server on the default port 5000. You can access the server in your web browser by navigating to http://localhost:5000/.

If you want to specify a different port, you can use the --port option, like this:



`FLASK_APP=app.py flask run --port=8000`
This will start the web server on port 8000.

Note that this command will only start the web server in the current terminal session. If you want to start the web server as a background process, you can use a tool like screen or systemd

This is a very rudimentary implementation,just to redirect to the latest assest.

#Usage 

To get the latest release,just append /account/repo to the request url like http://localhost:5000/account/repo

For example,to get the latest release of https://github.com/DJDoubleD/QobuzDownloaderX-MOD you go to the url http://localhost:5000/DJDoubleD/QobuzDownloaderX-MOD

#How It Works

This web server listens for incoming HTTP requests and extracts the GitHub repository URL from the request path. It then queries the GitHub API to get the latest release information for the repository, and extracts the download URL of the latest release asset with a .zip extension.

Finally, the web server redirects the incoming request to the extracted download URL using a 302 status code. If no ZIP assets are found for the given repository, the web server returns an error message.
This can't do many things,but works for my use case(for now)
