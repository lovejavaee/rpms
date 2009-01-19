# $Id$
# Authority: Fabian
# Dist: nodist

%define real_name iwlwifi-3945-ucode

Summary: Firmware for Intel Wireless 3945 network adapter
Name: iwl3945-firmware
Version: 15.28.1.8
Release: 1
License: Distributable
Group: System Environment/Kernel
URL: http://intellinuxwireless.org/

Source: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-3945-ucode-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

BuildArch: noarch

%description
This package provides the firmware required for running an Intel
Wireless 3945 adapter with the Linux kernel iwl3945 driver.

%prep
%setup -n %{real_name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 iwlwifi-3945-1.ucode %{buildroot}/lib/firmware/iwlwifi-3945-1.ucode
%{__install} -p -m0644 LICENSE.iwlwifi-3945-ucode %{buildroot}/lib/firmware/LICENSE.iwlwifi-3945-ucode
%{__install} -p -m0644 README.iwlwifi-3945-ucode %{buildroot}/lib/firmware/README.iwlwifi-3945-ucode

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc /lib/firmware/LICENSE.iwlwifi-3945-ucode
%doc /lib/firmware/README.iwlwifi-3945-ucode
/lib/firmware/iwlwifi-3945-1.ucode

%changelog
* Thu Jan 15 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 15.28.1.8-1
- Cosmetic changes for RPMforge integration.

* Fri Jan 02 2009 Philip J Perry <ned at unixmail.co.uk> - 15.28.1.8-1
- Initial RPM package based on 15.28.1.8 iwlwifi 3945 firmware.