%define upstream_name    lib-abs
%define upstream_version 0.93

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Get pathname of current working directory
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/lib/lib-abs-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildArch:	noarch
Provides:	perl(lib::abs)

%description
The main reason of this library is transformate relative paths to absolute
at the 'BEGIN' stage, and push transformed to '@INC'. Relative path basis
is not the current working directory, but the location of file, where the
statement is (caller file). When using common 'lib', relative paths stays
relative to curernt working directory,

	# For ex:
	# script: /opt/scripts/my.pl
	use lib::abs '../lib';

	# We run `/opt/scripts/my.pl` having cwd /home/mons
	# The @INC will contain '/opt/lib';

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.920.0-2mdv2011.0
+ Revision: 656983
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.920.0-1mdv2011.0
+ Revision: 601899
- update to new version 0.92

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.910.0-1mdv2011.0
+ Revision: 512602
- update to 0.91

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.900.0-1mdv2010.0
+ Revision: 398842
- import perl-lib-abs


* Thu Jul 23 2009 cpan2dist 0.90-1mdv
- initial mdv release, generated with cpan2dist

