%define debug_package %{nil}

Name:		servicenow-mid
Version:	20120718
Release:	1833.3%{?dist}
Summary:	Service Now MID Server

Group:		MID Server Installation
License:	Proprietary
URL:		http://wiki.servicenow.com/index.php?title=MID_Server_Installation
Source0:	http://install.service-now.com/glide/distribution/builds/package/mid/2012/07/18/mid.2012-07-18-1833.linux.x86-32.zip
Patch0:         sysvinit-compability.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
AutoReq: 0

%description
The Management, Instrumentation, and Discovery (MID) Server is a Java
server that runs as a Windows service or UNIX daemon. The MID Server
facilitates communication and movement of data between the ServiceNow
platform and external applications, data sources, and services.

%prep
%setup -q -n agent
%patch0 -p2

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/servicenow-mid %{buildroot}%{_sysconfdir}/init.d/
cp -rv * %{buildroot}/opt/servicenow-mid
ln -s /opt/servicenow-mid/bin/mid.sh %{buildroot}%{_sysconfdir}/init.d/servicenow-mid


%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add servicenow-mid

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service servicenow-mid stop >/dev/null 2>&1
    /sbin/chkconfig --del servicenow-mid
fi

%files
%defattr(-,root,root,-)
%doc
%{_sysconfdir}/init.d/servicenow-mid
/opt/servicenow-mid

%changelog
* Mon Sep 10 2012 Marek Mahut <mmahut@redhat.com> 20120718-1833.2
- Initial build
