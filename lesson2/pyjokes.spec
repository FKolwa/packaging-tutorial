
Name:           pyjokes
Version:        0.6.0
Release:        1%{?dist}
Summary:        One line jokes for programmers (jokes as a service)

License:        BSD
URL:            https://pypi.org/project/pyjokes/
Source0:        https://files.pythonhosted.org/packages/source/p/pyjokes/pyjokes-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Pyjokes is a python library for one line jokes for programmers. This package contains the Python 3 version of the library.}


%description %_description


%package -n python3-pyjokes
Summary:        %{summary}


%description -n python3-pyjokes %_description

%prep

%build

%install

%files 

%changelog
* Thu Feb 08 2024 Your Name <your.email@example.com> - 0.6.0-1
- First package for Fedora

