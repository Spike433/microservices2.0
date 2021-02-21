# microservices2.0

### Software used

- minikube for local testing

- docker

- CD/CI --> Github Actions

- kubernetas deployment --> Google Kubernetes Engine (GKE) 

### How it works

- On **push **/**pull**/**commit** to this repository /.github/workflows/**CD-CI.yml** gets triggered 


![Alt text](/images/Screenshot_1.png?raw=true "Optional Title") 
 
  - _service1_ and _service2 _ folders are built and sent to DockerHub \
         1. https://hub.docker.com/repository/docker/spike433/service1 \
         2. https://hub.docker.com/repository/docker/spike433/service2 \
         3. kepp in mind that service1:**2.0** gets newest updates, service: **2.6** as well, dockerHub allows to overwrite current tag with same tag


- Add artifacts to publish  ("Run" Unit Test, Integration Test)  

- Login to Kubernetas Engine

- Build yaml files that pull latest images from dockerHub  


![Alt text](/images/Screenshot_2.png?raw=true "Optional Title") 


- Run Smoke Test ( https://github.com/asm89/smoke.sh ) and save to artifact

- Automated versioning of service/solution artifacts

![Alt text](/images/Screenshot_3.png?raw=true "Optional Title")

- Exposed ports of services 
   
   -http://35.228.242.68      (service1 can't display its data because of watchdog that handles it in background)\
   -http://35.228.149.8:5000  (service2 - not sure how stdin should work (via url, arguments ...) so it is ignored)


