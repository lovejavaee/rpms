# $Id$
# Authority: dries
# Upstream: Ken Fox <kfox$vulpes,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Units

Summary: Unit conversion
Name: perl-Math-Units
Version: 1.2
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Units/

Source: http://www.cpan.org/modules/by-module/Math/Math-Units-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is Math::Units, the first official release of a powerful
unit conversion system written completely in Perl.  This module
has been tested fairly well using the GNU units program as a
baseline.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Units.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.