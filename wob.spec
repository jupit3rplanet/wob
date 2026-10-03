%bcond tests 1

Name:           wob
Version:        0.16
Release:        1
Summary:        Lightweight overlay bar for Wayland
License:        ISC
Group:          Graphical desktop/Other
URL:            https://github.com/francma/wob
Source0:        https://github.com/francma/wob/releases/download/%{version}/wob-%{version}.tar.gz

BuildSystem:    meson
BuildOption:    -Dseccomp=enabled
BuildOption:    -Dman-pages=enabled
BuildOption:    -Dsystemd-unit-files=enabled
%if %{with tests}
BuildOption:    -Dtests=enabled
%else
BuildOption:    -Dtests=disabled
%endif

BuildRequires:  meson
BuildRequires:  scdoc
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libseccomp)
%if %{with tests}
BuildRequires:  pkgconfig(cmocka)
%endif

%description
wob (Wayland Overlay Bar) is a lightweight overlay volume, brightness (or
anything) bar for Wayland compositors supporting the
wlr-layer-shell-unstable-v1 protocol. Values are read from standard input.

%files
%license LICENSE
%doc README.md
%{_bindir}/wob
%{_mandir}/man1/wob.1*
%{_mandir}/man5/wob.ini.5*
%{_userunitdir}/wob.service
%{_userunitdir}/wob.socket
