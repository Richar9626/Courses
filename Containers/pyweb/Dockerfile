#defining to run with latest python version available
FROM python:latest  

#making a directory and going to that directory for thebuild
RUN mkdir /build
WORKDIR /build
COPY . /build

#we ensure the installation of packages specified under requirements.txt
RUN pip install -r requirements.txt

#running the application
CMD ["python", "pyweb.py"]