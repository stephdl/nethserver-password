Summary: NethServer configuration for password policies
Name: nethserver-password
Version: 1.0.2
Release: 2%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

AutoReq: no
Requires: nethserver-directory


%description
NethServer configuration for password policies

%prep
%setup

%post

echo "
 Hi

 All my development work is done in my free time and from my own expenses. 
 If you consider my work as something helpful, thank you to kindly make 
 a donation to my paypal account and allow me to continue paying my server 
 and all associated costs.

 https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZPK8FKHVT4TY8

 Thank in advance.
 
 Stephane de Labrusse Alias Stephdl
"

%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun May 3 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.2-2-ns6
- disclamer

* Sun Apr 12 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.2-1-ns6
- The password policy for ibays has been removed since obsoleted

* Mon Apr 6 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-1-ns6
- Action created to merge PassExpire2yes with user-{modify,create}

* Sat Apr 4 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-5-ns6
- Initial release
