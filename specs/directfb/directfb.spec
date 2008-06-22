# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}
%{?el5:%define _with_sysfs 1}

%define real_name DirectFB
%define real_version 0.9.25

Summary: Hardware graphics acceleration library
Name: directfb
Version: 0.9.25.1
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.directfb.org/

Source: http://www.directfb.org/download/DirectFB/DirectFB-%{version}.tar.gz
Patch0: DirectFB-0.9.25.1-types.patch
Patch1: DirectFB-0.9.25.1-linux-compiler.patch
Patch2: DirectFB-0.9.25.1-ppc.patch
Patch3: DirectFB-0.9.25.1-sysfs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libjpeg-devel, zlib-devel, freetype-devel >= 2.0
BuildRequires: SDL-devel, libtool, gcc-c++, libvncserver-devel
%{?_with_sysfs:BuildRequires: libsysfs-devel}

%description
DirectFB is a thin library that provides hardware graphics acceleration,
input device handling and abstraction, integrated windowing system with
support for translucent windows and multiple display layers on top of the
Linux Framebuffer Device. It is a complete hardware abstraction layer with
software fallbacks for every graphics operation that is not supported by
the underlying hardware. DirectFB adds graphical power to embedded systems
and sets a new standard for graphics under Linux.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: SDL-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1 -b .types
%patch1 -p1 -b .linux-compiler
%patch2 -p1 -b .ppc
%patch3 -p1 -b .sysfs

%build
%configure \
	--disable-dependency-tracking \
	--disable-fast-install \
	--disable-maintainer-mode \
%ifarch x86_64
	--disable-mmx \
%endif
	--enable-fbdev \
	--enable-linux-input \
	--enable-static \
	--enable-video4linux2 \
	--enable-zlib
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up the docs
%{__rm} -f docs/html/Makefile*

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING docs/README.screenshots fb.modes NEWS README
%doc %{_mandir}/man1/dfbg.1*
%doc %{_mandir}/man5/directfbrc.5*
%{_bindir}/dfbg
%{_bindir}/dfbdump
%{_bindir}/dfbinfo
%{_bindir}/dfbinput
%{_bindir}/dfblayer
%{_bindir}/dfbpenmount
%{_bindir}/dfbscreen
%{_bindir}/dfbsummon
%{_datadir}/directfb-%{real_version}/
%dir %{_libdir}/directfb-%{real_version}/
%dir %{_libdir}/directfb-%{real_version}/*/
%dir %{_libdir}/directfb-%{real_version}/*/*/
%{_libdir}/directfb-%{real_version}/*/*.o
%{_libdir}/directfb-%{real_version}/*/*/*.o
%{_libdir}/directfb-%{real_version}/*/*.so
%{_libdir}/directfb-%{real_version}/*/*/*.so
%{_libdir}/libdirect-*.so.*
%{_libdir}/libdirectfb-*.so.*
%{_libdir}/libfusion-*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/html/*
%doc %{_mandir}/man1/directfb-csource.1*
%{_bindir}/directfb-config
%{_bindir}/directfb-csource
%{_includedir}/directfb/
%{_includedir}/directfb-internal/
%dir %{_libdir}/directfb-%{real_version}/
%dir %{_libdir}/directfb-%{real_version}/*/
%dir %{_libdir}/directfb-%{real_version}/*/*/
%{_libdir}/directfb-%{real_version}/*/*.a
%{_libdir}/directfb-%{real_version}/*/*/*.a
%exclude %{_libdir}/directfb-%{real_version}/*/*.la
%exclude %{_libdir}/directfb-%{real_version}/*/*/*.la
%{_libdir}/libdirectfb.a
%{_libdir}/libdirect.a
%{_libdir}/libfusion.a
%exclude %{_libdir}/libdirectfb.la
%exclude %{_libdir}/libdirect.la
%exclude %{_libdir}/libfusion.la
%{_libdir}/libdirectfb.so
%{_libdir}/libdirect.so
%{_libdir}/libfusion.so
%{_libdir}/pkgconfig/direct.pc
%{_libdir}/pkgconfig/directfb.pc
%{_libdir}/pkgconfig/directfb-internal.pc
%{_libdir}/pkgconfig/fusion.pc

%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 0.9.25.1-1
- Updated to release 0.9.25.1.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.24-1
- Updated to release 0.9.24.

* Sun Sep 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.22-1
- Updated to release 0.9.22.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.9.20-1
- Update to 0.9.20.
- Rebuild for Fedora Core 1.

* Mon Jul 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.19.
- Added systems directory, with the SDL plugin in the devel package.
- Removed /etc/fb.modes, which conflicts with the fbset rpm.
- Added libtool hack to get the proper binaries installed.

* Fri Jul 18 2003 Matthias Saou <http://freshrpms.net/>
- Major spec file cleanup... err, rewrite.

* Mon Jan 13 2003 Sven Neumann <neo@directfb.org> 0.9.16
- removed reference to avifile
- added rules for dfbg and its man-page

* Sun Oct 27 2002 Sven Neumann <neo@directfb.org> 0.9.14
- added this file as directfb.spec.in to the DirectFB source tree
- moved directfbrc manpage to the main package

* Fri Aug 23 2002 Götz Waschk <waschk@linux-mandrake.com> 0.9.13-1mdk
- add directfb-csource and man page
- 0.9.13

* Thu Jul 11 2002 Götz Waschk <waschk@linux-mandrake.com> 0.9.12-1mdk
- initial package based on PLD effort
