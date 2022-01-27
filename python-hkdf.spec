%global pypi_name hkdf
%global pypi_version 0.0.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1
Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF)

License:        BSD-2-Clause 
URL:            https://github.com/casebeer/python-hkdf
Source0:        https://files.pythonhosted.org/packages/source/%/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools

%description
HKDF - HMAC Key Derivation Function This module implements the HMAC Key
Derivation function

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
HKDF - HMAC Key Derivation Function This module implements the HMAC Key
Derivation function


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Thu Jan 27 2022 zhangkea <zhangkea@uniontech.com> - 0.0.3-1
- Initial package.
