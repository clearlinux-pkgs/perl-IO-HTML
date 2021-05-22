#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-HTML
Version  : 1.004
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/C/CJ/CJM/IO-HTML-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CJ/CJM/IO-HTML-1.004.tar.gz
Summary  : 'Open an HTML file with automatic charset detection'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-HTML-license = %{version}-%{release}
Requires: perl-IO-HTML-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
IO-HTML version 1.004, released September 26, 2020
This module opens a file and performs automatic charset detection
based on the HTML5 algorithm.  You can then pass the filehandle to
HTML::Parser or a related module (or just read it yourself).

%package dev
Summary: dev components for the perl-IO-HTML package.
Group: Development
Provides: perl-IO-HTML-devel = %{version}-%{release}
Requires: perl-IO-HTML = %{version}-%{release}

%description dev
dev components for the perl-IO-HTML package.


%package license
Summary: license components for the perl-IO-HTML package.
Group: Default

%description license
license components for the perl-IO-HTML package.


%package perl
Summary: perl components for the perl-IO-HTML package.
Group: Default
Requires: perl-IO-HTML = %{version}-%{release}

%description perl
perl components for the perl-IO-HTML package.


%prep
%setup -q -n IO-HTML-1.004
cd %{_builddir}/IO-HTML-1.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-HTML
cp %{_builddir}/IO-HTML-1.004/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-HTML/e2aa9543be154771b883c9ce3bce00d3add08d5a
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::HTML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-HTML/e2aa9543be154771b883c9ce3bce00d3add08d5a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/IO/HTML.pm
