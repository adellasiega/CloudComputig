# Nextcloud Cloud-based Storage Service & Load Testing with Locust

## Description
This project sets up a Nextcloud instance using Docker and performs load testing using Locust. Nextcloud is a self-hosted file sharing and collaboration platform, and Locust is an open-source load testing tool.

## Usage
1. Clone this repository.
2. Make sure you have Docker installed on your system.
3. Navigate to the project directory.
4. Run the following command to start the Nextcloud instance and Locust load testing:

    ```bash
    sudo docker-compose up
    ```

5. Access Nextcloud via your web browser at `http://localhost:8080`.
6. Access Locust's web interface for load testing at `http://localhost:8089`.
7. Customize Locust's test scenarios by editing `locust/tasks.py`.
8. Monitor load testing results through Locust's web interface.

## Configuration
- `docker-compose.yml`: Defines services for Nextcloud and Locust, along with their configurations
  - Nextcloud service:
    - Uses the latest Nextcloud Docker image
    - Exposes Nextcloud on port 8080
    - Sets environment variables for Nextcloud admin username, password, SQLite database name, and database directory
    - Mounts a volume for Nextcloud data persistence
  - Locust service:
    - Uses the Locust Docker image
    - Exposes Locust's web interface on port 8089
    - Specifies command-line arguments to run Locust with custom test scenarios and target host.
    - Mounts volumes for Locust test scripts and data

## Files
- `docker-compose.yml`: Docker Compose configuration file
- `locust/tasks.py`: Python script defining Locust test scenarios
- `test-data/`: Directory containing test data for Locust

## Authror
Alessandro Della Siega

University of Trieste, March 2024
