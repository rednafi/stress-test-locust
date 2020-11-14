# Use the latest locust image
FROM locustio/locust

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
