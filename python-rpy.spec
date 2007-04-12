%define module	rpy
%define r_version 2.3.1

Name:           python-%{module}
Version:        1.0
Release:        %mkrel 0.rc1.1
Summary:        A very simple, yet robust, Python interface to the R Programming Language
Group:          Development/Python
License:        BSD-like
URL:            http://rpy.sourceforge.net/
Source0:        http://osdn.dl.sourceforge.net/sourceforge/%{module}/%{module}-%{version}-RC1.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	R-base = %{r_version}
BuildRequires:  R-base = %{r_version}
BuildRequires:  python-devel
BuildRequires:	tetex-latex
BuildRequires:	texinfo

%description
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary R
functions (including the graphic functions). All errors from the R language
areconverted to Python exceptions. Any module installed for the R system can
be used from within Python. 

This code is inspired by RSPython from the Omegahat project. The main goals of
RPy are: 
 + to have a very robust interface for using R from Python 
 + the interface should be as transparent and easy to use as possible 
 + it should be usable for real scientific and statistical computations
 

%prep
%setup -n %{module}-%{version}-RC1 -q


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

(
 cd doc
 make all
)

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# install info
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/info
cp doc/rpy.info $RPM_BUILD_ROOT/%{_datadir}/info/


%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info rpy.info

%preun
%_remove_install_info rpy.info

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*
%{_datadir}/info/*
%doc NEWS README TODO examples/ doc/rpy_html doc/rpy.pdf



