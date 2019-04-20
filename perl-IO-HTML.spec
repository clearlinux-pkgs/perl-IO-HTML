#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-HTML
Version  : 1.001
Release  : 26
URL      : http://search.cpan.org/CPAN/authors/id/C/CJ/CJM/IO-HTML-1.001.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/C/CJ/CJM/IO-HTML-1.001.tar.gz
Summary  : 'Open an HTML file with automatic charset detection'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-HTML-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
IO-HTML version 1.001, released June 28, 2014
This module opens a file and performs automatic charset detection
based on the HTML5 algorithm.  You can then pass the filehandle to
HTML::Parser or a related module (or just read it yourself).

%package dev
Summary: dev components for the perl-IO-HTML package.
Group: Development
Provides: perl-IO-HTML-devel = %{version}-%{release}

%description dev
dev components for the perl-IO-HTML package.


%package license
Summary: license components for the perl-IO-HTML package.
Group: Default

%description license
license components for the perl-IO-HTML package.


%prep
%setup -q -n IO-HTML-1.001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-HTML
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-HTML/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/IO/HTML.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::HTML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-HTML/LICENSE
