# Helm Exercise 2

## Result:
You will create a Helm chart and will use K8s service and deployment from the K8s exercises to run it using helm. You will be able to see the deployment notes and uninstall both with a single command.
## Steps:

1. Create a Helm chart
2. Remove everything except for `Chart.yaml` and `NOTES.txt`
3. Create separate deployment and service yaml files and fill it with the content from the `k8s.yaml` file
4. Update `NOTES.txt` to your liking.
5. Install the Helm chart
6. Check that the notes showed and that the server is running
7. Using `kubectl` check that deployment and service were created
8. Uninstall Helm chart
9. Using `kubectl` check that deployment and service were removed


## Tips:
- Useful `helm` commands:
  - `helm create <chartName>`
  - `helm template <chartName>`
  - `helm install <releaseName> <chartName>`
  - `helm ls`
  - `helm uninstall <releaseName>`
- Useful `kubectl` commands:
  - `kubectl get deployments`
  - `kubectl get services`


