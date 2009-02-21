Name:		libopensync-plugin-moto
Version:	0.22
Release:	%mkrel 1

Summary:	Python plugin for using opensync with motorola phones
License:	GPLv2
Group:		System/Libraries
URL:		http://www.opensync.org/
Source:		libopensync-plugin-moto-0.22.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	libopensync-plugin-python

%description
This is a VERY EXPERIMENTAL plugin for syncing with Motorola phones 
using the AT command set. It supports syncing phonebook and calendar 
entries (ie. the contact and event object types). It will most likely
mess up the data on your phone and any other members of the sync group,
due to the limited data that can be stored on the phone. Use with caution
and make backups!

To prevent it writing any changes to the phone, set WRITE_ENABLED to False
(near the top of the file). Note that this will still allow it to send data
back to the other members of the sync group, so you probably want to have
backups of everything anyway. See TESTING/BACKUP below.

The models known to work are :
 * L7 SLVR
 * V3i RAZR

%prep
%setup -q

%build
%install
rm -rf %{buildroot}
# can be used to backup phone's content before testing
mkdir -p %{buildroot}%{_bindir}
cp mototool %{buildroot}%{_bindir}
# actual opensync plugin
mkdir -p %{buildroot}%{_libdir}/opensync/python-plugins
cp motosync.py %{buildroot}%{_libdir}/opensync/python-plugins
mkdir -p %{buildroot}%{_datadir}/opensync/defaults
cp moto-sync %{buildroot}%{_datadir}/opensync/defaults

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/mototool
%{_libdir}/opensync/python-plugins/motosync.py
%{_datadir}/opensync/defaults/moto-sync

