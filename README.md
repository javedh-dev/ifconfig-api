Sure, here is a sample `README.md` file for your Flask API application:

```markdown
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
```

The API will be accessible at `http://127.0.0.1:5000/get-data`.

## Docker

### Building the Docker Image

To build the Docker image, use the following command:

```bash
docker build -t flask-api .
```

### Running the Docker Container

To run the Docker container, use the following command:

```bash
docker run -p 5000:5000 flask-api
```

The API will be accessible at `http://<docker-host-ip>:5000/get-data`.

## GitHub Actions

A GitHub Actions workflow is set up to automatically build and push the Docker image to GHCR on each push to the `main` branch.

### GitHub Actions Workflow

The workflow file is located at `.github/workflows/docker-publish.yml` and contains the following steps:

- Checkout the repository
- Set up Docker Buildx
- Log in to GitHub Container Registry
- Build and push the Docker image to GHCR

### Secrets Configuration

Ensure your repository has the `GITHUB_TOKEN` secret configured. This token is automatically provided by GitHub Actions and has permissions to authenticate to GHCR.

## Usage

Once the Docker container is running, you can access the API endpoint:

```bash
curl http://<docker-host-ip>:5000/get-data
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation:

- **Prerequisites**: Lists the requirements for running the project.
- **Installation**: Provides steps to clone the repository and install dependencies.
- **Running Locally**: Describes how to run the Flask application locally.
- **Docker**: Explains how to build and run the Docker container.
- **GitHub Actions**: Provides details on the CI/CD setup with GitHub Actions.
- **Usage**: Shows how to access the API once it’s running.
- **License**: Mentions the project's license.

Make sure to replace `your-username` and `your-repository` with your actual GitHub username and repository name.
