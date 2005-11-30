#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightened Text Object Library
Summary(pl):	O¶wiecona biblioteka obiektów tekstowych (Enlightened Text Object Library)
Name:		etox
Version:	0.9.0.004
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	ffb6de465dfc9a9b2802b414dd432932
URL:		http://enlightenment.org/Libraries/Etox/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etox is a type setting and text layout library based on Evas. Etox
helps you when it comes to displaying, moving, resizing, layering,
clipping, aligning and coloring fonts in different styles.

Among other things, Etox provides a text layout engine that can
dynamically arrange text flow around other graphical obstacles.

%description -l pl
Etox to biblioteka sk³adania i rozmieszczania tekstu oparta na Evas.
Etox pomaga przy wy¶wietlaniu, przemieszczaniu, zmianie rozmiaru,
nawarstwianiu, przycinaniu, wyrównywaniu i kolorowaniu fontów w
ró¿nych stylach.

W¶ród innych rzeczy Etex dostarcza silnik do rozmieszczania tekstu
bêd±cy w stanie dynamicznie uk³adaæ tekst naoko³o innych przeszkód
graficznych.

%package libs
Summary:	Etox library
Summary(pl):	Biblioteka Etox
Group:		X11/Libraries

%description libs
Etox library.

%description libs -l pl
Biblioteka Etox.

%package devel
Summary:	Etox header file
Summary(pl):	Plik nag³ówkowy Etox
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Etox development header.

%description devel -l pl
Plik nag³ówkowy Etox.

%package static
Summary:	Static Etox library
Summary(pl):	Statyczna biblioteka Etox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Etox library.

%description static -l pl
Statyczna biblioteka Etox.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/etox_test
%attr(755,root,root) %{_bindir}/etox_selections
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetox.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/etox-config
%attr(755,root,root) %{_libdir}/libetox.so
%{_libdir}/libetox.la
%{_includedir}/Etox.h
%{_pkgconfigdir}/etox.pc
%{_aclocaldir}/etox.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libetox.a
%endif
