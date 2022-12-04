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
```shell
cd webapp
docker build -t yourusername/autoeq:latest
docker push yourusername/autoeq:latest
```