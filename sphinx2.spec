Summary:	CMU Sphinx2 - Speech recognitnion engine
Summary(pl.UTF-8):	CMU Sphinx2 - System rozpoznawania mowy
Name:		sphinx2
Version:	0.6
Release:	3
License:	BSD-like
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
# Source0-md5:	5fcd8e3b6c21334866f07c601f36b37e
Patch0:		%{name}-wid.patch
Patch1:		link.patch
URL:		https://cmusphinx.github.io/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of Carnegie Mellon University's open source large vocabulary,
speaker-independent continuous speech recognition engine.

Plug your microphone, launch sphinx2-simple, and test it!

%description -l pl.UTF-8
System rozpoznawania ciągłej mowy, niezależny od mówiącego, z dużym
słownikiem, pochodzący z Carnegie Mellon University.

Podłącz mikrofon, uruchom sphinx2-simple i testuj!

%package devel
Summary:	CMU Sphinx2 header files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek CMU Sphinx2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
CMU Sphinx2 header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek CMU Sphinx2.

%package static
Summary:	Static CMU Sphinx2 libraries
Summary(pl.UTF-8):	Biblioteki statyczne CMU Sphinx2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of CMU Sphinx2 libraries.

%description static -l pl.UTF-8
Statyczne wersje bibliotek CMU Sphinx2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%attr(755,root,root) %{_bindir}/adpow
%attr(755,root,root) %{_bindir}/adrec
%attr(755,root,root) %{_bindir}/cdcn_test
%attr(755,root,root) %{_bindir}/cont_adseg
%attr(755,root,root) %{_bindir}/cont_fileseg
%attr(755,root,root) %{_bindir}/lm3g2dmp
%attr(755,root,root) %{_bindir}/lm_fsg_test*
%attr(755,root,root) %{_bindir}/pdf32to8b
%attr(755,root,root) %{_bindir}/raw2cep
%attr(755,root,root) %{_bindir}/sphinx2-*
%attr(755,root,root) %{_libdir}/libsphinx2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsphinx2.so.0
%attr(755,root,root) %{_libdir}/libsphinx2ad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsphinx2ad.so.0
%attr(755,root,root) %{_libdir}/libsphinx2fe.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsphinx2fe.so.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsphinx2.so
%attr(755,root,root) %{_libdir}/libsphinx2ad.so
%attr(755,root,root) %{_libdir}/libsphinx2fe.so
%{_libdir}/libsphinx2.la
%{_libdir}/libsphinx2ad.la
%{_libdir}/libsphinx2fe.la
%{_includedir}/sphinx2

%files static
%defattr(644,root,root,755)
%{_libdir}/libsphinx2.a
%{_libdir}/libsphinx2ad.a
%{_libdir}/libsphinx2fe.a
