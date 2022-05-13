# Helm Exercise 3

## Result:
You will learn how to use Helm templates to make K8s yaml less repetitive and easier to manage. You will use `values.yaml` file to provide variable values to your Helm chart like a Docker image version. You will override those values with a flag and another file.
## Steps:

1. In the yaml files replace every hardcoded `python-test` with the dynamic Helm release name.
2. Add the same release name to the `NOTES.txt` file.
3. Check the Helm chart, install it, get the manifest, see that it works.
4. Create a values file with image repository and tag.
5. Update deployment file with the dynamic image repository and tag.
6. Using the `template` command see that the correct image data is set.
7. Using the `template` command with a `set` flag override image tag and see that it is set.
8. Create a `values-stg.yaml` file, override tag version.
9. Using the `template` command with a `values` flag point to the `values-stg.yaml` file and see that the updated tag is set.

## Tips:
- Useful `helm` commands:
  - `helm create <chartName>`
  - `helm template <chartName>`
  - `helm template <chartName> --set <path.to.key>=<value>`
  - `helm template <chartName> --values <file>`
  - `helm install <releaseName> <chartName>`
  - `helm get manifest <releaseName>`
  - `helm uninstall <releaseName>`
- Useful `kubectl` commands:
  - `kubectl get deployments`
  - `kubectl get services`


