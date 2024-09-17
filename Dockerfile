# Base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get -y install \
        python3-dev \
        default-libmysqlclient-dev \
        pkg-config \
        build-essential && \
    rm -rf /var/lib/apt/lists/*


RUN  pip install django && \
     pip install -r requirements.txt


# Copy the project files to the working directory
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
