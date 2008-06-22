# $Id$
# Authority: dries
# Upstream: J. J. Merelo-Guerv&#243;s <jmerelo%20(at)%20geneura,ugr,es>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Evolutionary

Summary: Performs paradigm-free evolutionary algorithms
Name: perl-Algorithm-Evolutionary
Version: 0.54
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Evolutionary/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Evolutionary-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for performing paradigm-free evolutionary algorithms.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Algorithm/Evolutionary.pm
%{perl_vendorlib}/Algorithm/Evolutionary/*

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.53-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.