# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Simple

Summary: Simple parsing of RFC2822 message format and headers
Name: perl-Email-Simple
Version: 2.003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Simple/

Source: http://www.cpan.org/modules/by-module/Email/Email-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module you can parse RFC2822 message format and headers.

This package contains the following Perl module:

    Email::Simple

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::Simple.3pm*
%doc %{_mandir}/man3/Email::Simple::Header.3pm*
%doc %{_mandir}/man3/Email::Simple::Headers.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Simple/
%{perl_vendorlib}/Email/Simple.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 2.003-1
- Updated to release 2.003.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.999-1
- Updated to release 1.999.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.995-1
- Initial package.