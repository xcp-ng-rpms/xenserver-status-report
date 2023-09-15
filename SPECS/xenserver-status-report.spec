%global package_speccommit 45a979d910c567caef49972b6e1685c3d332b760
%global package_srccommit v1.3.11

Summary:        A program that generates status reports for a XenServer host
Name:           xenserver-status-report
Version:        1.3.11
Release:        1%{?xsrel}%{?dist}
License:        GPLv2+
Source0: xenserver-status-report.tar.gz
BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python-defusedxml

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
Requires:       fcoe-utils
Requires:       gzip
Requires:       hdparm
Requires:       iproute
Requires:       iproute-tc
Requires:       iptables
Requires:       iscsi-initiator-utils
Requires:       kmod
Requires:       kpatch
Requires:       lldpad
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
