%define         shortname       authlibsmb
Summary:	Library to SMB authentication for muddleftpd
Summary(pl):	Biblioteka do autentykacji SMB dla muddleftpd
Name:		muddleftpd-authlibsmb
Version:	0.1
Release:	2
License:	GPL
Group:		Daemons
Source0:	http://www.arach.net.au/~wildfire/muddleftpd/modules/%{shortname}-%{version}.tar.gz
URL:		http://www.muddleftpd.cx/
BuildRequires:	autoconf
Requires:	muddleftpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir		%{_libdir}/muddle

%description
This module allows muddleftpd authenticate using a SMB server.

%description -l pl
Ten moduł pozwala muddleftpd autentykować użytkowników korzystając z
serwera SMB.

%prep
%setup -q -n %{shortname}-%{version}

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D libauthsmb.so $RPM_BUILD_ROOT%{_pkglibdir}/libauthsmb.so

gzip -9nf AUTHORS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(750,root,root) %{_pkglibdir}/libauthsmb.so
