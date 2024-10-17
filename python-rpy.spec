%define module rpy
%define r_version 2.8.1

Epoch:		1
Summary:	A very simple, yet robust, Python interface to the R Programming Language
Name:		python-%{module}
Version:	1.0.3
Release:	4
Group:		Development/Python
License:	BSD-like
URL:		https://rpy.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
Requires:	R-base >= %{r_version}
Requires:	python-numpy
BuildRequires:	R-base >= %{r_version}
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel
BuildRequires:	tetex-latex
BuildRequires:	texinfo
BuildRequires:	lapack-devel
BuildRequires:	pkgconfig(libR)

# First build failure in from src/RPy.h
# http://www.mail-archive.com/rpy-list@lists.sourceforge.net/msg01500.html
# Remaining just a cut&paste from rpy2's setup.py
Patch0:		rpy-1.0.3-R-base-2.8+.patch
Patch1:		rpy-1.0.3-R-version.patch

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
%setup -qn %{module}-%{version}

%patch0 -p1
%patch1 -p1

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

#pushd doc
#make all
#popd

%install
PYTHONDONTWRITEBYTECODE= \
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --record=INSTALLED_FILES

# install info
#mkdir -p %{buildroot}%{_datadir}/info
#cp doc/rpy.info %{buildroot}%{_datadir}/info/

%post
#%_install_info rpy.info

%preun
#%_remove_install_info rpy.info

%files -f INSTALLED_FILES
%doc NEWS README
