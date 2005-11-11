Summary:	Speech recognitnion engine
Summary(pl):	System rozpoznawania mowy
Name:		sphinx2
Version:	0.6
Release:	1
License:	BSD-like
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
# Source0-md5:	5fcd8e3b6c21334866f07c601f36b37e
Patch0:		%{name}-wid.patch
#Patch1:		%{name}-acam.patch
URL:		http://www.speech.cs.cmu.edu/sphinx/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of Carnegie Mellon University's open source large vocabulary,
speaker-independent continuous speech recognition engine.

Plug your microphone, launch sphinx2-simple, and test it!

%description -l pl
System rozpoznawania ci±g³ej mowy, niezale¿ny od mówi±cego, z du¿ym
s³ownikiem, pochodz±cy z Carnegie Mellon University.

Pod³±cz mikrofon, uruchom sphinx2-simple i testuj!

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description devel -l pl
Pliki nag³ówkowe %{name}.

%package static
Summary:	Static sphinx2 libraries
Summary(pl):	Biblioteki statyczne sphinx2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of sphinx2 libraries.

%description static -l pl
Statyczne wersje bibliotek sphinx2.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# hmm, name may conflict
rm -f $RPM_BUILD_ROOT%{_bindir}/batch.csh

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
