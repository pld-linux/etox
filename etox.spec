Summary:	Enlightened Text Object Library
Name:		etox
Version:	0.9.0
%define _snap	20050106
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	3af0f5ba3e9d55a3f30437f6ffa17c7e
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	DirectFB-static
BuildRequires:	ecore-static
BuildRequires:	edb-static
BuildRequires:	eet-static
BuildRequires:	evas-static
BuildRequires:	freetype-static
BuildRequires:	libjpeg-static
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etox is a type setting and text layout library based on Evas. Etox
helps you when it comes to displaying, moving, resizing, layering,
clipping, aligning and coloring fonts in different styles.

Among other things, Etox provides a text layout engine that can
dynamically arrange text flow around other graphical obstacles.

%package devel
Summary:	Etox headers and development libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Etox development headers and libraries.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README*
%attr(755,root,root) %{_libdir}/libetox.so.*
%attr(755,root,root) %{_bindir}/etox_test
%attr(755,root,root) %{_bindir}/etox_selections
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetox.so
%{_libdir}/libetox.la
%{_pkgconfigdir}/etox.pc
%{_includedir}/Etox.h
%attr(755,root,root) %{_bindir}/etox-config
%{_aclocaldir}/etox.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libetox.a
