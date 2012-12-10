#This is NOT a relocatable package
%define name conmen
%define version 0.3.020804
%define release %mkrel 8

Summary:   Console menuscripts for Linux
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.tar.bz2
License:   GPL
Group:     Shells
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.020804-8mdv2011.0
+ Revision: 617415
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.3.020804-7mdv2010.0
+ Revision: 424942
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.020804-6mdv2009.0
+ Revision: 243625
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.3.020804-4mdv2008.1
+ Revision: 131587
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import conmen


* Wed Feb 02 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.3.020804-4mdk
- rebuild

* Mon Dec 22 2003 David Baudens <baudens@mandrakesoft.com> 0.3.020804-3mdk
- Remove menu entries

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3.020804-2mdk
- rebuild

* Wed Oct 02 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.3.020804-1mdk
- from Max Heijndijk <cchq@wanadoo.nl> :
	- Upgrade to 0.3.020804

* Fri Aug 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.221-1mdk
- updated to 0.3.221

* Sat Nov 11 2000 Max Heijndijk <cchq@wanadoo.nl> 0.25-1mdk
- Upgrade to 0.25

* Fri Nov 10 2000 Max Heijndijk <cchq@wanadoo.nl> 0.24-1mdk
- Upgrade to 0.24
- Removed /usr/X11R6/bin/xmen

* Wed Nov 8 2000 Max Heijndijk <cchq@wanadoo.nl> 0.23-1mdk
- Upgrade to 0.23

* Wed Oct 11 2000 Max Heijndijk <cchq@wanadoo.nl> 0.22-1mdk
- Upgrade to 0.22

* Tue Aug 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2-2mdk
- BM

* Tue Aug 22 2000 Max Heijndijk <cchq@wanadoo.nl> 0.21-1mdk
- Upgrade to 0.21
- Added menu entryfile

* Wed Jun 28 2000 Max Heijndijk <cchq@wanadoo.nl> 0.2-2mdk
- Added requirement for bash >= 2.0

* Wed Jun 21 2000 Max Heijndijk <cchq@wanadoo.nl> 0.2-1mdk
- Upgraded to 0.2
- Made spec more readable

* Mon May 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1-1mdk
- clean spec
- used srpm provided by Max Heijndijk <cchq@wanadoo.nl>
