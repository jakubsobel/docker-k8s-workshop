# K8s Exercise 3

## Result:
You will create a k8s service that will expose the deployment created in the K8s Exercise 2. You will see how K8s service allows you to access the running server in yourt browser.

## Steps:

1. Edit the `k8s.yaml` file, fill the correct `python` API image from the Docker Exercise 3\
  You can optionally use my image: `jakubsobelyg/python-test:0.0.4`
2. Create the deployment and service using the `kubectl` command
3. Check list of created deployments, pods and replicasets
4. Check list of created services
5. Check `localhost:8081` and `localhost:8081/books`
6. Delete the deployment, check the above resources (deployments, pods, replicasets, services) again

## Tips:
- Useful `kubectl` commands:
  - `kubectl apply -f <file>`
  - `kubectl get deployments`
  - `kubectl get pods`
  - `kubectl get replicasets`
  - `kubectl get services`
  - `kubectl delete deployments <name>` - name from the deployment `metadata.name` in the yaml file
  - `kubectl delete services <name>` - name from the service `metadata.name` in the yaml file
  - [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
  - [kubectl Reference Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
