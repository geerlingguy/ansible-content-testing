# Ansible Content Testing repository

This repository is meant to test the migration of various types of module and role invocations against the 'next generation' of Ansible, e.g. the ACD Ansible Community Distribution.

## Testing

This project uses `molecule` to run tests in a controlled execution environment, and also requires `kind` to be installed for a local Kubernetes cluster to test against.

Make sure you have [Molecule](https://molecule.readthedocs.io/en/latest/), [Docker](https://docs.docker.com/get-docker/), and [Kind](https://kind.sigs.k8s.io) installed, then run:

    molecule test

## License

MIT.

## Author

[Jeff Geerling](https://www.jeffgeerling.com) maintains a [large variety of Ansible content](https://ansible.jeffgeerling.com).
