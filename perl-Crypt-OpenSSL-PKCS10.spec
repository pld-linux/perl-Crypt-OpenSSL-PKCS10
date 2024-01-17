#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Crypt
%define		pnam	OpenSSL-PKCS10
Summary:	Crypt::OpenSSL::PKCS10 - Perl extension to OpenSSL's PKCS10 API
Name:		perl-%{pdir}-%{pnam}
Version:	0.25
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	90fe7167c0eeb00fb0143aad01107b6a
URL:		http://search.cpan.org/dist/Crypt-OpenSSL-PKCS10/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Crypt-OpenSSL-Guess >= 0.15
%if %{with tests}
BuildRequires:	perl-Pod-Coverage >= 0.19
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::PKCS10 provides the ability to create PKCS10
certificate requests using RSA key pairs.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

rm -rf inc/Module/Install inc/Module/Install.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/%{pdir}/OpenSSL/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/OpenSSL/PKCS10
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/OpenSSL/PKCS10/*.so
%{_mandir}/man3/*
