Summary:	Collection of C++ functions emulating Python's string class methods
Summary(pl.UTF-8):	Zbiór funkcji C++ emulujących metody pythonowej klasy string
Name:		pystring
Version:	1.1.4
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/imageworks/pystring/releases
Source0:	https://github.com/imageworks/pystring/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e469841e8cea730353b7beb8ef8b33a4
URL:		https://github.com/imageworks/pystring
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pystring is a collection of C++ functions which match the interface
and behavior of Python's string class methods using std::string.
Implemented in C++, it does not require or make use of a Python
interpreter. It provides convenience and familiarity for common string
operations not included in the standard C++ library. It's also useful
in environments where both C++ and Python are used.

Overlapping functionality (such as index and slice/substr) of
std::string is included to match Python interfaces.

Originally developed at Sony Pictures Imageworks.
<http://opensource.imageworks.com/>

%description -l pl.UTF-8
Pystring to zbiór funkcji C++ o interfejsie i zachowaniu metod
pythonowej klasy string, zaimplementowanych przy użyciu std::string.
Implementacja w C++ nie wymaga ani nie używa interpretera Pythona.
Zapewnia, że częste operacje na łańcuchach, nie zawarte w standardzie
C++, są wygodne i znajome. Jest przydatna w środowiskach, gdzie
używane są jednocześnie C++ i Python.

Pokrywająca się funkcjonalność (taka jak indeks i slice/substr)
klasy std::string jest dołączona tak, aby pasowała do interfejsów
Pythona.

Kod oryginalnie powstał w Sony Pictures Imageworks
<http://opensource.imageworks.com/>.

%package devel
Summary:	Header files for pystring library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pystring
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for pystring library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pystring.

%package static
Summary:	Static pystring library
Summary(pl.UTF-8):	Statyczna biblioteka pystring
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pystring library.

%description static -l pl.UTF-8
Statyczna biblioteka pystring.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -Wall -Wextra" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/pystring}

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

cp -p pystring.h $RPM_BUILD_ROOT%{_includedir}/pystring

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libpystring.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpystring.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpystring.so
%{_libdir}/libpystring.la
%{_includedir}/pystring

%files static
%defattr(644,root,root,755)
%{_libdir}/libpystring.a
