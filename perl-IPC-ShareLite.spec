%define upstream_name    IPC-ShareLite
%define upstream_version 0.17

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	3

Summary: 	Lightweight interface to shared memory
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel >= 5.8.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
IPC-ShareLite module for perl.  IPC::ShareLite provides a simple
interface to shared memory, allowing data to be efficiently
communicated between processes.  Your operating system must support
SysV IPC (shared memory and semaphores) in order to use this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
