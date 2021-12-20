Summary:        A program that generates status reports for a XenServer host
Name:           xenserver-status-report
Version:        1.2.10
Release:        1%{?dist}
License:        GPLv2+

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-status-report/archive?at=v1.2.10&format=tar.gz&prefix=xenserver-status-report-1.2.10#/xenserver-status-report.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-status-report/archive?at=v1.2.10&format=tar.gz&prefix=xenserver-status-report-1.2.10#/xenserver-status-report.tar.gz) = c0cbf93b4944042fe5c637cb81ba5bf1b76093f7

BuildArch:      noarch
BuildRequires:  python-devel xapi-core xen-dom0-tools busybox help2man
Requires:       hdparm, dmidecode, lvm2, bridge-utils, biosdevname, arptables
Requires:       ebtables, ethtool, pciutils, pmtools, sg3_utils, iproute-tc
Obsoletes:      bugtool-conn-tests

%define bin0_name xen-bugtool

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

%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_sbindir}/%{bin0_name}
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_mandir}/man1/%{bin0_name}.1.gz

%changelog
* Mon Aug 30 2021 Lin Liu <lin.liu@citrix.com> - 1.2.10-1
- CP-36092: Backport winbind to Yangtze

* Thu Jan 28 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.9-1
- CA-350866: Remove bugtool-conn-tests extension

* Mon Dec 21 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.8-1
- CA-350311: Capture chrony information in bugtool

* Wed Jun 24 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.7-1
- Fix -u help message to correspond the result
- CA-341602: Calculate start time on per-process basis
- CA-341602: Do not start all of the process groups in parallel

* Fri Jan 24 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.6-2
- Add iproute-tc as a dependency

* Fri Nov 15 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.6-1
- CP-32427 Filter secrets from xapi-db

* Thu Oct 24 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.5-1
- CP-32039: gather NUMA memory information

* Wed Jun 19 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.4-1
- CA-317150: move bugtool plugins before log capture

* Mon Jun 10 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.3-1
- CP-31442: rename the tool to xen-ucode

* Tue May 28 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.2-1
- CP-31376: Improve bugtool filtering

* Wed May 08 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.1-1
- CP-31126: add output of xen-microcode

* Wed Mar 27 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.0-1
- CA-308916: Remove special vncterm coredump handling

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
