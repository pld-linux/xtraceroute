Summary:	An X and GTK+ based graphical display of traceroute's output
Summary(pl):	Program wy¶wietlaj±cy traceroute w postaci graficznej pod X/GTK+
Name:		xtraceroute
Version:	0.9.0
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.dtek.chalmers.se/~d3august/xt/dl/%{name}-%{version}.tar.gz
Source1:	http://www.dtek.chalmers.se/~d3august/xt/dl/ndg_files.tar.gz
Patch0:		%{name}-desktop.patch
URL:		http://www.dtek.chalmers.se/~d3august/xt/
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gettext-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	libtiff-devel
Requires:	/usr/sbin/traceroute
Requires:	/usr/bin/host-nikhof
ExcludeArch:	ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xtraceroute is a graphical version of the traceroute program, which
traces the route your IP packets travel to their destination.
Xtraceroute shows the packets' path on a rotating globe, as a series
of yellow lines between sites, which are shown as small balls of
different colors. You'll need a fairly fast machine, an OpenGL
implementation (Mesa or OpenGL), GTK+, GtkGLArea, and tifflib.

%description -l pl
xtraceroute jest graficzn± wersj± programu traceroute, ¶ledz±cego
trasê Twoich pakietów IP do celu. Pokazuje ¶cie¿kê pakietów na
obracaj±cej siê kuli ziemskiej jako ¿ó³t± liniê pomiêdzy miejscami,
które s± przedstawione jako ma³e kropki w ró¿nych kolorach. Program
wymaga relatywnie szybkiej maszyny z implementacj± OpenGL'a (Mesa lub
OpenGL), GTK+, GtkGLArea oraz tifflib.

%prep
%setup -q -a1
%patch0 -p1

%build
%{__gettextize}
aclocal
autoheader
%{__autoconf}
%{__automake}
%configure \
	--with-lib-GL \
	--with-traceroute=/usr/sbin/traceroute \
	--with-host=/usr/bin/host-nikhof

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install xtraceroute.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network
install xtraceroute.png $RPM_BUILD_ROOT%{_pixmapsdir}
install networks.cache $RPM_BUILD_ROOT%{_datadir}/xtraceroute
install hosts.cache $RPM_BUILD_ROOT%{_datadir}/xtraceroute

gzip -9nf README AUTHORS BUGS ChangeLog NEWS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xtraceroute
%{_mandir}/man1/*
%{_datadir}/xtraceroute
%{_applnkdir}/Network/xtraceroute.desktop
%{_pixmapsdir}/*
