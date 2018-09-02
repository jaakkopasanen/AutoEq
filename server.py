# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, Response
import gevent.pywsgi
import traceback
from frequency_response import FrequencyResponse

app = Flask(__name__)
compensations = {
    'innerfidelity_2016': FrequencyResponse.read_from_csv('innerfidelity/resources/innerfidelity_compensation_2016.csv'),
    'innerfidelity_2017': FrequencyResponse.read_from_csv('innerfidelity/resources/innerfidelity_compensation_2017.csv'),
    'innerfidelity_sbaf-serious': FrequencyResponse.read_from_csv('innerfidelity/resources/innerfidelity_compensation_sbaf-serious.csv'),
    'headphonecom': FrequencyResponse.read_from_csv('headphonecom/resources/headphonecom_compensation.csv'),
    'headphonecom_sbaf-serious': FrequencyResponse.read_from_csv('headphonecom/resources/headphonecom_compensation_sbaf-serious.csv'),
    'harman_in-ear_2016': FrequencyResponse.read_from_csv('compensation/harman_in-ear_2016.csv'),
    'harman_in-ear_2017-1': FrequencyResponse.read_from_csv('compensation/harman_in-ear_2017-1.csv'),
    'harman_in-ear_2017-2': FrequencyResponse.read_from_csv('compensation/harman_in-ear_2017-2.csv'),
    'harman_over-ear_2013': FrequencyResponse.read_from_csv('compensation/harman_over-ear_2013.csv'),
    'harman_over-ear_2015': FrequencyResponse.read_from_csv('compensation/harman_over-ear_2015.csv'),
    'harman_over-ear_2018': FrequencyResponse.read_from_csv('compensation/harman_over-ear_2018.csv'),
    'harman_in-ear_2016_wo_bass': FrequencyResponse.read_from_csv('compensation/harman_in-ear_2016_wo_bass.csv'),
    'harman_in-ear_2017-1_wo_bass': FrequencyResponse.read_from_csv('compensation/harman_in-ear_2017-1_wo_bass.csv'),
    'harman_in-ear_2017-2_wo_bass': FrequencyResponse.read_from_csv('compensation/harman_in-ear_2017-2_wo_bass.csv'),
    'harman_over-ear_2013_wo_bass': FrequencyResponse.read_from_csv('compensation/harman_over-ear_2013_wo_bass.csv'),
    'harman_over-ear_2015_wo_bass': FrequencyResponse.read_from_csv('compensation/harman_over-ear_2015_wo_bass.csv'),
    'harman_over-ear_2018_wo_bass': FrequencyResponse.read_from_csv('compensation/harman_over-ear_2018_wo_bass.csv'),
    'loudspeaker_in-room_flat_2013': FrequencyResponse.read_from_csv('compensation/loudspeaker_in-room_flat_2013.csv'),
}
calibrations = {
    'headphonecom_to_innerfidelity': FrequencyResponse.read_from_csv('calibration/headphonecom_to_innerfidelity.csv'),
    'innerfidelity_to_headphonecom': FrequencyResponse.read_from_csv('calibration/innerfidelity_to_headphonecom.csv')
}


def bad_request(status, msg):
    response = Response(msg)
    response.status_code = status
    return response


@app.route('/process', methods=['POST'])
def process():
    # Get body
    try:
        body = request.get_json()
    except Exception as err:
        return bad_request(400, 'Body is missing from request or is not JSON.')

    if body is None:
        return bad_request(400, 'Body is missing from request or is not JSON.')
    if 'frequency' not in body:
        return bad_request(400, '"frequency" is missing from body.')
    if 'raw' not in body:
        return bad_request(400, '"raw" is missing from body.')

    frequency = body['frequency']
    raw = body['raw']
    if len(raw) != len(frequency):
        return bad_request(400, 'Raw data does not match frequency data.')

    # Get params from body
    params = dict()
    for key in ['calibration', 'compensation', 'equalize', 'parametric_eq', 'max_filters', 'bass_boost',
                'iem_bass_boost', 'tilt', 'max_gain', 'treble_f_lower', 'treble_f_upper', 'treble_max_gain',
                'treble_gain_k']:
        if key in body:
            params[key] = body[key]

    if 'compensation' in params:
        if type(params['compensation']) == str:
            # Get values by name
            if params['compensation'] not in compensations:
                return bad_request(400, 'Unrecognized compensation function.')
            params['compensation'] = compensations[params['compensation']]
            if len(frequency) != len(params['compensation']):
                params['compensation'] = FrequencyResponse(
                    name='compensation',
                    frequency=params['compensation'].frequency,
                    raw=params['compensation'].raw
                )
                params['compensation'].interpolate(frequency)
        else:
            # List, assume to have same frequency data as raw
            if len(frequency) != len(params['compensation']):
                params['compensation'].interpolate(frequency)
            params['compensation'] = FrequencyResponse(
                name='compensation',
                frequency=frequency,
                raw=params['compensation']
            )

    if 'calibration' in params:
        if type(params['calibration']) == str:
            # Get values by name
            if params['calibration'] not in calibrations:
                return bad_request(400, 'Unrecognized compensation function.')
            params['calibration'] = calibrations[params['calibration']]
            if len(frequency) != len(params['calibration']):
                params['calibration'] = FrequencyResponse(
                    name='calibration',
                    frequency=params['calibration'].frequency,
                    raw=params['calibration'].raw
                )
                params['calibration'].interpolate(frequency)
        else:
            # List, assume to have same frequency data as raw
            if len(frequency) != len(params['calibration']):
                params['calibration'].interpolate(frequency)
            params['calibration'] = FrequencyResponse(
                name='calibration',
                frequency=frequency,
                raw=params['calibration']
            )

    # Create frequency response and process
    try:
        fr = FrequencyResponse(name='fr', frequency=frequency, raw=raw)
        fr.process(**params)
    except Exception as err:
        return bad_request(str(err), 500)

    return jsonify(fr.to_dict())


def run():
    ws = gevent.pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    ws.serve_forever()
    #app.run('0.0.0.0', 8080)


if __name__ == '__main__':
    run()
