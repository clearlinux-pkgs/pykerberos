#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pykerberos
Version  : 1.2.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/9a/b8/1ec56b6fa8a2e2a81420bd3d90e70b59fc83f6b857fb2c2c37accddc8be3/pykerberos-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9a/b8/1ec56b6fa8a2e2a81420bd3d90e70b59fc83f6b857fb2c2c37accddc8be3/pykerberos-1.2.1.tar.gz
Summary  : High-level interface to Kerberos
Group    : Development/Tools
License  : Apache-2.0
Requires: pykerberos-python3
Requires: pykerberos-license
Requires: pykerberos-python
BuildRequires : buildreq-distutils3
BuildRequires : e2fsprogs-dev
BuildRequires : krb5-dev

%description
This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.
        The goal is to avoid having to build a module that wraps the entire Kerberos.framework,
        and instead offer a limited set of functions that do what is needed for client/server

%package license
Summary: license components for the pykerberos package.
Group: Default

%description license
license components for the pykerberos package.


%package python
Summary: python components for the pykerberos package.
Group: Default
Requires: pykerberos-python3

%description python
python components for the pykerberos package.


%package python3
Summary: python3 components for the pykerberos package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pykerberos package.


%prep
%setup -q -n pykerberos-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536800274
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pykerberos
cp LICENSE %{buildroot}/usr/share/doc/pykerberos/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pykerberos/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
