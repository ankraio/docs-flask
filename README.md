# API Microservice
Welcome to our Git repository, where we provide insights into the deployment flow configuration of a .ankra.yaml file. At Ankra, we understand that deploying applications into the cloud native ecosystem can be a daunting task. That's why we've created a tool that simplifies the process and ensures a smooth and efficient deployment.

Ankra is the place where you can add your application, and it will automatically pick up the .ankra.yaml file, which contains the configuration for the continuous integration and continuous deployment (CICD) flow. With this file, you can define the different stages of the deployment process, including build, test, and deployment to the cloud environment.

In this repository, we aim to provide insights into how the .ankra.yaml file works and how you can use it to configure your CICD flow for your application. We will also provide examples of how to use the file and integrate it with your cloud environment to ensure a seamless deployment process.

Thank you for choosing Ankra, and we hope that our repository will help you deploy your applications with ease and efficiency.

## What is the `.ankra.yaml` file?

The `.ankra.yaml` file is used for configuring the deployment of a cloud-native application. It defines the CICD flow in stages such as **build**, **predeploy**, and **development**. The file sets environment variables and secrets used during deployment, and contains scripts and actions executed at different stages, such as building Docker images and upgrading Helm charts. Here's a quick breakdown:

- **stages**: Defines the different stages of the deployment flow, such as building, predeploy, and development, and lists the actions to be taken in each stage.
- **variables**: Sets environment variables and secrets used during deployment, such as the version number, target environment, and registry credentials.
- **predeploy**: Contains actions to be executed before deployment, such as creating namespaces and setting up credentials for Cloudflare and Docker registry.
- **build**: Contains actions for building Docker images and creating Helm charts.
- **tag_cleanup**: Deletes old tags and pushes the new ones to the Git repository.
- **dev**: Contains actions for deploying the application, including upgrading Helm charts and setting environment variables.

read more: https://ankra.gitbook.io/docs-flask/ankra-yaml-file

