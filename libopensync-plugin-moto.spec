Name:           libopensync-plugin-moto
Version:        0.22
Epoch:          1
Release:        %mkrel 2
Summary:        Plugin for syncing with Motorola phones via libopensync
License:        GPLv2+
Group:          Office
URL:            http://www.opensync.org
Source:         http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  libopensync-devel < 0.30
Requires:       libopensync >= %{epoch}:%{version}
Requires: python-dateutil
Requires: python-pybluez
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%description
Plugin for syncing with Motorola phones via libopensync.



%prep
%setup -q


%build

%install
install -p -m644 -D motosync.py \
    %{buildroot}/%{_libdir}/opensync/python-plugins/motosync.py
install -p -m644 -D moto-sync \
    %{buildroot}/%{_datadir}/opensync/defaults/moto-sync

%clean

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/opensync/python-plugins/motosync*
%{_datadir}/opensync/defaults/moto-sync

%changelog
* Sat Apr  4 2009 Daniel Lucio <dlucio@okay.com.mx>  1:0.22-1mdv2009.1
- #1 try

