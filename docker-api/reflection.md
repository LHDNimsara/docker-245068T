# Reflection of the Docker Project

## What I did

For this assignment, I have created a small API using Python and Flask. The API has two routes. The first route returns my student ID, name and a message. The second route checks the health of the application and returns a simple status message.

Then, I used Docker to containerize the application. I created a Docker to build the Docker image and a compose.yaml file to run the container using Docker Compose. I have also done a port mapping for the API to be able to accessed through localhost:5000

## What I learned

Following this assignment, I have gained the knowledge on basic relationship between a Dockerfile, Docker Image and Docker Container. I also leanred how Docker Compose can contributes to build and run an application easily.

## Challenge

During the assignment, I faced a challenge while running the project with Docker Compose. The container was building successfully, but the API was not reachable from the browser. After checking the setup, I found that the Flask app was listening only on localhost instead of all network interfaces. Because of that, the app was running inside the container but not accessible through the mapped port. I fixed it by setting the app to run on `0.0.0.0` and keeping the port mapping as `5000:5000`. This allowed the application to work correctly through Docker.

## Overall Understanding
Overall, this taks helped me to understand how Docker can create an isolaed environment for executing applications easily with just few simple commands.

