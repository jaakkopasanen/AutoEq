FROM ubuntu:22.04
RUN apt update
RUN apt install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt update
RUN apt install -y nodejs
RUN apt -y install nodejs libsndfile1 python3 python3-dev python3-pip python3-venv
WORKDIR /app
COPY ./autoeq/*.py ./autoeq/
COPY ./webapp/ui/package.json ./webapp/ui/package.json
COPY ./webapp/ui/package-lock.json ./webapp/ui/package-lock.json
COPY ./webapp/ui/public ./webapp/ui/public
COPY ./webapp/ui/src ./webapp/ui/src
COPY ./webapp/main.py ./webapp/main.py
COPY ./webapp/requirements.txt ./webapp/requirements.txt
COPY ./pyproject.toml ./pyproject.toml
COPY ./README.md ./README.md
#RUN ls -lR /app
#RUN python3 -m venv venv
#RUN . venv/bin/activate
RUN python3 -m pip install -U pip
RUN python3 -m pip install -U .
WORKDIR /app/webapp
RUN python3 -m pip install -U -r ./requirements.txt
WORKDIR /app/webapp/ui
RUN npm ci
RUN npm run build
WORKDIR /app/webapp
ENV APP_ENV=production
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
#CMD ["python3", "-m" "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
#CMD ["/opt/venv/python", "-m" "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["python3", "-m", "autoeq", "--help"]
#CMD ["/opt/venv/python", "--version"]
