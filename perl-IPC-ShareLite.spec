%define module  IPC-ShareLite
%define name    perl-%{module}
%define version 0.13
%define release %mkrel 1


Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Lightweight interface to shared memory
License: 	GPL or Artistic
Group: 		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/IPC/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.8.0
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
IPC-ShareLite module for perl.  IPC::ShareLite provides a simple
interface to shared memory, allowing data to be efficiently
communicated between processes.  Your operating system must support
SysV IPC (shared memory and semaphores) in order to use this module.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
make CFLAGS="%{optflags}"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorarch}/auto/IPC
%{perl_vendorarch}/IPC
