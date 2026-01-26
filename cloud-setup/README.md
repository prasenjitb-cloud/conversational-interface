# Cloud Setup (AWS EC2)

This document describes how the conversational-interface backends are deployed on AWS EC2 using the Free Tier.

A single EC2 instance is used to host:
- Python (Flask) backend
- Node.js (Express) backend

Each backend runs on a different port.

---

## Overview

- Cloud Provider: AWS EC2
- OS: Amazon Linux
- Instance Type: Free Tier eligible
- Public IP: 16.171.224.237

---

## Network Configuration (Security Groups)

The following inbound rules are enabled on the EC2 Security Group:

| Port | Service              | Purpose |
|-----:|----------------------|--------|
| 5000 | Python Flask Backend | `/chat` API |
| 8000 | Node.js Backend      | `/chat` API |

Source for both ports: 0.0.0.0/0

## Deployment (Python Backend)

The Flask backend is deployed on AWS EC2 (Free Tier).

- Cloud Provider: AWS EC2 (Amazon Linux)
- Public IP: 16.171.224.237
- Port: 5000

### Live Test URL
GET:
http://16.171.224.237:5000/chat?message=hello

This endpoint is accessible from both desktop and mobile browsers.

### Notes
- Port 5000 is enabled via EC2 Security Group inbound rules.
- Flask is currently running using the built-in development server.


### AWS Setup Steps
1. Created an EC2 instance (Free Tier)
2. Enabled inbound rule for port 5000
3. Installed Python and Flask
4. Ran the Flask app using `python3 app.py

## Deployment (Node)

The Node.js Server is deployed on AWS EC2 (Free Tier).

- Cloud Provider: AWS EC2 (Amazon Linux)
- Public IP: 16.171.224.237
- Port: 8000

### Live Test URL
GET:
http://16.171.224.237:8000/chat?message=hello

This endpoint is accessible from both desktop and mobile browsers.


### Notes 
Port 8000 is enabled via EC2 Security Group inbound rules.

Express is currently running as the primary server for the frontend UI and Node API.

### AWS Setup Steps for Node
1. Installed Node.js and npm on the existing EC2 instance (16.171.224.237).
2. Enabled inbound rule for port 8000 in the AWS Security Group.
3. Installed required packages using npm install.
4. Started the Node server using node server.js.

