Name:           hello-world
Version:        1.0.0
Release:        2%{?dist}
Summary:        A simple service that logs "Hello World" to journald every 5 seconds

License:        MIT
URL:            https://github.com/FKolwa/packaging-tutorial
Source0:        hello-world.sh
Source1:        hello-world.service

BuildArch:      noarch
BuildRequires:  systemd

Requires:       systemd

%description
A simple service that logs "Hello World" to journald every 5 seconds.

%install
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}.sh
install -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%files
%{_bindir}/%{name}.sh
%{_unitdir}/%{name}.service

%post
systemctl --system daemon-reload 2>&1

%preun
if [ $1 -eq 0 ]; then
    systemctl --quiet stop %{name}.service
    systemctl --quiet disable %{name}.service
fi

%posttrans
systemctl is-enabled %{name}.service >/dev/null 2>&1
if [  $? -eq 0 ]; then
    systemctl restart %{name}.service >/dev/null
fi


%changelog
* Thu Feb 08 2024 Your Name <your.email@example.com> - 1.0.0-1
- Initialize package 
