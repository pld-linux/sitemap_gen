Summary:	Google Sitemap Generator
Summary(pl.UTF-8):	Generator Sitemap z google
Name:		sitemap_gen
Version:	1.5
Release:	1
License:	BSD
Group:		Applications
Source0:	http://sitemap-generators.googlecode.com/files/%{name}_%{version}.tar.gz
# Source0-md5:	98754e802722c0cc2ffcc8aedead67b6
URL:		http://code.google.com/p/sitemap-generators/
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Google Sitemap Generator is a Python script that creates a Sitemap
for your site using the Sitemap Protocol. This script can create
Sitemaps from URL lists, web server directories, or from access logs.

%description -l pl.UTF-8
Skrypt Google Sitemap Generator to skrypt w języku Python, służący do
tworzenia mapy witryny przy użyciu protokołu Sitemap Protocol. Skrypt
umożliwia tworzenie map witryn z list adresów URL, katalogów serwerów
internetowych lub dzienników dostępu.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

install sitemap_gen.py $RPM_BUILD_ROOT%{_bindir}
install example* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
