Python Flask App CI/CD with AWS

Project Overview

This project demonstrates how to set up a complete CI/CD pipeline for a simple Python Flask application using:
1.	GitHub (source code management)
2.	AWS CodePipeline (orchestration)
3.	AWS CodeBuild (build and Docker image creation)
4.	AWS CodeDeploy (deployment to EC2)
5.	Amazon EC2 (hosting the application in a Docker container)
Every code push to GitHub automatically triggers the pipeline → builds → deploys to EC2.
 
Project Structure
python-flask-app-on-ec2/
│   ├── app.py                 # Flask application code
│   ├── Dockerfile             # Docker image build instructions
│   ├── requirements.txt       # Python dependencies
│
scripts/
│   ├── start_container.sh     # Script to start Docker container
│   └── stop_container.sh      # Script to stop Docker container
appspec.yml                    # CodeDeploy configuration

IAM Roles
The following IAM roles were created for secure access control:
1. codepipeline-python-flask-app-on-ec2
   - Used by AWS CodePipeline.
   - Allows pipeline orchestration and triggering CodeBuild/CodeDeploy.
 
2. codebuild-python-flask-app-on-ec2
   - Used by AWS CodeBuild.
   - Grants permissions for S3 (artifacts), ECR/Docker registry (push images), and CloudWatch logs.
 
3. codedeploy-python-flask-app-on-ec2
   - Used by AWS CodeDeploy and attached to the EC2 instance.
   - Allows deployment agent on EC2 to fetch artifacts and execute lifecycle hooks.

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
