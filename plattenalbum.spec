%undefine _debugsource_packages

Name:           plattenalbum
Version:        2.2.0
Release:        1
Summary:        A client for the Music Player Daemon (MPD).
License:        GPL-3.0
Group:          Music
URL:            https://github.com/SoongNoonien/plattenalbum/
Source:         https://github.com/SoongNoonien/plattenalbum/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)

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

%files
