#!/bin/bash

pkill port-forward

kubectl delete service mailparse
kubectl delete deployment mailparse
