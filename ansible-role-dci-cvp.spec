%define _source_payload w0.gzdio
%define _binary_payload w0.gzdio

Name:       ansible-role-dci-cvp
Version:    0.0.1
Release:    1%{?dist}
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
mkdir -p %{buildroot}%{_datadir}/dci/roles/dci-cvp
chmod 755 %{buildroot}%{_datadir}/dci/roles/dci-cvp

cp -r defaults %{buildroot}%{_datadir}/dci/roles/dci-cvp
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-cvp


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-cvp


%changelog
* Wed Apr 28 2021 Bill Peck <bpeck@redhat.com> - 0.0.1-1
- Initial release
