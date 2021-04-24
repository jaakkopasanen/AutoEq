#!/usr/bin/python
# coding=UTF-8
#
# Auto EQ Server
#
# Copyright © 2021 Carl Wilson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""AutoEQ Headphone app pages."""
import os
from flask import render_template, current_app, send_from_directory

from .model import RECOMMENDED, RESULTS
from .const import SOURCES, REC_SRC

FAVICO_DIR = os.path.join(current_app.root_path, 'static', 'favicon')

@current_app.context_processor
def inject_stage_and_region():
    """Inject a global for sources."""
    return dict(sources=SOURCES)

@current_app.route("/")
def home():
    """Application home page."""
    return render_template('results.html', source=REC_SRC, headphones=RECOMMENDED)

@current_app.route("/results/<source>")
def results_by_source(source):
    """Recommended filter sets according to preferences."""
    return render_template('results.html', source=SOURCES[source], headphones=RESULTS[source])

@current_app.route("/about/")
def about():
    """Application about page."""
    return render_template('about.html')

@current_app.route('/favicon.ico')
def favicon():
    """Serve the favicon."""
    return send_from_directory(FAVICO_DIR,
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@current_app.route('/favicon-16x16.png')
def favicon16():
    """Serve the favicon."""
    return send_from_directory(FAVICO_DIR,
                               'favicon-16x16.png', mimetype='image/png')

@current_app.route('/favicon-32x32.png')
def favicon32():
    """Serve the favicon."""
    return send_from_directory(FAVICO_DIR,
                               'favicon-32x32.png', mimetype='image/png')

@current_app.route('/apple-touch-icon.png')
def faviconapple():
    """Serve the favicon."""
    return send_from_directory(FAVICO_DIR,
                               'apple-touch-icon.png', mimetype='image/png')

@current_app.route('/android-chrome-192x192.png')
def favicon192():
    """Serve the favicon."""
    return send_from_directory(FAVICO_DIR,
                               'android-chrome-192x192.png', mimetype='image/png')

@current_app.route('/android-chrome-512x512.png')
def favicon512():
    """Serve the favicon."""
    return send_from_directory(FAVICO_DIR,
                               'android-chrome-512x512.png', mimetype='image/png')

@current_app.route('/site-webmanifest')
def webmanifest():
    """Serve the favicon."""
    return send_from_directory(FAVICO_DIR,
                               'site-webmanifest', mimetype='application/manifest+json')
