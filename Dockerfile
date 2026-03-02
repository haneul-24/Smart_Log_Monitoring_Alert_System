
FROM python:3.12.3-slim 

WORKDIR /myapp

RUN apt-get update && apt-get install -y ca-certificates &&  rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt 

COPY src/ /myapp/src/

COPY tests/ /myapp/tests/

ENV PYTHONPATH=/myapp

RUN mkdir -p target/surefire-reports

# CMD ["pytest", "--junitxml=myapp/target/surefire-reports/results.xml"]








