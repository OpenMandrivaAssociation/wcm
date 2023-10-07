Name:           wcm
Version:        0.8.0
Release:        1
Summary:        Wayfire Config Manager
Group:          System/Tools/Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wcm
Source0:        https://github.com/WayfireWM/wcm/releases/download/v%{version}/wcm-%{version}.tar.xz

BuildRequires:  pkgconfig(glm)
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wf-config) >= 0.8.0
BuildRequires:  pkgconfig(wf-shell) >= 0.8.0
BuildRequires:  pkgconfig(xkbregistry)
 
Requires:       hicolor-icon-theme

Provides: wayfire-config-manager
 
%description
Wayfire Config Manager is a Gtk3 application to configure wayfire. It writes the config file that wayfire reads to update option values.
 
%prep
%autosetup -n wcm-%{version} -p1
 
%build
%meson
%meson_build
 
%install
%meson_install
 
%files
%license LICENSE
%{_bindir}/wcm
%{_bindir}/wdisplays
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/wdisplays.svg
%{_datadir}/wayfire/
