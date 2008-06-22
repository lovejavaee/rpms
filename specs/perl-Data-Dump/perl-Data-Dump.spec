# $Id$
# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Dump

Summary: Pretty print data
Name: perl-Data-Dump
Version: 1.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Dump/

Source: http://www.cpan.org/modules/by-module/Data/Data-Dump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package contain the Data::Dump module. It can be used for pretty
printing data.

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
%doc %{_mandir}/man3/Data::Dump.3pm*
%{perl_vendorlib}/Data/Dump.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Jun 15 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.