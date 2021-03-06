# microservices2.0 Part-two

### Software used

- minikube for local testing

- docker

- CD/CI --> [Github Actions](https://github.com/features/actions)

- kubernetas deployment --> [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)

### How it works

- On **push **/**pull**/**commit**  (.github/workflows/**CD-CI.yml**) gets triggered 


![Alt text](/images/Screenshot_1.png?raw=true "Optional Title") 
 
  - [_service1_](https://hub.docker.com/repository/docker/spike433/service1) and [_service2_](https://hub.docker.com/repository/docker/spike433/service2) folders are built and sent to DockerHub \
         - kepp in mind that service1:**2.0** gets newest updates, service: **2.6** as well, dockerHub allows to overwrite current tag with same tag


- Add artifacts to publish  ("Run" Unit Test, Integration Test)  

- Login to Kubernetas Engine

- Build yaml files in repository and pull latest images from dockerHub  


![Alt text](/images/Screenshot_2.png?raw=true "Optional Title") 


- Run Smoke Test ( https://github.com/asm89/smoke.sh ) and save to artifact

- Automated versioning of service/solution artifacts

![Alt text](/images/Screenshot_3.png?raw=true "Optional Title")

- Exposed ports of services 
   
   -http://35.228.242.68      (service1 can't display its data because of watchdog that handles it in background)\
   -http://35.228.149.8:5000  (service2 - not sure how stdin should work (via url, arguments ...) so it is ignored)

### Questions about tasks that are left

1. Where should be deployed Production, deploying it to same k8 cluster doesn't make sense, making another cluster and deploying there also doesn't seem right.

![Alt text](/images/Screenshot_4.png?raw=true "Optional Title")

2. Confused about 2 projects, where? how it looks like? what it contains? more info!

![Alt text](/images/Screenshot_5.png?raw=true "Optional Title")

3. [Rollback](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/rollback )  is not implemented but it could be realised with POST https://container.googleapis.com/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}:rollback request

   








