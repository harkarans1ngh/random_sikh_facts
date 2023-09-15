# random_sikh_facts
This is an API built in Django using the django-drf package that provides one random fact a day related to Sikhism, the fifth-largest religion in the world. 

## Usage and Deployment
This repo utilises docker and docker-compose to make it work across all platforms. However, appspec files are also included for Continous Deployment of the Webapp to AWS via CodeDeploy. 

To run this locally,

`git clone https://github.com/pr0grmr/random_sikh_facts`

Provide an env.dev file at random_sikh_facts/env/ and then run

`docker-compose -f docker_compose_local.yml up -d`

To run this in production, provide .env.prod and .env.prod.db at random_sikh_facts/env/
If deploying using CodeDeploy, add the .env.prod and .env.prod.db in AWS SSM Parameter Store and make sure that the deployment host has access to it.  

