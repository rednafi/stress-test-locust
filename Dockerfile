# Use the latest locust image
FROM python:3.9.7-slim-bullseye

# Set working directory
WORKDIR /code

# This is where the modules get installed so it's a good
# idea to add that to the $PATH
ENV PATH /home/locust/.local/bin:$PATH

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code

EXPOSE 8089 5557

RUN useradd --create-home locust
USER locust
WORKDIR /home/locust

# Turn off python output buffering.
ENV PYTHONUNBUFFERED=1
