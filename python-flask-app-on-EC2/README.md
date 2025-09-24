Python Flask App CI/CD with AWS

Project Overview

This project demonstrates how to set up a complete CI/CD pipeline for a simple Python Flask application using:
1.	GitHub (source code management)
2.	AWS CodePipeline (orchestration)
3.	AWS CodeBuild (build and Docker image creation)
4.	AWS CodeDeploy (deployment to EC2)
5.	Amazon EC2 (hosting the application in a Docker container)
Every code push to GitHub automatically triggers the pipeline → builds → deploys to EC2.
 <img width="743" height="400" alt="image" src="https://github.com/user-attachments/assets/456e8aee-8727-4fa1-bf62-a3466f090ce0" />

Project Structure

<img width="562" height="352" alt="image" src="https://github.com/user-attachments/assets/af685b9a-cf11-42f5-ad57-9fdbbcbecc85" />


IAM Roles
The following IAM roles were created for secure access control:
1. codepipeline-python-flask-app-on-ec2
   - Used by AWS CodePipeline.
   - Allows pipeline orchestration and triggering CodeBuild/CodeDeploy.
 <img width="940" height="275" alt="image" src="https://github.com/user-attachments/assets/d2d33db3-824e-4262-9422-5515a089584f" />
 <img width="940" height="291" alt="image" src="https://github.com/user-attachments/assets/5291a9d8-1612-432f-ac85-0115a7b5156b" />

2. codebuild-python-flask-app-on-ec2
   - Used by AWS CodeBuild.
   - Grants permissions for S3 (artifacts), ECR/Docker registry (push images), and CloudWatch logs.
 <img width="940" height="274" alt="image" src="https://github.com/user-attachments/assets/5ddb110c-2944-41e3-822f-0e6050f454da" />
 <img width="940" height="259" alt="image" src="https://github.com/user-attachments/assets/2205bc46-3e57-44be-90ae-f8fc257065ef" />

3. codedeploy-python-flask-app-on-ec2
   - Used by AWS CodeDeploy and attached to the EC2 instance.
   - Allows deployment agent on EC2 to fetch artifacts and execute lifecycle hooks.
 <img width="940" height="339" alt="image" src="https://github.com/user-attachments/assets/02f6968c-f230-484e-b3f4-7905ccd6e282" />
 <img width="940" height="258" alt="image" src="https://github.com/user-attachments/assets/08dfd0bb-15bf-48c4-8f6b-6c9c060f9567" />

CI/CD Workflow
1. Source Stage (CodePipeline)
   - GitHub repo is configured as the source.
   - Any push to the main branch triggers the pipeline.
2. Build Stage (CodeBuild)
   - Installs dependencies from `requirements.txt`.
   - Builds a Docker image using `Dockerfile`.
   - Pushes the Docker image to the container registry.
   - Generates build artifacts for deployment.
3. Deploy Stage (CodeDeploy)
   - Downloads build artifacts.
   - Uses `appspec.yml` to run lifecycle hooks.
   - Stops old container (`stop_container.sh`).
   - Starts new container with the updated application (`start_container.sh`).
<img width="940" height="252" alt="image" src="https://github.com/user-attachments/assets/37072ed1-268d-4ebe-9a18-11b16f27d6d1" />
