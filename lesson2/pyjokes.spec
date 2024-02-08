
Name:           pyjokes
Version:        0.6.0
Release:        1%{?dist}
Summary:        One line jokes for programmers (jokes as a service)

License:        BSD
URL:            https://pypi.org/project/pyjokes/
Source0:        https://files.pythonhosted.org/packages/source/p/pyjokes/pyjokes-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest

%global _description %{expand:
Pyjokes is a python library for one line jokes for programmers. This package contains the Python 3 version of the library.}


%description %_description


%package -n python3-pyjokes
Summary:        %{summary}


%description -n python3-pyjokes %_description


%prep
%autosetup -p1 -n pyjokes-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyjokes


%files -n python3-pyjokes -f %{pyproject_files}
%doc README.*
%{_bindir}/pyjokes
%{_bindir}/pyjoke
%{python3_sitelib}/pyjokescli/*


%changelog
* Thu Feb 08 2024 Your Name <your.email@example.com> - 0.6.0-1
- First package for Fedora

