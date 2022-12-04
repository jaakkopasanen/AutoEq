#FROM nikolaik/python-nodejs:python3.9-nodejs16
FROM ubuntu:22.04
RUN apt update
RUN apt install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt update
RUN apt install -y nodejs
RUN apt -y install libsndfile1 python3 python3-dev python3-pip python3-venv
WORKDIR /autoeq
COPY . .
RUN python3 -m pip install -U pip
RUN python3 -m pip install -U -r requirements.txt
RUN python3 -m pip install -U autoeq
WORKDIR /autoeq/ui
RUN npm ci
RUN npm run build
RUN rm -fr public/ src/ node_modules/ package.json package-lock.json
WORKDIR /autoeq
ENV NODE_ENV production
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
#CMD ["python", "-m" "uvicorn", "main:app"]
