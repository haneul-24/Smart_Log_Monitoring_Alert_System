# Smart Log Monitoring, Alert & Retention System
A real-time log monitoring and alert system built with FastAPI and MongoDB that tracks service logs, provides error summaries, and sends alerts for critical issues.

## About 
**What does the project do:**

The Smart Log Monitoring & Alert System is a comprehensive tool for monitoring logs from multiple services. It provides:

- **Real-time log collection:** Collect logs from various services automatically.
- **Log categorization:** Organize logs by severity: INFO, WARNING, ERROR.
- **View all logs / error logs:** Quickly access all logs or only the critical error logs.
- **Filtering:** Filter logs by service or severity for faster troubleshooting.
- **Log summaries:** Generate summaries with total logs, counts by level, and errors by service.
- **Alerts & notifications:** Highlight high-warning, warning, and danger levels based on error thresholds.
- **Persistent logging:** Maintain a record of all logs in a database (MongoDB).
- **Safe and structured storage:** Logs are timestamped and stored with UTC timezone.
- **User-friendly interface:** Console-based interface with clear formatting and colors.
- **APIs available:** RESTful APIs to push and fetch logs programmatically.
- **Error handling & stability:** Handles failed connections, invalid requests, and duplicate logs gracefully.

**Why it exists:**

Manual log checking is tedious and error-prone. Applications can fail silently or generate large volumes of logs, making it hard to find critical issues. This system exists to:

- Automate log monitoring across services.
- Quickly identify errors and warnings, preventing downtime.
- Provide actionable insights through summaries and alerts.
- Support developers and admins in maintaining healthy applications efficiently.

## Features of the project: 
1. Multi-Service Log Monitoring
- Tracks logs from multiple services like Authentication, Payment, and Order services.

2. Log Level Categorization
- Classifies logs into INFO, WARNING, and ERROR.

3. Real-Time Alerts
+ Generates alerts for services with high error counts:

  - 🔴 Danger (≥5 errors)
  - 🟠 Warning (3–4 errors)
  - 🟡 High Warning (1–2 errors)

4. Logs Summary
- Provides a quick summary of logs: total logs, counts of each level, and errors by service.

5. Filter Logs
- Allows filtering logs by service and/or log level.

6. Persistent Storage with MongoDB
- Stores logs in MongoDB for retrieval, analysis, and persistence.

7. User-Friendly Console Interface
- Clear visual output using upper() and lower() for better readability.

8. API Support (Optional for Integration)
- RESTful endpoints to create, fetch, and delete logs programmatically.

9. Logging System
- All actions in the monitoring system are logged using Python’s logging module.

10. Time-Based Error Monitoring
- Detects recent error spikes (e.g., within last 1 minute) for faster incident response.

## Tech Stack

**Programming Language**

- Python 3.12.3

**Backend Framework**

- FastAPI – for building high-performance REST APIs

**Database**

- MongoDB (Atlas) – NoSQL database for persistent log storage

**Database Driver**

- PyMongo – MongoDB client library for Python

**Logging & Monitoring**

- Python Logging Module – for structured application logging

**API & Networking**

- Requests – for making HTTP API calls between services

**Configuration & Environment**

- python-dotenv – for managing environment variables securely

**Scheduling & Automation**

- Cron Jobs (Linux/WSL) – for periodic log monitoring, alerts, and cleanup

**Development Environment**

- Linux / WSL

- Virtual Environment (venv)


**Version Control & Collaboration**

- Git

- GitHub

## Project Structure

**Smart_Log_Monitoring_Alert_System/**

- **alert_engine.py**      ➡️ cron job 
  -  Cron job to detect ERROR spikes (counts errors in last 1 minute and triggers alerts based on log count and per-service analysis) 

- **cleanup_logss.py**     ➡️  cron job  
  -  Cron job to automatically delete logs older than 7 days

- **log_producer_app.py**  ➡️  cron job
  - Sample application to generate logs automatically (used for testing and demonstration)

- **logger_config.py**
  - Central logging configuration (stores application logs in app.log)

- **python_API.py**
  -  FastAPI-based REST API for log ingestion and retrieval

- **monitoring.py**
  - Core monitoring logic for the system

- **utils.py**
  -  Helper and utility functions

- **main.py**
  - Menu-based CLI application (main entry point)

- **requirements.txt**
  - List of required Python packages

**Run main file using the command:**

```python main.py```

## Installation 

### 1. clone the repo
- **Github repository:** https://github.com/haneul-24/Smart_Log_Monitoring_Alert_System

- ```git clone https://github.com/haneul-24/Smart_Log_Monitoring_Alert_System.git```

### 2. Create Virtual Environment:

```python -m venv venv```

**Activate it:**

**Linux/WSL**
```source venv/bin/activate```

**Windows**:
```venv\Scripts\activate```

### 3. Install dependencies:
```pip install -r requirements.txt```

### 4.Configure enviroments variables:
Create a ```.env``` file in the project root

### 5. Setup logging:
Logging is automatically configured using ```logger_config.py```.

All logs will be stored in:

```app.log```

### 6. Start the FastAPI Server

```uvicorn main:app --reload```

### 7. Test API Endpoints
Open browser or Postman:

```GET  /          → Welcome message```

```POST /logs      → Create logs```

```GET  /logs      → View all logs```

```GET  /logs/error → View ERROR logs```

```DELETE /logs/{id} → Delete a log```

### 8. Setup Cron Job
```crontab -e```

## Cron Job Support

Cron jobs can be configured to:

- Periodically monitor error logs
- Trigger alert checks automatically
- Manage log retention and cleanup

## Usage
- Generate logs from multiple services

- Store logs in MongoDB via FastAPI

- View all logs or only ERROR logs

- Monitor logs using CLI tool

- Filter logs by service and level

- Generate alerts for frequent errors

- Automatically clean old logs

## Real World Applications 

- Monitoring microservices in production environments

- Detecting failures in payment, authentication, or order systems  

- Supporting DevOps and SRE teams with error alerts  

- Log analysis for debugging and root-cause analysis 

- CI/CD pipeline monitoring and validation  

- Maintaining application health and reducing downtime  


## License
This project is licensed under the **MIT License**.

## Author 
**Sejal**