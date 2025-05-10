
## Code Environment
Run below commands

    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt

## Variables Environment
copy .env-sample into .env (Do not commit .env)


## Setup Docker Application
Run below commands to build application

    docker-compose -f .\docker-compose.yml build

Run below commands to run application

    docker-compose -f .\docker-compose.yml up -d



## 🗂 Folder Structure

    your-project/
    │
    ├── app/
    │   └── main.py            # Your FastAPI app code
    │
    ├── Dockerfile         # Build instructions for the app
    ├── docker-compose.yml # Setup services, ports, volumes, etc
    │
    ├── requirements.txt       # Python dependencies
    │
    └── README.md              # (optional) project description
