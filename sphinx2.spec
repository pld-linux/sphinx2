Summary:	Speech recognitnion engine
Summary(pl):	System rozpoznawania mowy
Name:		sphinx2
Version:	0.3
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/cmusphinx/%{name}-%{version}.tar.gz
Patch0:		%{name}-wid.patch
URL:		http://www.speech.cs.cmu.edu/sphinx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of Carnegie Mellon University's open source large vocabulary,
speaker-independent continuous speech recognition engine.

Plug your microphone, launch sphinx2-simple, and test it!

%description -l pl
System rozpoznawania ci�g�ej mowy, niezale�ny od m�wi�cego, z du�ym
s�ownikiem, pochodz�cy z Carnegie Mellon University.

Pod��cz mikrofon, uruchom sphinx2-simple i testuj!

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag��wkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description devel -l pl
Pliki nag��wkowe %{name}.

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
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
