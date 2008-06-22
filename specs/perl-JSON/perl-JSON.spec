# $Id$
# Authority: dries
# Upstream: Makamaka Hannyaharamitu <makamaka$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON

Summary: Converts Perl data to and from JavaScript Object Notation
Name: perl-JSON
Version: 1.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON/

Source: http://www.cpan.org/modules/by-module/JSON/JSON-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: dos2unix
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate. It is based on a subset of the JavaScript Programming Language,
Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is

completely language independent but uses conventions that are familiar to
programmers of the C-family of languages, including C, C++, C#, Java,
JavaScript, Perl, Python, and many others. These properties make JSON an
ideal data-interchange language.

This module converts between JSON (JavaScript Object Notation) and Perl data
structure into each other. For JSON, see http://www.json.org/

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Apache::JSONRPC.3pm*
%doc %{_mandir}/man3/JSON.3pm*
%doc %{_mandir}/man3/JSON::*.3pm*
%doc %{_mandir}/man3/JSONRPC.3pm*
%doc %{_mandir}/man3/JSONRPC::*.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/JSONRPC.pm
%{perl_vendorlib}/JSON/
%{perl_vendorlib}/JSON.pm
%{perl_vendorlib}/JSONRPC/
%{perl_vendorlib}/JSONRPC.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Sun Sep 03 2006 Al Pacifico < adpacifico@users.sourceforge.net> - 1.07-1
- Initial packaging.