# $Id$
# Authority: dries
# Upstream: Slaven Rezi&#263; <slaven$rezic,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name GD-Convert

Summary: Additional output formats for GD
Name: perl-GD-Convert
Version: 2.12
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD-Convert/

Source: http://search.cpan.org/CPAN/authors/id/S/SR/SREZIC/GD-Convert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
GD::Convert is a pure perl module which provides additional output
functions for the GD module: ppm and xpm. These formats are useful if
you need to dynamically create photos for Tk. Perl/Tk lesser than
version 804 does not accept any of GD's output formats: png only via
the additional Tk::PNG module and jpeg only via the additional
Tk::JPEG module. So if you cannot compile on your system, this module
is for you.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/GD/Convert.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.12-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Updated to release 2.12.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.11-1
- Initial package.
