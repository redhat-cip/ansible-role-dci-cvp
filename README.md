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
    dci_cvp_bundle_spec:  "{{ cvp_bundle_spec }}"
    dci_cvp_bundle_tag: "{{ cvp_bundle_tag }}"
    dci_cvp_pullsecret_file: "{{ dci_pullsecret_file }}"
    dci_cvp_registry_host: "{{ dci_registry_host }}"
    dci_cvp_cache_dir: "{{ dci_cache_dir }}"
    dci_cvp_cs_url: "{{ dci_cs_url }}"
    dci_cvp_client_id: "{{ dci_client_id }}"
    dci_cvp_api_secret: "{{ dci_api_secret }}"
    dci_cvp_pyxis_submit: "{{ pyxis_cvp_submit }}"
    dci_cvp_pyxis_apikey: "{{ pyxis_apikey }}"
    dci_cvp_pyxis_identifier: "{{ pyxis_identifier }}"
  when:
    - cvp_bundle_spec is defined
...
```

## License

Apache License, Version 2.0 (see [LICENSE](LICENSE) file)

## Contact

Email: Distributed-CI Team <distributed-ci@redhat.com>
IRC: #distributed-ci on Freenode
