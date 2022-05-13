# K8s Exercise 1

## Result:
You will have a Kubernetes Cluster installed locally and will be able to use `kubectl` command from the terminal.
## Steps:
1. Open Docker Desktop Dashboard.
2. Go to Settings (cogwheel on the top right) -> Kubernetes -> Enable Kubernetes
3. After some time you will see green Kubernetes box next to the green Docker box.
4. Go to the terminal, check if `kubectl` is working correctly, set `docker-desktop` context.

## Tips:
- Useful `kubectl` commands:
  - `kubectl config use-context docker-desktop`
  - `kubectl get nodes`
  - `kubectl get deployments`
  - `kubectl get services`
  - [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
  - [kubectl Reference Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
- If you had the `kubectl` configured already and `docker-desktop` context is not working check the value of the `$KUBECONFIG` env variable:
  - `echo $KUBECONFIG`
  - it should contain the path to `/Users/<username>/.kube/config`
  - if its not there, edit your system preferences. E.g. change the `KUBECONFIG` env variable export in the `~/.zshrc` file.
