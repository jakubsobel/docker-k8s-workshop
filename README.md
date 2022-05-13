## Tips:
- Useful `Dockerfile` instructions:
  - `FROM <image>:<tag>`
  - `ENTRYPOINT ["executable", "param1", "param2"]`
  - `CMD ["executable","param1","param2"]`
  - `CMD ["param1","param2"]`  - as default parameters to ENTRYPOINT
  - `WORKDIR <path>`
  - `COPY <hostPath> <dockerPath>` - `dockerPath` is relative to the set `WORKDIR` 
  - `EXPOSE <port>`
  - [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- Useful `docker` commands:
  - `docker build -t <username>/<name>:<version> .`
  - `docker run [OPTIONS] <username>/<name>:<version> [COMMAND]`
    - `--rm` - automatically clean up the container and remove the file system when the container exits
    - `-d` - container will run in a detached (background) mode
    - `-p <hostPort>:<dockerPort>` - expose port
    - `-v <hostPath>:<dockerPath>` - mount filesystem; `dockerPath` is relative to the set `WORKDIR` 
    - `-it` - interactive terminal
  - `docker push <username>/<name>:<version>`   
  - `docker compose up`    
  - [Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)
- Useful `docker-compose` fields:
  - ```yaml
    image: <username>/<name>:<version>
    volumes:
        - <hostPath>:<dockerPath>
        - ...
    ports:
        - <hostPort>:<dockerPort>
        - ...
    depends_on: <service_name>
    ```
  - [Docker Compose overview](https://docs.docker.com/compose/)
- Useful `kubectl` commands:
  - `kubectl config use-context docker-desktop`
  - `kubectl get nodes`
  - `kubectl get deployments`
  - `kubectl get pods`
  - `kubectl get replicasets`
  - `kubectl get services`
  - `kubectl apply -f <file>`
  - `kubectl delete deployments <name>` - name from the deployment `metadata.name` in the yaml file
  - `kubectl delete services <name>` - name from the service `metadata.name` in the yaml file
  - `kubectl rollout history deployments`
  - `kubectl rollout undo deployments <name>`
  - [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
  - [kubectl Reference Docs](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
- Useful `helm` commands:
  - `helm version`
  - `helm ls`
  - `helm create <chartName>`
  - `helm template <chartName>`
  - `helm template <chartName> --set <path.to.key>=<value>`
  - `helm template <chartName> --values <file>` 
  - `helm install <releaseName> <chartName>`
  - `helm install <releaseName> <chartName> --values <file>`
  - `helm get manifest <releaseName>`
  - `helm uninstall <releaseName>`
  - [Helm Commands](https://helm.sh/docs/helm/helm/)
