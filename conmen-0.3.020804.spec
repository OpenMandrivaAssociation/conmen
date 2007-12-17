#This is NOT a relocatable package
%define name conmen
%define version 0.3.020804
%define release %mkrel 4

Summary:   Console menuscripts for Linux
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.tar.bz2
License:   GPL
Group:     Shells
URL:       http://home.wanadoo.nl/cchq/conmen/index.html
Requires:  dialog >= 0.9a Xdialog
BuildArchitectures: noarch

%description
These are menu scripts for the bash shell.
The program uses dialog and Xdialog.

%prep
  [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
  && rm -rf ${RPM_BUILD_ROOT}/

%setup -q

%install
  mkdir -p ${RPM_BUILD_ROOT}/etc/conmen
  mkdir -p ${RPM_BUILD_ROOT}/usr/bin
  mkdir -p ${RPM_BUILD_ROOT}/usr/lib/conmen
#  mkdir -p ${RPM_BUILD_ROOT}%{_menudir}
  mkdir -p ${RPM_BUILD_ROOT}/var/lib/conmen

  cp conmen \
     cmcfg \
     cmcdrecording \
     cmdialup \
     cmfloppy \
     cmgames \
     cmgraphics \
     cmlog \
     cmm \
     cmmp3 \
     cmprint \
     cmrpm \
     cmsound \
     cmsystem \
     cmuser \
     ${RPM_BUILD_ROOT}/usr/bin

cp -r usr/lib/conmen ${RPM_BUILD_ROOT}/usr/lib

cp cmrc ${RPM_BUILD_ROOT}/etc/conmen

cd ${RPM_BUILD_ROOT}/usr/bin
ln -sf conmen cm

#cat << EOF > ${RPM_BUILD_ROOT}%{_menudir}/%{name}
#?package(conmen): needs="x11" section="Applications/Shells" title="ConMen" longtitle="ConMen is a menu shell" command="%{name}"
#?package(conmen): needs="x11" section="Documentation" title="Conmen Homepage" command="if ps U \$USER | grep -q \$BROWSER; then \$BROWSER -remote \'openURL(%{url})\'; else \$BROWSER \'%{url}\'; fi"
#?package(conmen): title="(Un)Mount CD-ROM" section="Configuration/Other" needs="x11" command="cmm cd"
#?package(conmen): title="(Un)Mount CD-RW" section="Configuration/Other" needs="x11" command="cmm cdr"
#?package(conmen): title="(Un)Mount Windows C:" section="Configuration/Other" needs="x11" command="cmm dosc"
#?package(conmen): title="(Un)Mount Windows D:" section="Configuration/Other" needs="x11" command="cmm dosd"
#?package(conmen): title="(Un)Mount DOS Floppy" section="Configuration/Other" needs="x11" command="cmm df"
#?package(conmen): title="(Un)Mount EXT2 Floppy" section="Configuration/Other" needs="x11" command="cmm e2f"
#EOF

#%post
#%update_menus

#%postun
#%clean_menus

%clean
  [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
  && rm -rf ${RPM_BUILD_ROOT}/

%files
%defattr(-,root,root,755)
%doc AUTHORS BUGS ChangeLog COPYING README THANKS TODO
%config(noreplace) /etc/conmen/cmrc
/usr/bin/conmen
/usr/bin/cm
/usr/bin/cmcfg
/usr/bin/cmcdrecording
/usr/bin/cmdialup
/usr/bin/cmfloppy
/usr/bin/cmgames
/usr/bin/cmgraphics
/usr/bin/cmlog
/usr/bin/cmm
/usr/bin/cmmp3
/usr/bin/cmprint
/usr/bin/cmrpm
/usr/bin/cmsound
/usr/bin/cmsystem
/usr/bin/cmuser
/usr/lib/conmen/*[!~]
#%{_menudir}/%{name}
/var/lib/conmen

