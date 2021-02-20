#!/bin/bash

. smoke.sh

echo
echo Service1 smokeTest
echo

smoke_url_ok "http://35.228.242.68"
    
smoke_report

. smoke.sh

echo 
echo
echo Service2 smokeTest
echo

smoke_url_ok "http://35.228.149.8:5000/"

    
smoke_report
