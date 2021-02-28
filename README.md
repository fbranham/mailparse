# mailparse
Code Exercise

This is a code / config exercise for an interview. It parses emails sent to either the baseurl or /post, and returns a set of SMTP headers in json. 

This sets up a python flask app, wraps it in an alpine/nginx container, and deploys it to a local K8 installation

## Quickstart

This was done on a Macbook Pro using xcode python3, and the native Docker kubernetes support. 

### Requirements

* python3
* Docker engine
* a k8 cluster (Docker needs to be configured to push to the k8 Docker repo)

### Helper scripts

```
bash doit.sh 
```
This builds the docker image from a Dockerfile, creates the deployment and service, and starts local port forwarding with the service on localport 8080. At least on my kubernetes, the port forwarding command did not like running in the background. 

```
bash test.sh
```
This simply curls the contents of the emails to port 8080.

```
bash clean.sh
```
Cleans up the service and deployment

## Directories

* /docker contains the Dockerfile, an nginx.conf default, and some scripts to set up uwsgi support. The starter kit here is https://github.com/jazzdd86/alpine-flask. I tweaked it a bit, mostly to copy in the flask app instead of using a volume. 
* /docker/mailparse has the Flask app. 
* /docker/mailparse/tests has a test.sh script which will fire up a local flask server and curl in the sample emails. 

## Notes
The tricky part was getting nginx and the Flask app working. Docs on exactly how Flask presents a python module are just a bit scarce. I did choose to use Alpine before finding the alpine-flask, and decided to just use nginx instead of Flask's native server after seeing it. 

I pulled minikube from brew, and got my local Docker to use kube as a registry before noticing the new Docker k8 support. 
