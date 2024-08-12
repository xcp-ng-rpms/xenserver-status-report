%global package_speccommit 6c63345c01862cd28cbfed03f9118635a1b79e4e
%{!?xsrel: %global xsrel 2}

Summary:        A program that generates status reports for a XenServer host
Name:           xenserver-status-report
Version:        2.0.5
Release:        %{?xsrel}%{?dist}
License:        GPLv2+
%global repo    https://code.citrite.net/rest/archive/latest/projects/XSU/repos/status-report
%global file    archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}.tar.gz
Source0: xenserver-status-report.tar.gz
BuildArch:      noarch
%if 0%{?xenserver} < 9
BuildRequires:  help2man
%endif
BuildRequires:  python-defusedxml
# Same code is used for XS8/python2 and XS9/python3
# we disable the shebang check here
%global __brp_mangle_shebangs %nil

# Keep in sync with the External Programs list.
Requires:       acpica-tools
Requires:       arptables
Requires:       biosdevname
Requires:       bridge-utils
Requires:       chkconfig
Requires:       chrony
Requires:       coreutils
Requires:       device-mapper
Requires:       device-mapper-multipath
Requires:       dmidecode
Requires:       ebtables
Requires:       efibootmgr
Requires:       ethtool
%if 0%{?xenserver} < 9
Requires:       fcoe-utils
%endif
Requires:       gzip
Requires:       hdparm
Requires:       iproute
Requires:       iproute-tc
Requires:       iptables
Requires:       iscsi-initiator-utils
Requires:       kmod
Requires:       kpatch
%if 0%{?xenserver} < 9
Requires:       lldpad
%endif
Requires:       lvm2
Requires:       mdadm
Requires:       net-tools
Requires:       openvswitch
Requires:       pciutils
Requires:       procps-ng
Requires:       python-defusedxml
Requires:       sg3_utils
Requires:       systemd
Requires:       util-linux
Requires:       xapi-core
Requires:       xapi-xe
Requires:       xen-dom0-tools
Requires:       xenopsd-xc
Requires:       xen-tools

%define bin0_name xen-bugtool

%description
The %{name} package collects various system configuration and state to aid in
diagnosing issues.

%prep
%autosetup -p1

%build
%install
install -m 755 -d %{buildroot}/%{_sbindir}
install -m 755 -p %{bin0_name} %{buildroot}/%{_sbindir}
ln %{buildroot}/%{_sbindir}/%{bin0_name} \
   %{buildroot}/%{_sbindir}/%{name}

%if 0%{?xenserver} < 9
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
%endif

%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_sbindir}/%{bin0_name}
%if 0%{?xenserver} < 9
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_mandir}/man1/%{bin0_name}.1.gz
%endif

%changelog
* Mon Jun 24 2024 Bernhard Kaindl <bernhard.kaindl@cloud.com> - 2.0.5-2
- CP-49659:  Fix collecting kernel module infos with non-latin strings
- CA-394409: Fix collecting logs for HW certification and tapdisk

* Thu May 16 2024 Deli Zhang <deli.zhang@cloud.com> - 2.0.4-2
- CP-46076: On XS9, no longer require the FCoE and lldpad packages

* Tue Mar 26 2024 Lin Liu <Lin.Liu01@cloud.com> - 2.0.4-1
- CP-48613: Build with XS9
- Fixes for error handling and error logging

* Thu Feb 22 2024 Bernhard Kaindl <bernhard.kaindl@cloud.com> - 2.0.3-1
- CA-389135: Fix saving RRDs using the hidden --entries=persistent-stats flag
- CA-389176: Fix collecting the /var/log/xcp-rrdd-plugin logs when --all is used
- CA-389177: Fix interactive yes/no question mode (if --yestoall is not passed)

* Wed Feb 14 2024 Bernhard Kaindl <bernhard.kaindl@cloud.com> - 2.0.1-1
- CA-388587: Update to collect the latest xapi-clusterd database

* Tue Jan 30 2024 Deli Zhang <deli.zhang@cloud.com> - 2.0.0-2
- CP-47448: Fix release number in koji

* Fri Jan 26 2024 Deli Zhang <deli.zhang@cloud.com> - 2.0.0-1
- CP-44440: Collect SNMP config files
- CP-41819: Partial python3 support

* Thu Oct 19 2023 Bernhard Kaindl <bernhard.kaindl@cloud.com> - 1.3.14-1
- CA-383852: Fix output from `sar -A`, move `sar` to `cap(system-load)`

* Tue Oct  3 2023 Bernhard Kaindl <bernhard.kaindl@cloud.com> - 1.3.13-1
- CP-45506: Also add testcase for the subarchive at etc/systemd.tar
- CP-45506: Archive /etc/systemd as a tar archive inside the output

* Tue Sep 26 2023 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.3.12-1
- CA-378768: capture block schedulers
- Capture the contents of the cron dirs
- CP-41107: Store bug tool log in status report
- CP-43806: Collect `xen-cpuid -p`
- Collect customised multipath configuration
- Remove obsolete MPP from bugtool
- CP-42688: Collect NRPE config files
- XSI-1385: Collect plain text (human-readable) SAR file reports

* Wed May 10 2023 Xueqing Zhang <xueqing.zhang@citrix.com> - 1.3.11-1
- CP-42688: Collect NRPE config files

* Tue Apr 18 2023 Lin Liu <lin.liu@citrix.com> - 1.3.10-1
- Fix up some legacy configuration files

* Wed Mar 22 2023 Xueqing Zhang <xueqing.zhang@citrix.com> - 1.3.9-1
- CP-41620: Update status report to collect telemetry logs

* Thu Sep 22 2022 Lin Liu <lin.liu@citrix.com> - 1.3.8-1
- CA-369805: EFI-variables in snapshot data is not filtered

* Fri Sep 16 2022 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.3.7-1
- CP-38441: Add bugtool support for vTPM
- CA-369841: XSI-1298 xen-bugtool command takes over 1 hour to collect xenserver-databases

* Tue Apr 12 2022 Lin Liu <lin.liu@citrix.com> - 1.3.6-1
- CA-355588: Include AD users and groups in the bugtool

* Thu Nov 25 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.3.5-1
- CP-38679: Include /proc/xsversion in the bugtool

* Wed Sep 29 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.3.4-1
- CA-358870: Removed filename parameter and usage from func_output to fix error in the unclustered case
- CA-358870: added exception to prevent file not found error in the unclusterd case

* Tue Sep 14 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.3.3-1
- CA-355820: Filter out cluster_token from bugtool

* Fri May 28 2021 Lin Liu <lin.liu@citrix.com> - 1.3.2-1
- CP-36092: Collect samba winbind info and logs

* Fri May 07 2021 Mark Syms <mark.syms@citrix.com> - 1.3.1-1
- CA-353772: Add capture of iSCSI iface information

* Thu Feb 18 2021 Andrew Cooper <andrew.cooper3@citrix.com> - 1.3.0-1
- Fix multiple pylint error/warnings
- Drop collection of obsolete logfiles
- Correct the build and runtime dependencies

* Thu Jan 28 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.9-1
- CA-350866: Remove bugtool-conn-tests package

* Wed Dec 23 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.8-1
- CA-350311: Capture chrony information in bugtool

* Wed Jun 24 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2.7-2
- CP-35517: Drop busybox as a BuildRequires

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
