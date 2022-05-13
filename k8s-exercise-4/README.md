# K8s Exercise 4

## Result:
You will learn how to upgrade and rollback your k8s deployments. You will make a new version of the docker image and then apply the changes to the running deployment and then go back to the previous version.

## Steps:

1. Edit the `k8s.yaml` file, fill the correct `python` API image from the Docker Exercise 3.\
  You can optionally use my image: `jakubsobelyg/python-test:0.0.4`
2. Start the deployment and the service and check that the API is working.
3. Edit the `app.py` file, add another book entry.
4. Using `docker` build and push the image to your `python` API repository using the newer tag.
5. Edit the `k8s.yaml` file, update the `python` API image version to the new one.
6. Apply the updated file.
7. Check in the browser that now the updated version is running.
8. Using `kubectl` rollback to the previous version.
7. Check in the browser that now the old version is running.
8. Delete the deployment and the service.


## Tips:
- Useful `kubectl` commands:
  - `kubectl apply -f <file>`
  - `kubectl describe deployments`
  - `kubectl describe pods`
  - `kubectl rollout history deployments`
  - `kubectl rollout undo deployments <name>`
  - `kubectl get deployments`
  - `kubectl get pods`
  - `kubectl get replicasets`
  - `kubectl get services`
  - `kubectl delete deployments <name>` - name from the deployment `metadata.name` in the yaml file
  - `kubectl delete services <name>` - name from the service `metadata.name` in the yaml file
  - [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
  - [kubectl Reference Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
- Useful `docker` commands:
  - `docker build -t <username>/<name>:<version> .`
  - `docker run [OPTIONS] <username>/<name>:<version> [COMMAND]`
    - `--rm` - automatically clean up the container and remove the file system when the container exits
    - `-d` - container will run in a detached (background) mode
    - `-p <hostPort>:<dockerPort>` - expose port
    - `-v <hostPath>:<dockerPath>` - mount filesystem; `dockerPath` is relative to the set `WORKDIR` 
    - `-it` - interactive terminal
  - `docker push <username>/<name>:<version>`    
  - [Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)

