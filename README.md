# demo-app

# Demo Calculator App

This is a simple calculator web application built using Flask and Docker. The app demonstrates basic arithmetic operations and serves as a demo for containerizing Python applications.

## Features

- **Basic Calculator:** Perform addition, subtraction, multiplication, and division.
- **Dockerized Application:** Easily build, run, and share the app using Docker.
- **Web-Based Interface:** Simple HTML form for user input and displaying results.

## Project Structure


- **Dockerfile:** Defines the Docker image for the app.
- **app.py:** Contains the Flask application code, including the calculator logic.
- **requirements.txt:** Lists Python dependencies.
- **.gitignore:** Specifies files and directories to ignore in Git.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Git](https://git-scm.com/) (optional, for version control).

## Getting Started


#### Initialize an empty Git repository
```bash
git init
```
#### Add all project files to the repository
```bash
git add .
```
#### Commit the changes
```bash
git commit -m "Updated docker"
```
#### Add a remote repository (replace the URL with your repository URL)
```bash
git remote add origin https://github.com/yourusername/demo-app.git
```
#### (Optional) If you need to rename the default branch to main:
```bash
git branch -M main
```

# Push the changes to the remote repository
```bash
git push -u origin main
```
### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/demo-app.git
cd demo-app
```

## Building and Running the Docker Container
```bash
docker build -t demo-app .
docker run -d -p 5000:5000 demo-app
```
The Flask app listens on port 5000 inside the container, but you access it via http://localhost:5001.

### Tagging and Pushing the Image to Docker Hub
```bash
docker tag demo-app milroyp/demo-app:latest
docker push milroyp/demo-app:latest
```
### Pulling the Image from the Docker Hub
```bash
docker pull milroyp/demo-app:latest
```
### Running the Container
```bash
docker run -p 5001:5000 milroyp/demo-app:latest
```