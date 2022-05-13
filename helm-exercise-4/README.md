# Helm Exercise 4

## Result:
You will run two Helm deployments using a separate values files, simulating different type of deployments. You will see how to upgrade the helm deployment to update the values.
## Steps:

1. In the default value file set default port number.
2. In the stg values file set the port to 8082.
3. Update the service file to use values variable as a port.
4. Using `template` command check that the port is correctly set for the default and stg values.
5. Install both deployments using default install, and install with `--values` flag.
6. Check that both `localhost:8081` and `localhost:8082` are running.
7. Check that `kubectl` is showing both releases deployments and services.
8. Change image tag version in the values stg.
9. Use `upgrade` command to create new Helm revision.
10. Check that now there are two different versions of the API running.
## Tips:
- Useful `helm` commands:
  - `helm create <chartName>`
  - `helm template <chartName>`
  - `helm template <chartName> --set <path.to.key>=<value>`
  - `helm template <chartName> --values <file>`
  - `helm install <releaseName> <chartName>`
  - `helm install <releaseName> <chartName> --values <file>`
  - `helm ls`
  - `helm uninstall <releaseName>`
- Useful `kubectl` commands:
  - `kubectl get deployments`
  - `kubectl get services`


