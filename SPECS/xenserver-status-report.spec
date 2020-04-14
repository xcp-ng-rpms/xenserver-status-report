Summary:        A program that generates status reports for a XenServer host
Name:           xenserver-status-report
Version:        1.1.11
Release:        1
License:        GPLv2+

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-status-report/archive?at=v1.1.11&format=tar.gz&prefix=xenserver-status-report-1.1.11#/xenserver-status-report.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-status-report/archive?at=v1.1.11&format=tar.gz&prefix=xenserver-status-report-1.1.11#/xenserver-status-report.tar.gz) = c89d7e88095ca356e1cc1659db79ed93fff1a797

BuildArch:      noarch
BuildRequires:  python-devel xapi-core xen-dom0-tools busybox help2man
Requires:       hdparm, dmidecode, lvm2, bridge-utils, biosdevname, arptables
Requires:       ebtables, ethtool, pciutils, pmtools, sg3_utils

%define bin0_name xen-bugtool

%define subpackage0_name bugtool-conn-tests
%define subpackage0_destdir %{_sysconfdir}/xensource/bugtool

%description
The %{name} package collects various system configuration and state to aid in
diagnosing issues.

%prep
%autosetup -p1

%install
install -m 755 -d %{buildroot}/%{_sbindir}
install -m 755 -p %{bin0_name} %{buildroot}/%{_sbindir}
ln %{buildroot}/%{_sbindir}/%{bin0_name} \
   %{buildroot}/%{_sbindir}/%{name}

install -m 755 -d %{buildroot}/%{_mandir}/man1
help2man \
    -n 'pack diagnostic information' \
    -s 1 \
    -m 'User Commands' \
    -N \
    -S 'XenServer commands' \
    --version-string=%{version} \
    -o %{buildroot}/%{_mandir}/man1/%{bin0_name}.1 \
    ./%{bin0_name}

chmod 644 %{buildroot}/%{_mandir}/man1/%{bin0_name}.1
ln %{buildroot}/%{_mandir}/man1/%{bin0_name}.1 \
   %{buildroot}/%{_mandir}/man1/%{name}.1

# *** bugtool-conn-tests ***
install -m 755 -d %{buildroot}/%{subpackage0_destdir}/conntest
install -m 666 \
    ext/%{subpackage0_name}/config/conntest.xml \
    %{buildroot}%{subpackage0_destdir}
install -m 666 \
    ext/%{subpackage0_name}/config/conntest/* \
    %{buildroot}%{subpackage0_destdir}/conntest
# *** end ***

%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_sbindir}/%{bin0_name}
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_mandir}/man1/%{bin0_name}.1.gz

# *** bugtool-conn-tests ***
%package -n %{subpackage0_name}
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-status-report/archive?at=v1.1.11&format=tar.gz&prefix=xenserver-status-report-1.1.11#/xenserver-status-report.tar.gz) = c89d7e88095ca356e1cc1659db79ed93fff1a797
# 'Version' inherited from 'xenserver-status-report'
Summary: Plugins for the XenServer bugtool to collect connectivity information

%description -n %{subpackage0_name}
The %{name} package includes extensions for XenServer's bugtool to gather info
on the connectivity status.

%files -n %{subpackage0_name}
%defattr(-,root,root,-)
%{subpackage0_destdir}/*
# *** end ***

%changelog
* Fri Apr 03 2020 Igor Druzhinin <igor.druzhinin@citrix.com> - 1.1.11-1
- CP-31376: Improve bugtool filtering

* Fri Sep 28 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.1.10-1
- CP-28674: remove EFI variables from bugtool

* Fri Jul 27 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.1.9-1
- CP-28674 remove variables from bugtool
- Revert "CP-28674 remove variables from bugtool"
- CA-294376: delete xcp-networkd.log and v6d.log from the bugtool

* Fri Jul 06 2018 Yang Qian <yang.qian@citrix.com> - 1.1.8-1
- CA-292788: Ignore and print nonexistent pid when collecting fd usage
- CA-292788: Print traceback when catching exception

* Wed Sep 20 2017 Simon Rowe <simon.rowe@citrix.com> - 1.1.7-1
- CP-23836: Dump the multicast table of OVS to XenServer Status Report

* Tue Aug 22 2017 Simon Rowe <simon.rowe@citrix.com> - 1.1.6-1
- refine indentation

* Wed Jul 26 2017 Simon Rowe <simon.rowe@citrix.com> - 1.1.5-1
- Change DHCP_LEASE_DIR to /var/lib/xcp/dhclient

* Wed Jun 28 2017 Simon Rowe <simon.rowe@citrix.com> - 1.1.4-1
- Clean up the repo

* Tue May 16 2017 Simon Rowe <simon.rowe@citrix.com> - 1.1.3-1
- Exclude crash coredump files from a report
- CP-21737: Add more info to collect

* Tue Apr 11 2017 Simon Rowe <simon.rowe@citrix.com> - 1.1.2-1
- CA-248105: Capture buddyinfo in bugtool
- CA-248105: Capture NIC queue information

* Fri Aug 05 2016 Kostas Ladopoulos <konstantinos.ladopoulos@citrix.com>
- bugtool-conn-tests is built as a subpackage of xenserver-status-report

* Thu Jul 11 2013 Frediano Ziglio <frediano.ziglio@citrix.com>
- First packaged version
