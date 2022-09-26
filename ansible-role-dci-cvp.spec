%define _source_payload w0.gzdio
%define _binary_payload w0.gzdio

Name:       ansible-role-dci-cvp
Version:    0.0.2
Release:    1.VERS%{?dist}
Summary:    ansible-role-dci-cvp
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-cvp
Source0:    ansible-role-dci-cvp-%{version}.tar.gz

BuildArch:  noarch

%description
An Ansible role that is used to automate cvp testing

%prep
%setup -qc


%build

%install
make install BUILDROOT=%{buildroot} DATADIR=%{_datadir}/dci

%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-cvp


%changelog
* Mon Sep 26 2022 Frederic Lepied <flepied@redhat.com> 0.0.2-1
- use a Makefile to install

* Wed Aug 24 2022 Bill Peck <bpeck@redhat.com> - 0.0.1-2
- Rebuild for el9

* Wed Apr 28 2021 Bill Peck <bpeck@redhat.com> - 0.0.1-1
- Initial release
