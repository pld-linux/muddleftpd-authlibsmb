%define         shortname       authlibsmb
Summary:	Library to SMB authentication for muddleftpd
Summary(pl.UTF-8):   Biblioteka do autentykacji SMB dla muddleftpd
Name:		muddleftpd-authlibsmb
Version:	0.1
Release:	3
License:	GPL
Group:		Daemons
Source0:	http://www.arach.net.au/~wildfire/muddleftpd/modules/%{shortname}-%{version}.tar.gz
# Source0-md5:	fa435f6d955235e17e1569c079c25e15
URL:		http://www.arach.net.au/~wildfire/muddleftpd/
BuildRequires:	autoconf
Requires:	muddleftpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir		%{_libdir}/muddle

%description
This module allows muddleftpd authenticate using a SMB server.

%description -l pl.UTF-8
Ten moduł pozwala muddleftpd autentykować użytkowników korzystając z
serwera SMB.

%prep
%setup -q -n %{shortname}-%{version}

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D libauthsmb.so $RPM_BUILD_ROOT%{_pkglibdir}/libauthsmb.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%attr(750,root,root) %{_pkglibdir}/libauthsmb.so
