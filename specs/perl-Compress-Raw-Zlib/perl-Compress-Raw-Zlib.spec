# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Raw-Zlib

Summary: Low-Level Interface to zlib compression library
Name: perl-Compress-Raw-Zlib
Version: 2.010
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Raw-Zlib/

Source: http://www.cpan.org/modules/by-module/Compress/Compress-Raw-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Low-Level Interface to zlib compression library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Compress::Raw::Zlib.3pm*
%dir %{perl_vendorarch}/auto/Compress/
%dir %{perl_vendorarch}/auto/Compress/Raw/
%{perl_vendorarch}/auto/Compress/Raw/Zlib/
%dir %{perl_vendorarch}/Compress/
%dir %{perl_vendorarch}/Compress/Raw/
%{perl_vendorarch}/Compress/Raw/Zlib.pm

%changelog
* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 2.010-1
- Updated to release 2.010.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.009-1
- Updated to release 2.009.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.008-1
- Updated to release 2.008.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 2.006-1
- Updated to release 2.006.

* Wed Aug 08 2007 Dag Wieers <dag@wieers.com> - 2.005-1
- Updated to release 2.005.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.