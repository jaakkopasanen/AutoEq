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
ORTRY = 'oratory1990'

# Root dir for measurments, manufacturers, and type sub-dirs
MEAS_ROOT = os.path.join(AEQ_ROOT, 'measurements')
ORTRY_MEAS_ROOT = os.path.join(MEAS_ROOT, ORTRY)
MNFCT_FILE_NAME = 'manufacturers.tsv'
MNFCT_FILE = os.path.join(MEAS_ROOT, 'manufacturers.tsv')

# Target types
HRMN_INEAR_2019V2 = 'harman_in-ear_2019v2'
HRMN_OVEAR_2018 = 'harman_over-ear_2018'

# Phone types
IN_EAR = 'inear'
OVER_EAR = 'overear'

# Results
RES_ROOT = os.path.join(AEQ_ROOT, 'results')
NAME_FILE_NAME = 'name_index.tsv'
ORTRY_RES_ROOT = os.path.join(RES_ROOT, ORTRY)
ORTRY_NAMES = os.path.join(ORTRY_MEAS_ROOT, NAME_FILE_NAME)
ORTRY_INEAR_RES_ROOT = os.path.join(ORTRY_RES_ROOT, HRMN_INEAR_2019V2)
ORTRY_OVEAR_RES_ROOT = os.path.join(ORTRY_RES_ROOT, HRMN_OVEAR_2018)
ORTRY_RES_BY_TYPE = {
    IN_EAR: ORTRY_INEAR_RES_ROOT,
    OVER_EAR: ORTRY_OVEAR_RES_ROOT
}
