Name:           libopensync-plugin-moto
Version:        0.36
Epoch:          1
Release:        2
Summary:        Plugin for syncing with Motorola phones via libopensync
License:        GPLv2+
Group:          Office
URL:            https://www.opensync.org
Source:         http://www.opensync.org/download/releases/0.36/%{name}-%{version}.tar.bz2
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
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.22-4mdv2011.0
+ Revision: 620173
- the mass rebuild of 2010.0 packages

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 1:0.22-3mdv2010.0
+ Revision: 438728
- rebuild

* Sat Apr 04 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1:0.22-2mdv2009.1
+ Revision: 364048
- Fix requires
- Fix requires

* Sat Apr 04 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1:0.22-1mdv2009.1
+ Revision: 364035
- #3 try
- #2 try

* Sat Feb 21 2009 Guillaume Bedot <littletux@mandriva.org> 0.22-1mdv2009.1
+ Revision: 343718
- import libopensync-plugin-moto


* Sat Feb 21 2009 Guillaume Bedot <littletux@mandriva.org> 0.22-1mdv2009.1
- First package for libopensync-plugin-moto


