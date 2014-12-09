Name:           ros-hydro-voice-text
Version:        1.0.55
Release:        0%{?dist}
Summary:        ROS voice_text package

Group:          Development/Libraries
License:        HOYA License
URL:            http://ros.org/wiki/voice_text
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-hydro-catkin

%description
voice_text (www.voicetext.jp)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Dec 09 2014 k-okada <t@t.com> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 k-okada <t@t.com> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 k-okada <t@t.com> - 1.0.53-0
- Autogenerated by Bloom

* Mon Oct 20 2014 k-okada <t@t.com> - 1.0.51-0
- Autogenerated by Bloom

* Tue Oct 14 2014 k-okada <t@t.com> - 1.0.49-0
- Autogenerated by Bloom

* Sun Oct 12 2014 k-okada <t@t.com> - 1.0.48-0
- Autogenerated by Bloom

