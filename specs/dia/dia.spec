# $Id$
# Authority: dag

Summary: Diagram drawing program
Name: dia
Version: 0.96.1
Release: 1
Epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.gnome.org/projects/dia/

#Source: http://ftp.gnome.org/pub/gnome/sources/dia/%{version}/dia-%{version}.tar.bz2
Source: http://ftp.gnome.org/pub/gnome/sources/dia/0.96/dia-%{version}.tar.bz2
Patch1: dia-0.92.2-dtd.patch
Patch2: dia-0.95-pre6-help.patch
Patch3: dia-0.94-fallbacktoxpmicons.patch
Patch4: dia-0.96-python-detect.patch
Patch5: dia-0.96.1-64bit.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.6, gtk2-devel >= 2.6, libxml2-devel >= 2.3.9
BuildRequires: libgnome-devel >= 2.0, libgnomeui-devel >= 2.0, pango-devel >= 1.1.5
BuildRequires: libart_lgpl-devel >= 2.3.10, libxslt-devel, libpng-devel
BuildRequires: python-devel >= 2.2.1, pygtk2-devel, gcc-c++, gettext, pkgconfig >= 0.9
BuildRequires: intltool, perl(XML::Parser), gettext, PyXML, docbook-style-xsl
%{?el4:BuildRequires: gcc-g77}
%{?fc5:BuildRequires: gcc-gfortran}
%{?fc4:BuildRequires: gcc-gfortran}
%{?fc3:BuildRequires: gcc-g77}

%description
The Dia drawing program is designed to be like the Microsoft(R) Visio
program. Dia can be used to draw different types of diagrams, and
includes support for UML static structure diagrams (class diagrams),
entity relationship modeling, and network diagrams. Dia can load and
save diagrams to a custom file format, can load and save in .xml
format, and can export to PostScript(TM).

%prep
%setup
%patch1 -p1 -b .dtd
%patch2 -p1 -b .help
%patch3 -p1 -b .fallbacktoxpmicons
%patch4 -p1 -b .py-detect
%patch5 -p1 -b .64bit

%build
%configure \
	--enable-db2html \
	--enable-gnome \
	--with-python
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Clean up buildroot
#{__rm} -f %{buildroot}%{_libdir}/dia/*.la

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ KNOWN_BUGS NEWS README THANKS TODO
%doc %{_datadir}/gnome/help/dia/
%doc %{_mandir}/man?/*
%{_bindir}/dia
%{_datadir}/applications/dia.desktop
%{_datadir}/dia/
%{_datadir}/mime-info/dia.keys
%{_datadir}/mime-info/dia.mime
%{_datadir}/pixmaps/dia-diagram.png
%{_datadir}/pixmaps/dia_gnome_icon.png
%{_libdir}/dia/

%changelog
* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 0.96.1-1.
- Updated to release 0.96.1.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Updated to release 0.95.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.94-1.
- Updated to release 0.94.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 0.93-1.
- Updated to release 0.93.

* Sun Nov 09 2003 Dag Wieers <dag@wieers.com> - 0.92.2-1
- Fixed the "Couldn't find standard objects..." error. (Krzysztof Leszczynski)

* Sat Nov 01 2003 Dag Wieers <dag@wieers.com> - 0.92.2-0
- Updated to release 0.92.2.

* Sun Oct 26 2003 Dag Wieers <dag@wieers.com> - 0.92.1-0
- Updated to release 0.92.1.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 0.92-0
- Updated to release 0.92.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 0.92-0-pre3
- Updated to release 0.92-pre3.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Thu Jan 3 2003 Dag Wieers <dag@wieers.com> - 0.90.20030131-0
- Initial package. (using DAR)