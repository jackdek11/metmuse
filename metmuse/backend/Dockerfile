# Build from Python 3.10
FROM python:3.10-alpine

# Set working directory to /code/
WORKDIR /code

ENV PATH /home/root/.local/bin:${PATH}

# Install requirements
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy over chrome_manager and logging config
COPY backend/ /code/backend/
COPY images/ /code/images/
COPY fixtures.json /code/fixtures.json
COPY manage.py /code/manage.py
COPY startup.sh /code

RUN chmod +x startup.sh

# Entrypoint to container
CMD ["./startup.sh"]