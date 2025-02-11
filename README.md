# Python_Web_App_with_Docker_-_K8s
# Python Web App with Docker & Kubernetes

## 🚀 Auto-scaling Docker Kubernetes Project
This project demonstrates **automatic scaling** of a Python Flask application using **Docker** and **Kubernetes**. The application includes CPU-intensive endpoints to showcase **auto-scaling capabilities**.

---

## 📌 Prerequisites
Ensure you have the following installed:

- **Docker Desktop**
- **Python 3.9+**
- **Minikube**
- **kubectl**
- **MacOS/Linux environment**

---

## 📁 Project Structure
```
autoscale-docker-k8s/
├── app.py
├── Dockerfile
├── requirements.txt
├── load_test.py
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    └── hpa.yaml
```

---

## 🛠️ Setup Instructions

### **1️⃣ Install Required Tools**
#### Install Homebrew (if not installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
#### Install Docker Desktop:
```bash
brew install --cask docker
```
#### Install kubectl:
```bash
brew install kubectl
```
#### Install Minikube:
```bash
brew install minikube
```

### **2️⃣ Clone and Setup Project**
#### Create project directory:
```bash
mkdir autoscale-docker-k8s && cd autoscale-docker-k8s
```
#### Copy provided Python files and Kubernetes configs to respective locations.

### **3️⃣ Build and Push Docker Image**
#### Build Docker image:
```bash
docker build -t yourusername/autoscale-docker-k8s:latest .
```
#### Login to Docker Hub:
```bash
docker login
```
#### Push image to Docker Hub:
```bash
docker push yourusername/autoscale-docker-k8s:latest
```

### **4️⃣ Deploy to Kubernetes**
#### Start Minikube:
```bash
minikube start --driver=docker
```
#### Enable Metrics Server:
```bash
minikube addons enable metrics-server
```
#### Apply Kubernetes configurations:
```bash
kubectl apply -f k8s/
```
#### Verify deployments:
```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get hpa
```

### **5️⃣ Test Auto-scaling**
#### Start Minikube tunnel (in a separate terminal):
```bash
minikube tunnel
```
#### Get service URL:
```bash
minikube service autoscale-docker-k8s --url
```
#### Run Load Test:
```bash
python load_test.py
```
#### Monitor Scaling (in a separate terminal):
```bash
kubectl get hpa -w
kubectl get pods -w
```

---

## ✅ Verification Steps

### Check if pods are running:
```bash
kubectl get pods
```
✅ Should show pods in **"Running"** state.

### Check service status:
```bash
kubectl get services
```
✅ Should show **autoscale-docker-k8s** service with an external IP.

### Check Horizontal Pod Autoscaler (HPA):
```bash
kubectl get hpa
```
✅ Should show **autoscale-docker-k8s** HPA with current/target metrics.

---

## 🛠️ Troubleshooting

### **Pods aren't starting?**
```bash
kubectl describe pod
```
### **Service isn't accessible?**
```bash
minikube tunnel   # Run in separate terminal
```
### **HPA isn't working?**
```bash
kubectl describe hpa autoscale-docker-k8s
```

---

## 🔥 Common Issues and Solutions

- **Port already in use?**
  ```bash
  docker run -p 8080:5000 yourusername/autoscale-docker-k8s:latest
  ```
  ✅ Use a different port in the **docker run** command.

- **Metrics not available?**
  ```bash
  minikube addons enable metrics-server
  ```
  ✅ Ensure the **metrics-server** is enabled.

- **Connection refused?**
  ```bash
  minikube tunnel
  ```
  ✅ Ensure **Minikube tunnel** is running and service is properly exposed.

---

## 🧹 Cleanup

### Delete Kubernetes resources:
```bash
kubectl delete -f k8s/
```
### Stop Minikube:
```bash
minikube stop
```
### (Optional) Delete Minikube cluster:
```bash
minikube delete
```

---

## 📊 Monitoring and Scaling

### Monitor CPU usage:
```bash
kubectl top pods
```
### Check scaling events:
```bash
kubectl describe hpa autoscale-docker-k8s
```
### View logs:
```bash
kubectl logs deployment/autoscale-docker-k8s
```

---

## 🤝 Contributing

1. **Fork** the repository.
2. **Create** your feature branch.
3. **Commit** your changes.
4. **Push** to the branch.
5. **Create** a new **Pull Request**.

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

🎉 **Happy Coding!** 🚀

