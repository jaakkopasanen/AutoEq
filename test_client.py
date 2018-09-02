import requests
from time import time
from frequency_response import FrequencyResponse

fr = FrequencyResponse.read_from_csv('innerfidelity/data/onear/AKG K450/AKG K450.csv')
comp = FrequencyResponse.read_from_csv('headphonecom/data/onear/Sennheiser HD 600/Sennheiser HD 600.csv')
calib = FrequencyResponse.read_from_csv('calibration/innerfidelity_to_headphonecom.csv')

t = time()
res = requests.post('http://127.0.0.1:8080/process', json={
    'frequency': fr.frequency.tolist(),
    'raw': fr.raw.tolist(),
    'compensation': comp.raw.tolist(),
    #'compensation': 'innerfidelity_sbaf-serious',
    'calibration': calib.raw.tolist(),
    'equalize': True,
    'parametric_eq': False,
    'max_filters': [5, 5],
    'bass_boost': 4,
    'tilt': 0.3,
    #'iem_bass_boost': 4,
    'treble_gain_k': 0.0
})
print('Request took {:.2f}s'.format(time() - t))

if res.status_code != 200:
    print(res.status_code, res.text)
    exit()

print('{')
for key, value in res.json().items():
    print('    {k}: {v}'.format(k=key, v=value))
print('}')
