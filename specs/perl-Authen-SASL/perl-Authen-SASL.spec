# $Id$
# Authority: dries
# Upstream: Graham Barr <gbarr$pobox,com>

%{?el3:%define _without_gssapi 1}
%{?rh9:%define _without_gssapi 1}
%{?rh7:%define _without_gssapi 1}
%{?el2:%define _without_gssapi 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-SASL

Summary: SASL Authentication framework
Name: perl-Authen-SASL
Version: 2.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-SASL/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-SASL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Digest::HMAC_MD5)
BuildRequires: perl(ExtUtils::MakeMaker)
%{!?_without_gssapi:BuildRequires: perl(GSSAPI)}
Requires: perl >= 0:5.005

%description
This module permits authentication with SASL.

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
%doc Changes MANIFEST META.yml SIGNATURE api.txt example_pl
%doc %{_mandir}/man3/Authen::SASL.3pm*
%doc %{_mandir}/man3/Authen::SASL::*.3pm*
%dir %{perl_vendorlib}/Authen/
%{perl_vendorlib}/Authen/SASL/
%{perl_vendorlib}/Authen/SASL.pm
%{perl_vendorlib}/Authen/SASL.pod

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.11-1
- Updated to release 2.11.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Updated to release 2.09.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Initial package.
