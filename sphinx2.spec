Summary:	Speech recognitnion engine
Summary(pl):	System rozpoznawania mowy
Name:		sphinx2
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
URL:		http://www.speech.cs.cmu.edu/sphinx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of Carnegie Mellon University's open source large vocabulary, 
speaker-independent continuous speech recognition engine.

Plug your microphone, launch sphinx2-simple, and test it!

%description -l pl


%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description -l pl devel
Pliki nag³ówkowe %{name}.

%prep 
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# hmm, name may conflict
rm -f $RPM_BUILD_ROOT%{_bindir}/batch.csh

gzip -9nf README

%post   
/sbin/ldconfig

%postun 
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_datadir}/%{name}


%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
