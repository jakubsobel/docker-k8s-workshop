# K8s Exercise 2

## Result:
You will create a k8s deployment of the `python` API server image created in the Docker Exercise 3. You will see how K8s deployment is creating pods and how you can apply changes to the running deployment. 
## Steps:

1. Edit the `k8s.yaml` file, use the `python` API image that you've created in the Docker Exercise 3\
  You can optionally use my image: `jakubsobelyg/python-test:0.0.4`
2. Create the deployment using the `kubectl` command
3. Check list of created deployments, pods and replicasets
4. Change number of replicas in the `k8s.yaml` file
5. Apply the changed file and check the pods again
6. Delete the deployment, check the above resources (deployments, pods, replicasets) again


## Tips:
- Useful `kubectl` commands:
  - `kubectl apply -f <file>`
  - `kubectl get deployments`
  - `kubectl get pods`
  - `kubectl get replicasets`
  - `kubectl delete deployments <name>` - name from the deployment `metadata.name` in the yaml file
  - [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
  - [kubectl Reference Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)