# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Multiplex

Summary: IO-Multiplex module for perl
Name: perl-IO-Multiplex
Version: 1.09
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Multiplex/

Source: http://www.cpan.org/modules/by-module/IO/IO-Multiplex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
IO-Multiplex module for perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/IO/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-2.2
- Rebuild for Fedora Core 5.

* Sun Feb 20 2005 Dag Wieers <dag@wieers.com> - 1.08-2
- Cosmetic changes.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.04-0
- Initial package. (using DAR)