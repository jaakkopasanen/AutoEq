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
from flask import current_app

# Root directory for measurement/result data, currently the GitHub checkout root
AEQ_ROOT = aeq_root = current_app.config['AEQ_ROOT']

# Measurement types
README = 'README.md'

# Root dir for measurments, manufacturers, and type sub-dirs
MEAS_ROOT = os.path.join(AEQ_ROOT, 'measurements')

MNFCT_FILE_NAME = 'manufacturers.tsv'
NAME_FILE_NAME = 'name_index.tsv'
MNFCT_FILE = os.path.join(MEAS_ROOT, 'manufacturers.tsv')

# Targets
HRMN_INEAR_2019V2 = 'harman_in-ear_2019v2'
HRMN_OVEAR_2018 = 'harman_over-ear_2018'

# Target types
IN_EAR = 'in-ear'
OVER_EAR = 'over-ear'

# Results
RES_ROOT = os.path.join(AEQ_ROOT, 'results')
REC_RESULTS = os.path.join(RES_ROOT, README)
ALL_RESULTS = os.path.join(RES_ROOT, 'INDEX.md')


REC_SRC = {
    'name': 'Recommended',
    'title': 'Recommended results.',
    'description': """
    The recommended filters for your headphonesRecommendation priority is:
    oratory1990 > Crinacle > Innerfidelity > Rtings > Headphone.com > Reference Audio Analyzer.
    This means if there are measurements from multiple sources for the same headphone
    model only the highest priority result will be shown in this list."""
}

SOURCES = {
    'oratory1990': {
        'name': 'Oratory',
        'title': 'All Oratory results.',
    },
    'crinacle': {
        'name': 'Crinacle',
        'title': 'All Crinacle results.'
    },
    'innerfidelity': {
        'name': 'Inner Fidelity',
        'title': 'All Inner Fidelity results.'
    },
    'rtings': {
        'name': 'Rtings',
        'title': 'All Rtings results.'
    },
    'headphonecom': {
        'name': 'Headphones.com',
        'title': 'All Headphones.com results.'
    },
    'referenceaudioanalyzer': {
        'name': 'RAA',
        'title': 'All Reference Audio Analyzer results.'
    }
}

PHONE_TYPE_DETAILS = {
    IN_EAR: {
        'code': IN_EAR,
        'name': 'In Ear',
        'icon': 'inear.png',
        'alt': 'Created by Vectors Point for Noun project.'
    },
    OVER_EAR: {
        'code': OVER_EAR,
        'name': 'Over Ear',
        'icon': 'overear.png',
        'alt': 'Icon for over ear headphones'
    }
}
