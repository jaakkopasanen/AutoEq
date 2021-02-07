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
"""Configuration for AutoEQ Flask app."""
import os
import tempfile

from autoeq_srv.const import ConfKey

# Template these values for flexible install
HOST = 'localhost'
TEMP = tempfile.gettempdir()

# pylint: disable=R0903
class BaseConfig:
    """Base / default config, no debug logging and short log format."""
    DEBUG = False
    HOST = HOST
    AEQ_PORT = int(os.environ.get(ConfKey.AEQ_PORT, 5000))
    LOG_FILE = os.path.join(TEMP, 'autoeq-web.log')
    LOG_FORMAT = '[%(filename)-15s:%(lineno)-5d] %(message)s'
    SECRET_KEY = '3175b8e3f55408f2f14259f0'

# pylint: disable=R0903
class DevConfig(BaseConfig):
    """Developer level config, with debug logging and long log format."""
    DEBUG = True
    LOG_FORMAT = '[%(asctime)s %(levelname)-8s %(filename)-15s:%(lineno)-5d ' +\
                 '%(funcName)-30s] %(message)s'

CONFIGS = {
    "dev": 'autoeq_srv.config.DevConfig',
    "default": 'autoeq_srv.config.BaseConfig'
}

def configure_app(app):
    """Grab the environment variable for app config or defaults to dev."""
    config_name = os.getenv(ConfKey.AEQ_CONF_NAME, 'default')
    app.config.from_object(CONFIGS[config_name])
