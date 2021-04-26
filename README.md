# DCI Openshift CVP Role

`ansible-role-dci-cvp` enables CVP operator tests in the Red Hat Distributed CI service.

## Table of Contents

- [Requirements](#requirements)
- [License](#license)
- [Contact](#contact)

## Requirements

This role can't be used on it's own.  It shold be called from either the `dci-openshift-agent` or from the install hook of `dci-openshift-app-agent`.

Here is an example of calling this role:
```yaml
---
- name: Execute CVP Operators role
  include_role:
    name: dci-cvp
  vars:
    OO_BUNDLE_SPEC:  "{{ dci_cvp_bundle_spec }}"
    OO_PACKAGE: "{{ dci_cvp_package }}"
    OO_CHANNEL: "{{ dci_cvp_channel }}"
    DCI_SUBMIT: "{{ dci_cvp_submit | default(false) }}"
    dci_cvp_cache_dir: "{{ dci_cache_dir }}"
    dci_cvp_cs_url: "{{ dci_cs_url }}"
    dci_cvp_client_id: "{{ dci_client_id }}"
    dci_cvp_api_secret: "{{ dci_api_secret }}"
  when:
    - dci_cvp_bundle_spec is defined
    - dci_cvp_package is defined
    - dci_cvp_channel is defined
...
```

## License

Apache License, Version 2.0 (see [LICENSE](LICENSE) file)

## Contact

Email: Distributed-CI Team <distributed-ci@redhat.com>
IRC: #distributed-ci on Freenode
