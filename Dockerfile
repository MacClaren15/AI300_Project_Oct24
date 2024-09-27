# Start with a python base image
# Take your pick from https://hub.docker.com/_/python
FROM python:3.11-slim

# Set /flask-app as the main application directory
WORKDIR /AUG24-P09

# Copy the requirements.txt file and required directories into docker image
COPY ./requirements.txt /AUG24-P09/requirements.txt
COPY ./src /AUG24-P09/src
COPY ./model /AUG24-P09/model

# Add /src directory to PYTHONPATH, so that model.py Python module can be found
# To add multiple directories, delimit with colon e.g. /flask-app/src:/flask-app
ENV PYTHONPATH /AUG24-P09/src

# Install python package dependancies, without saving downloaded packages locally
RUN pip install -r /AUG24-P09/requirements.txt --no-cache-dir

# Allow port 80 to be accessed (Flask app)
EXPOSE 80

# Start the Flask app using gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:80", "src.app:app"]