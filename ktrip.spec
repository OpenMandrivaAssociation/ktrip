%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		ktrip
Version:	23.08.4
Release:	%{?git:0.%{git}.}2
Summary:	Public transport assistant for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/plasma-mobile/ktrip/-/archive/v%{version}/ktrip-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5QQC2DesktopStyle)
BuildRequires:	cmake(KPublicTransport)

%description
Public transport assistant for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang ktrip --all-name

%files -f ktrip.lang
%{_bindir}/ktrip
%{_datadir}/applications/org.kde.ktrip.desktop
%{_datadir}/metainfo/org.kde.ktrip.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.ktrip.svg
