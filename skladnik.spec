%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 70 -o "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Name:		skladnik
Version:	25.08.3
Release:	1
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/skladnik-%{version}.tar.xz
Summary:	Move the crates puzzle game
URL:		https://apps.kde.org/skladnik/
License:	GPL-2.0+
Group:		Games
BuildRequires:	cmake
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KDEGames6)

%description
Move the crates puzzle game

%files -f %{name}.lang
%{_bindir}/skladnik
%{_datadir}/applications/org.kde.skladnik.desktop
%{_datadir}/icons/hicolor/*/apps/skladnik.png
%{_mandir}/man6/skladnik.6*
%{_datadir}/metainfo/org.kde.skladnik.metainfo.xml
%{_datadir}/skladnik
