Summary:	Collection of C++ functions emulating Python's string class methods
Name:		pystring
Version:	1.1.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/imageworks/pystring/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f2c68786b359f5e4e62bed53bc4fb86d
URL:		https://github.com/imageworks/pystring
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pystring is a collection of C++ functions which match the interface
and behavior of python's string class methods using std::string.
Implemented in C++, it does not require or make use of a python
interpreter. It provides convenience and familiarity for common string
operations not included in the standard C++ library. It's also useful
in environments where both C++ and python are used.

Overlapping functionality (such as index and slice/substr) of
std::string is included to match python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%{__make} \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

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
%doc README
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
