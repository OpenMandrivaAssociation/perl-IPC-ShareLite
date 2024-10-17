%define upstream_name    IPC-ShareLite
%define upstream_version 0.17

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	5

Summary: 	Lightweight interface to shared memory
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.170.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 555257
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 402564
- update to 0.56

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2009.1
+ Revision: 353646
- update to new version 0.17

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.13-4mdv2009.0
+ Revision: 257384
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.13-3mdv2009.0
+ Revision: 245407
- rebuild

* Mon Mar 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2008.1
+ Revision: 183286
- update to new version 0.13

* Tue Feb 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2008.1
+ Revision: 175334
- new version

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.09-5mdv2008.1
+ Revision: 151372
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.09-4mdv2008.0
+ Revision: 67617
- use %%mkrel


* Tue Nov 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.09-4mdk
- rebuild for new perl

* Wed Jun 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.09-3mdk
- rebuild

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.09-2mdk
- rebuild for new auto{prov,req}

* Fri Apr 25 2003 Fran�ois Pons <fpons@mandrakesoft.com> 0.09-1mdk
- 0.09.

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 0.08-3mdk
- rebuild

* Tue Jul 23 2002 Philippe Libat <philippe@mandrakesoft.com> 0.08-2mdk
- rebuild for perl 5.8.0

* Mon Jun 10 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.08-1mdk
- from Peter Chen <petechen@netilla.com> :
	- 0.08

