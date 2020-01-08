Name:           minigalaxy
Version:        0.9.2
Release:        1
Summary:        Unofficial GOG client for Linux
BuildArch:      noarch
License:        GPLv3+
URL:            https://github.com/sharkwouter/minigalaxy
Source0:        https://github.com/sharkwouter/minigalaxy/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3egg(setuptools)
BuildRequires:  python3dist(requests)
Requires:       webkit2
 
%description
Python 3 based, simple and unofficial GOG client for Linux that lets you download and play your GOG Linux
games.
 
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
%{_iconsdir}/hicolor/192x192/apps/minigalaxy.png
%{python_sitelib}/%{name}/
%{python_sitelib}/Minigalaxy-*.egg-info/
%{_datadir}/metainfo/minigalaxy.metainfo.xml
