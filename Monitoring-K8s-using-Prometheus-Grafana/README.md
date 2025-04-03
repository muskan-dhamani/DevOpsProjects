Monitoring with Prometheus and Grafana on Kubernetes

Prerequisites: 
1. Kubernetes Cluster
2. kubectl configured
3. Cloud Platform
4. Helm - curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version

Steps:
1. Deploy Prometheus - helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack

kubectl get pods -n default

2. Prometheus Dashboard - kubectl port-forward svc/prometheus-operated 9090:9090
http://localhost:9090 or http://<public_ip_address_of_instance>:9090

3. Deploy Grafana - kubectl get svc -n default
kubectl port-forward svc/grafana 3000:80
http://localhost:3000 or http://<public_ip_address_of_instance>:3000

4. Configure Grafana to Use Prometheus as Data Source
Go to Grafana > Configuration > Data Sources > Add Data Source
Select Prometheus and set the URL as http://prometheus-operated:9090
Save & Test

5. Create Dashboards in Grafana
   
