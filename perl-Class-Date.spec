%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Date
Summary:	Class for easy date and time manipulation
Summary(pl):	Klasa Perla do ³atwej manipulacji dat± i czasem
Name:		perl-%{pdir}-%{pnam}
Version:	1.1.5
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
This module is intended to provide a general-purpose date and datetime
type for Perl. You have a Class::Date class for absolute date and
datetime, and have a Class::Date::Rel class for relative dates.

%description -l pl
Ten modu³ ma za zadanie udostêpniæ dla Perla typy daty i czasu
ogólnego przeznaczenia. Zawiera klasê Class::Date do bezwzglêdnych dat
i czasu oraz Class::Date::Rel do dat wzglêdnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
