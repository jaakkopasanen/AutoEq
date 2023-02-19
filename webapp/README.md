# WebApp
WebApp for AutoEq

## Development
Install dependencies
```shell
cd webapp
python -m pip install -U -r requirements.txt
```

Run backend
```shell
uvicorn main:app --reload
```

Run frontend dev server
```shell
cd ui
npm i
npm start
```

Go to `http://localhost:3000`

## Build Docker File
Needs to be done from root directory, not from webapp
```shell
docker build -t yourusername/autoeq:latest .
docker push yourusername/autoeq:latest
```

## Run Docker
Data directory needs to be created and mounted. `webapp/create_data.py` creates the directory and necessary files by
packaging compensation curves and measurements. You need all measurement data available in the `measurements` directory
to do this.

The `data/audio` directory also needs to have all the songs for the player. It's recommended to normalize the volumes across all
your tracks. https://www.loudnesspenalty.com/ helps calculating the required amplification. Use Spotify levels.

Privacy policy (`privacy-policy.html`) and Terms of Service (`terms-of-service.html`) should be placed in `data/legal`.

```shell
data/
  audio/
    Jennifer Warnes - Bird On a Wire.ogg
  legal/
    privacy-policy.html
    terms-of-service.html
  compensations.json
  entries.json
  measurements.json
```

```shell
docker run -d -p 8000:8000 -v /path/to/AutoEq/webapp/data:/app/webapp/data yourusername/autoeq:latest
```