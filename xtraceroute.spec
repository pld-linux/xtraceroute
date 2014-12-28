Summary:	An X and GTK+ based graphical display of traceroute's output
Summary(pl.UTF-8):	Program wyświetlający traceroute w postaci graficznej pod X/GTK+
Name:		xtraceroute
Version:	0.9.1
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.dtek.chalmers.se/~d3august/xt/dl/%{name}-%{version}.tar.gz
# Source0-md5:	ac212fed3ac9dc06851e5ffbe95901c0
Source1:	http://www.dtek.chalmers.se/~d3august/xt/dl/ndg_files.tar.gz
# Source1-md5:	0e2d6ab6a780b49acbd8f706840380d9
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-po.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-segv.patch
Patch4:		%{name}-stat.patch
URL:		http://www.dtek.chalmers.se/~d3august/xt/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel >= 1.0.0
BuildRequires:	gtkglarea1-devel
BuildRequires:	libtiff-devel
Requires:	/usr/bin/traceroute
Requires:	/usr/bin/host-nikhof
ExcludeArch:	ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
xtraceroute is a graphical version of the traceroute program, which
traces the route your IP packets travel to their destination.
Xtraceroute shows the packets' path on a rotating globe, as a series
of yellow lines between sites, which are shown as small balls of
different colors. You'll need a fairly fast machine, an OpenGL
implementation (Mesa or OpenGL), GTK+, GtkGLArea, and tifflib.

%description -l pl.UTF-8
xtraceroute jest graficzną wersją programu traceroute, śledzącego
trasę Twoich pakietów IP do celu. Pokazuje ścieżkę pakietów na
obracającej się kuli ziemskiej jako żółtą linię pomiędzy miejscami,
które są przedstawione jako małe kropki w różnych kolorach. Program
wymaga relatywnie szybkiej maszyny z implementacją OpenGL'a (Mesa lub
OpenGL), GTK+, GtkGLArea oraz tifflib.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-lib-GL \
	--with-traceroute=/usr/bin/traceroute \
	--with-host=/usr/bin/host-nikhof \
	%{?debug:--enable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install xtraceroute.desktop $RPM_BUILD_ROOT%{_desktopdir}
install xtraceroute.png $RPM_BUILD_ROOT%{_pixmapsdir}
install networks.cache $RPM_BUILD_ROOT%{_datadir}/xtraceroute
install hosts.cache $RPM_BUILD_ROOT%{_datadir}/xtraceroute

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS BUGS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/xtraceroute
%{_mandir}/man1/*
%dir %{_datadir}/xtraceroute
%{_datadir}/xtraceroute/*.cache
%{_datadir}/xtraceroute/*.png
%attr(755,root,root) %{_datadir}/xtraceroute/*.sh
%{_desktopdir}/xtraceroute.desktop
%{_pixmapsdir}/*
