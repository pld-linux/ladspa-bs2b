Summary:	BS2B (Bauer stereophonic-to-binaural DSP) effect plugin for LADSPA
Summary(pl.UTF-8):	Wtyczka efektu bs2b (DSP stereofoniczno-dwuusznego Bauera) dla szkieletu LADSPA
Name:		ladspa-bs2b
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/bs2b/%{name}-%{version}.tar.lzma
# Source0-md5:	dc8555ae062ee6cd70c64f17d9e97b20
URL:		http://www.ladspa.org/
BuildRequires:	ladspa-devel
BuildRequires:	libbs2b-devel >= 3.1.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	ladspa-common
Requires:	libbs2b >= 3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BS2B (Bauer stereophonic-to-binaural DSP) effect plugin for LADSPA.

%description -l pl.UTF-8
Wtyczka efektu bs2b (DSP stereofoniczno-dwuusznego Bauera) dla
szkieletu LADSPA.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ladspa/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS THANKS
%attr(755,root,root) %{_libdir}/ladspa/bs2b.so
