# (2024-02-25) don't require 'typelib(WebKit2) = 4.0'w
# because 'typelib(WebKit2) = 4.1' is used.
%global __requires_exclude  ^typelib\\(WebKit2\\) = 4.0$

Name:           minigalaxy
Version:        1.4.0
Release:        1
Summary:        Unofficial GOG client for Linux
BuildArch:      noarch
License:        GPLv3+
URL:            https://github.com/sharkwouter/minigalaxy
Source0:        https://github.com/sharkwouter/minigalaxy/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3egg(setuptools)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pip)
Requires:       webkit4.1
 
%description
Python 3 based, simple and unofficial GOG client for Linux
that lets you download and play your GOG Linux games.
 
%prep
%autosetup -n %{name}-%{version} -p1
 
%build
%py_build
 
%install
%py_install
 
%files
%license LICENSE THIRD-PARTY-LICENSES.md
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*x*/apps/io.github.sharkwouter.Minigalaxy.png
%{python_sitelib}/%{name}/
%{python_sitelib}/minigalaxy-%{version}.dist-info
%{python_sitelib}/tests/download/
%{_datadir}/metainfo/io.github.sharkwouter.Minigalaxy.metainfo.xml
