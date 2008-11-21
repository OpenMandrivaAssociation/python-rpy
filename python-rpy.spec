%define module rpy
%define r_version 2.8.0
%define _requires_exceptions libR.so

%define rel rc1

Summary:	A very simple, yet robust, Python interface to the R Programming Language
Name:		python-%{module}
Version:	2.0.0
Release:	%mkrel -c %{rel} 1
Group:		Development/Python
License:	BSD-like
URL:		http://rpy.sourceforge.net/
Source0:	http://osdn.dl.sourceforge.net/sourceforge/%{module}/%{module}2-%{version}%{rel}.tar.gz
Requires:	R-base = %{r_version}
Requires:	python-numpy
BuildRequires:	R-base = %{r_version}
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel
BuildRequires:	tetex-latex
BuildRequires:	texinfo
BuildRequires:	lapack-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -qn %{module}2-%{version}%{rel}

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

#pushd doc
#make all
#popd

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --record=INSTALLED_FILES

# install info
#mkdir -p %{buildroot}%{_datadir}/info
#cp doc/rpy.info %{buildroot}%{_datadir}/info/

%clean
rm -rf %{buildroot}

%post
#%_install_info rpy.info

%preun
#%_remove_install_info rpy.info

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc NEWS README
#%attr(755,root,root) %{py_platsitedir}/_rpy*.so
#%{py_platsitedir}/rpy-*py2.5.egg-info
#%{py_platsitedir}/rpy.py
#%{py_platsitedir}/rpy.pyc
#%{py_platsitedir}/rpy.pyo
#%{py_platsitedir}/rpy_io.py
#%{py_platsitedir}/rpy_io.pyc
#%{py_platsitedir}/rpy_io.pyo
#%attr(755,root,root) %{py_platsitedir}/rpy_options.py
#%{py_platsitedir}/rpy_options.pyc
#%{py_platsitedir}/rpy_options.pyo
#%{py_platsitedir}/rpy_tools.py
#%{py_platsitedir}/rpy_tools.pyc
#%{py_platsitedir}/rpy_tools.pyo
#%{py_platsitedir}/rpy_version.py
#%{py_platsitedir}/rpy_version.pyc
#%{py_platsitedir}/rpy_version.pyo
#%{py_platsitedir}/rpy_wintools.py
#%{py_platsitedir}/rpy_wintools.pyc
#%{py_platsitedir}/rpy_wintools.pyo
#%{_datadir}/info/*
