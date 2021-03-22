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
"""AutoEQ Web REST API."""
from flask import jsonify, current_app, send_from_directory

from .model import (
    get_filters,
    MANUFACTURERS,
    RESULTS
)

APP = current_app

@APP.route("/api/manufacturers/")
def manufacturers():
    """Get a complete list of headphone manufacturers."""
    return jsonify(manufacturers=MANUFACTURERS)

@APP.route("/api/results/<source>")
def results(source):
    """Get a complete list of results by source."""
    return jsonify(results=RESULTS[source])

@APP.route("/api/filters/<source>/<target>/<model>")
def filters(source, target, model):
    """Get a complete list of headphones."""
    send_dir, zip_name = get_filters(source, target, model)
    return send_from_directory(send_dir, zip_name)
