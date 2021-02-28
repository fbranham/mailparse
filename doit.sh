#!/bin/bash
cd "$(dirname "$0")"
kubectl create -f kube/mailparse.yaml
kubectl create -f kube/mpservice.yaml
sleep 10
kubectl port-forward deployment/mailparse 8080:80



