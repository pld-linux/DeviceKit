Summary:	Device Enumeration Framework
Name:		DeviceKit
Version:	003
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		Libraries
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	8b311547f4a2c8c6b6598e3318d66cd7
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.76
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	udev-devel >= 130
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
Requires:	udev >= 130
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeviceKit is an abstraction for enumerating devices and listening to
device events. Any application on the system can access the
org.freedesktop.DeviceKit service via the system message bus. On
GNU/Linux, DeviceKit can be considered a simple D-Bus frontend to
udev.

%package libs
Summary:	DeviceKit library
Summary(pl.UTF-8):	Biblioteka DeviceKit
Group:		Libraries

%description libs
DeviceKit library.

%description libs
Biblioteka DeviceKit.

%package devel
Summary:	Header files for DeviceKit library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.0

%description devel
Header files for DeviceKit library.

%package static
Summary:	Static DeviceKit library
Summary(pl.UTF-8):	Statyczna biblioteka DeviceKit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static DeviceKit library.

%description static -l pl.UTF-8
Statyczna biblioteka DeviceKit.

%package apidocs
Summary:	DeviceKit library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki DeviceKit
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
DeviceKit library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki DeviceKit.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-gtk-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_bindir}/devkit
%attr(755,root,root) %{_libdir}/devkit-daemon
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.DeviceKit.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/udev/rules.d/98-devkit.rules
%{_datadir}/dbus-1/interfaces/org.freedesktop.DeviceKit.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.DeviceKit.service
%{_mandir}/man1/devkit.1*
%{_mandir}/man7/DeviceKit.7*
%{_mandir}/man8/devkit-daemon.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdevkit-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdevkit-gobject.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdevkit-gobject.so
%{_libdir}/libdevkit-gobject.la
%{_includedir}/DeviceKit
%{_pkgconfigdir}/devkit-gobject.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdevkit-gobject.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/devkit
