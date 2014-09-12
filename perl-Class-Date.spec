#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Date
Summary:	Perl Class for easy date and time manipulation
Summary(pl.UTF-8):	Klasa Perla do łatwej manipulacji datą i czasem
Name:		perl-Class-Date
Version:	1.1.10
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d9f305bf7cf5a1ca67354339e2fff5d5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
This module is intended to provide a general-purpose date and datetime
type for Perl. You have a Class::Date class for absolute date and
datetime, and have a Class::Date::Rel class for relative dates.

%description -l pl.UTF-8
Ten moduł ma za zadanie udostępnić dla Perla typy daty i czasu
ogólnego przeznaczenia. Zawiera klasę Class::Date do bezwzględnych dat
i czasu oraz Class::Date::Rel do dat względnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%dir %{perl_vendorarch}/%{pdir}/%{pnam}
%{perl_vendorarch}/%{pdir}/%{pnam}/*.pm
#%dir %{perl_vendorarch}/auto/%{pdir} # -- which package should be a Class/ owner?
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.*
%{_mandir}/man3/*
