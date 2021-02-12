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
"""Code for the headphone data model."""
import os
from zipfile import ZipFile
from urllib.parse import unquote

from flask import current_app

from autoeq_srv.routes.const import (
    MNFCT_FILE,
    ORTRY_NAMES,
    ORTRY_RES_BY_TYPE,
    OVER_EAR, IN_EAR,
    PHONE_TYPE_DETAILS
)

APP = current_app

def _manufacturers_with_variants():
    """Return the raw manufacturers data including variants."""
    with open(MNFCT_FILE,
              encoding='utf-8') as _fh:
        raw_manufacturers = _fh.read().strip().split('\n')
        manufacturers = [m.strip().split('\t') for m in raw_manufacturers]
    return manufacturers

RAW_MANUFACTURERS = _manufacturers_with_variants()

def get_manufacturers():
    """Return the manufacturers list."""
    manufacturers = []
    for manufacturer in RAW_MANUFACTURERS:
        manufacturers.append(manufacturer[0])
    return manufacturers

def resolve_manufacturer(name):
    """Return a canonical name and variant tuple."""
    for manufacturer in RAW_MANUFACTURERS:
        if name in manufacturer:
            return manufacturer[0], name
    return None

def get_oratory_phones():
    """Return the list of headphones with Oratory measurements."""
    phones = []
    with open(ORTRY_NAMES,
              encoding='utf-8') as _fh:
        raw_names = _fh.read().strip().split('\n')
        phone_parts = [m.strip().split('\t') for m in raw_names]
    for phone in phone_parts:
        if phone[0] == 'false_name':
            continue
        phones.append({ 'key': phone[1], 'name': phone[0], 'type': phone[2] })
    return phones

def get_oratory_results():
    """Return the list of headphones with Oratory results."""
    phones = []
    for phone_type in [IN_EAR, OVER_EAR]:
        phones.extend(get_phone_results(ORTRY_RES_BY_TYPE[phone_type],
                                        phone_type))
    return phones

def get_phone_results(to_scan, phone_type):
    """Return a list of phone directories."""
    phones = []
    for phone_dir in [ name for name in os.listdir(to_scan) \
                       if os.path.isdir(os.path.join(to_scan, name)) ]:
        phones.append({
                'name': phone_dir,
                'type': PHONE_TYPE_DETAILS[phone_type]
                })
    return phones

def get_oratory_filters(phone_type, name):
    """Return the zipped convolution filters for oratory results."""
    phone_name = unquote(name)
    phone_path = os.path.join(ORTRY_RES_BY_TYPE[phone_type],
                              phone_name)
    if not os.path.isdir(phone_path):
        return None
    zip_name = '{}_harman_results.zip'.format(phone_name)
    zip_path = os.path.join(phone_path, zip_name)
    if not os.path.isfile(zip_path):
        with ZipFile(zip_path, 'w') as reszip:
            filter_name =  '{} minimum phase 44100Hz.wav'.format(phone_name)
            reszip.write(os.path.join(phone_path, filter_name), arcname=filter_name)
            filter_name =  '{} minimum phase 48000Hz.wav'.format(phone_name)
            reszip.write(os.path.join(phone_path, filter_name), arcname=filter_name)
    return phone_path, zip_name
