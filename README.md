# Flask API with Docker and GitHub Actions

This project is a simple Flask API that makes a request to an external API and returns the JSON response. The project is containerized using Docker and set up with a GitHub Actions workflow to build and push the Docker image to GitHub Container Registry (GHCR).

## Features

- Flask API that calls an external API and returns the response
- Containerized with Docker for easy deployment
- GitHub Actions workflow to automate Docker image building and pushing

## Prerequisites

- Docker
- GitHub account with access to GitHub Container Registry

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

To run the Flask application locally, use the following command:

```bash
flask run
