# Python_Web_App_with_Docker_-_K8s
Auto-scaling Docker Kubernetes Project
This project demonstrates automatic scaling of a Python Flask application using Docker and Kubernetes. The application includes CPU-intensive endpoints to demonstrate auto-scaling capabilities.
Prerequisites
* Docker Desktop
* Python 3.9+
* Minikube
* kubectl
* MacOS/Linux environment
Project Structure

Copy
autoscale-docker-k8s/
├── app.py
├── Dockerfile
├── requirements.txt
├── load_test.py
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    └── hpa.yaml
Setup Instructions
1. Install Required Tools
bash
Copy
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Docker Desktop
brew install --cask docker

# Install kubectl
brew install kubectl

# Install Minikube
brew install minikube
2. Clone and Setup Project
bash
Copy
# Create project directory
mkdir autoscale-docker-k8s
cd autoscale-docker-k8s

# Create Python files and Kubernetes configs
# Copy the provided files into their respective locations
3. Build and Push Docker Image
bash
Copy
# Build Docker image
docker build -t yourusername/autoscale-docker-k8s:latest .

# Login to Docker Hub
docker login

# Push image to Docker Hub
docker push yourusername/autoscale-docker-k8s:latest
4. Deploy to Kubernetes
bash
Copy
# Start Minikube
minikube start --driver=docker

# Enable metrics server
minikube addons enable metrics-server

# Apply Kubernetes configurations
kubectl apply -f k8s/

# Verify deployments
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get hpa
5. Test Auto-scaling
bash
Copy
# Start Minikube tunnel (in a separate terminal)
minikube tunnel

# Get service URL
minikube service autoscale-docker-k8s --url

# Run load test
python load_test.py

# Monitor scaling (in a separate terminal)
kubectl get hpa -w
kubectl get pods -w
Verification Steps
1. Check if pods are running:
bash
Copy
kubectl get pods
# Should show pods in "Running" state
1. Check service:
bash
Copy
kubectl get services
# Should show autoscale-docker-k8s service with an external IP
1. Check HPA:
bash
Copy
kubectl get hpa
# Should show autoscale-docker-k8s HPA with current/target metrics
Troubleshooting
1. If pods aren't starting:
bash
Copy
kubectl describe pod <pod-name>
1. If service isn't accessible:
bash
Copy
minikube tunnel  # Run in separate terminal
1. If HPA isn't working:
bash
Copy
kubectl describe hpa autoscale-docker-k8s
Common Issues and Solutions
1. Port already in use:
    * Use a different port in docker run command
    * Example: docker run -p 8080:5000 yourusername/autoscale-docker-k8s:latest
2. Metrics not available:
    * Ensure metrics-server is enabled
    * minikube addons enable metrics-server
3. Connection refused:
    * Ensure minikube tunnel is running
    * Check if service is properly exposed
Cleanup
bash
Copy
# Delete Kubernetes resources
kubectl delete -f k8s/

# Stop Minikube
minikube stop

# Optional: Delete Minikube cluster
minikube delete
Monitoring and Scaling
* Monitor CPU usage:
bash
Copy
kubectl top pods
* Check scaling events:
bash
Copy
kubectl describe hpa autoscale-docker-k8s
* View logs:
bash
Copy
kubectl logs deployment/autoscale-docker-k8s
Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.
