# Ansible Content Testing repository

[![CI](https://github.com/geerlingguy/ansible-content-testing/workflows/CI/badge.svg?branch=master)](https://github.com/geerlingguy/ansible-content-testing/actions?query=workflow%3ACI)

This repository is meant to test the migration of various types of module and role invocations against the 'next generation' of Ansible, e.g. the ACD Ansible Community Distribution.

## Testing

This project uses `molecule` to run tests in a controlled execution environment, and also requires `kind` to be installed for a local Kubernetes cluster to test against. Finally, it also requires the `openshift` Docker library be installed (`pip3 install openshift`).

Make sure you have [Molecule](https://molecule.readthedocs.io/en/latest/), [Docker](https://docs.docker.com/get-docker/), and [Kind](https://kind.sigs.k8s.io) installed, then run:

    molecule test

The [CI GitHub Actions Workflow](https://github.com/geerlingguy/ansible-content-testing/actions?query=workflow%3ACI) is meant to test this playbook against the following scenarios:

  - Latest Ansible 2.9.x release (should pass)
  - Latest Ansible ACD release (what will become 2.10) (should pass)
  - Latest ansible-base release (`devel` branch) (should fail)

## License

MIT.

## Author

[Jeff Geerling](https://www.jeffgeerling.com) maintains a [large variety of Ansible content](https://ansible.jeffgeerling.com).
