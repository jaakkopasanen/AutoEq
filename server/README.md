# AutoEQ Server
This is a light flask app to make finding and serving the settings and filters
a little more user friendly. To do this the app:
- puts all headphones on a single web page with optimal download options;
- a more detailed per-headphone page that displays the GitHub info; and
- offers a convenient "filters in a zip file" suitable for upload to Roon software.

# Usage
Super brief at the moment,
- Use a python 3.6+ virtualenv
- go to the `./server` directory
- define the Flask app env var `export FLASK_APP='autoeq_srv'`
- issue command `flask run`
- browse to <http://localhost:5000>
