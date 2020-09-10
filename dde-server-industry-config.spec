%global with_debug 1
%global _unpackaged_files_terminate_build 0
%if 0%{?with_debug}
%global debug_package   %{nil}
%endif

Name:           dde-server-industry-config
Version:        5.0.0.3
Release:        1
Summary:        DDE desktop-server industry version special configuration file.
License:        LGPLv3
URL:            http://shuttle.corp.deepin.com/cache/tasks/19366/unstable-amd64
Source0:        http://shuttle.corp.deepin.com/cache/tasks/19366/unstable-amd64/%{name}_%{version}.orig.tar.xz

BuildArch:      noarch

%description
DDE desktop-server industry version special configuration file.

%prep
%setup

%build


%install
install -d %{buildroot}/usr/share/glib-2.0/schemas/
install -Dm644 com.deepin.dde.auth.control.gschema.xml %{buildroot}/usr/share/glib-2.0/schemas/
install -Dm644 com.deepin.dde.control-versiontype.gschema.xml %{buildroot}/usr/share/glib-2.0/schemas/

%files
%{_datadir}/glib-2.0/schemas/*


%changelog
* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> 5.0.0.3
- Initial package build
