%define lib_dwfcore	%mklibname dwfcore 1
%define lib_dwftk %mklibname dwftk 7

Name: dwftoolkit
Version: 7.2.1
Release: %mkrel 5
License: BSD-like
Summary: DWF Toolkit 7.2.1 provides APIs for reading and writing 3D DWF from any application
URL: http://usa.autodesk.com/
Source: DWFToolkit-%{version}-src.tar.gz
Patch0: DWFToolkit-7.2.1-soname.patch
Group: Sciences/Geosciences
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: zlib-devel

%description
DWF Toolkit 7.2.1 provides APIs for reading and writing 3D DWF from any
application, simplified 2D interfaces, supports composite DWF files (3D and 2D
combined) and cross-platform support (Windows, Mac, Linux). It includes C++
source code for reading and writing DWF files. 

#--------------------------------------------------------------------------------

%package devel
Summary: DWF Toolkit 7.2.1 devel files
Group: Development/Other
Requires: %lib_dwfcore = %version-%release
Requires: %lib_dwftk = %version-%release

%description devel
DWF Toolkit 7.2.1 devel files

%files devel
%defattr(-,root,root,-)
%_includedir/*
%_libdir/*.so
%_libdir/*.la

#--------------------------------------------------------------------------------

%package static-devel
Group: Developmen/Othert
Summary: DWF Toolkit 7.2.1 static devel files
Requires: %{name}-devel

%description static-devel
DWF Toolkit 7.2.1 static devel files

#--------------------------------------------------------------------------------

%package -n %lib_dwfcore
Group: System/Libraries
Summary: Dwfcore library

%description -n %lib_dwfcore
dwfcore library

%files -n %lib_dwfcore
%defattr(-,root,root,-)
%_libdir/*.so.*

#--------------------------------------------------------------------------------

%package -n %lib_dwftk
Group: System/Libraries
Summary: Dwftk library

%description -n %lib_dwftk
dwftk library

%files -n %lib_dwftk
%defattr(-,root,root,-)
%_libdir/*.so.*

#--------------------------------------------------------------------------------

%prep
%setup -q -c -T -n %name-%version -a 0
%patch0 -p1 -b .soname


%build
for name in dwfcore dwftoolkit; do
pushd develop/global/build/gnu/$name
sh -x build_setup.sh
popd
done
for name in dwfcore dwf; do
pushd develop/global/src/$name
%configure2_5x \
	--disable-static
%make
popd
done

%install
for name in dwfcore dwf; do
pushd develop/global/src/$name
%makeinstall_std
popd
done

%clean
rm -rf %buildroot



