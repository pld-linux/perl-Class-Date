%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Date
Summary:	Class for easy date and time manipulation
Name:		perl-%{pdir}-%{pnam}
Version:	1.1.5
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended to provide a general-purpose date and datetime
type for perl. You have a Class::Date class for absolute date and
datetime, and have a Class::Date::Rel class for relative dates.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%{perl_sitearch}/%{pdir}/%{pnam}.pm
%dir %{perl_sitearch}/%{pdir}/%{pnam}
%{perl_sitearch}/%{pdir}/%{pnam}/*.pm
#%dir %{perl_sitearch}/auto/%{pdir} # -- which package should be a Class/ owner?
%dir %{perl_sitearch}/auto/%{pdir}/%{pnam}
%{perl_sitearch}/auto/%{pdir}/%{pnam}/%{pnam}.*
%{_mandir}/man3/*
