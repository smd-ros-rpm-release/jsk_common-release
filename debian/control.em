Source: @(Package)
Section: misc
Priority: extra
Maintainer: @(Maintainer)
Build-Depends: debhelper (>= 9.0.0), @(', '.join(BuildDepends)), jsk-groovy-navigation
Homepage: @(Homepage)
Standards-Version: 3.9.2

Package: @(Package)
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, @(', '.join(Depends)), jsk-groovy-navigation
Description: @(Description)
