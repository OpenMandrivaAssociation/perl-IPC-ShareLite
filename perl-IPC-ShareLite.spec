%define module  IPC-ShareLite
%define version 0.09
%define release %mkrel 4
%define	pdir	IPC
%define pname   ShareLite


Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.bz2
Url: 		http://search.cpan.org/search?dist=IPC-ShareLite
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Requires: 	perl
BuildRequires:	perl-devel >= 5.8.0

%description
IPC-ShareLite module for perl.  IPC::ShareLite provides a simple
interface to shared memory, allowing data to be efficiently
communicated between processes.  Your operating system must support
SysV IPC (shared memory and semaphores) in order to use this module.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
make OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=%{prefix}
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README TODO
%{_mandir}/*/*
%dir %{perl_vendorlib}/*/auto/IPC/ShareLite
%attr(755,root,root) %{perl_vendorlib}/*/auto/IPC/ShareLite/ShareLite.so
%{perl_vendorlib}/*/auto/IPC/ShareLite/autosplit.ix
%dir %{perl_vendorlib}/*/IPC
%{perl_vendorlib}/*/IPC/ShareLite.pm

