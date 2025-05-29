%undefine _debugsource_packages

Name:           plattenalbum
Version:        2.3.0
Release:        1
Summary:        A client for the Music Player Daemon (MPD).
License:        GPL-3.0
Group:          Music
URL:            https://github.com/SoongNoonien/plattenalbum/
Source:         https://github.com/SoongNoonien/plattenalbum/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  desktop-file-utils

Requires:  python
Requires:  python-mpd2
Requires:  python-gobject3
Requires:  python-gi
Requires:  gtk4
Requires:  libadwaita-common


%description
A client for the Music Player Daemon (MPD).
Browse your collection while viewing large album covers. Play your music without managing playlists.

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%meson_install

%find_lang de.wagnermartin.Plattenalbum

%files -f de.wagnermartin.Plattenalbum.lang
%{_bindir}/plattenalbum
%{_datadir}/applications/de.wagnermartin.Plattenalbum.desktop
%{_datadir}/de.wagnermartin.Plattenalbum/de.wagnermartin.Plattenalbum.gresource
%{_datadir}/glib-2.0/schemas/de.wagnermartin.Plattenalbum.gschema.xml
%{_datadir}/metainfo/de.wagnermartin.Plattenalbum.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/de.wagnermartin.Plattenalbum.svg
%{_iconsdir}/hicolor/symbolic/apps/de.wagnermartin.Plattenalbum-symbolic.svg
