Name: docbook5-style-xsl
Version: 1.75.2
Release: 4%{?dist}
Group: Applications/Text

Summary: Norman Walsh's XSL stylesheets for DocBook 5.X

# Package is licensed as MIT/X (http://wiki.docbook.org/topic/DocBookLicense),
# some .js files under ./slides/browser/ are licensed MPLv1.1
License: MIT and MPLv1.1
URL: http://wiki.docbook.org/topic/DocBookXslStylesheets

Provides: docbook-xsl-ns = %{version}
# xml-common was using /usr/share/xml until 0.6.3-8.
Requires: xml-common >= 0.6.3-8
# libxml2 required because of usage of /usr/bin/xmlcatalog
Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
Conflicts: passivetex < 1.21

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Source0: http://downloads.sourceforge.net/docbook/docbook-xsl-ns-%{version}.tar.bz2

%description
These XSL namespace aware stylesheets allow you to transform any
DocBook 5 document to other formats, such as HTML, manpages, FO,
XHMTL and other formats. They are highly customizable. For more
information see W3C page about XSL.

%prep
%setup -q -n docbook-xsl-ns-%{version}
#remove .gitignore files
rm -rf $(find -name '.gitignore' -type f)
#make ruby scripts executable
chmod +x epub/bin/dbtoepub

%build

%install
DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version
cp -a [[:lower:]]* $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/
cp -a VERSION $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/
ln -s xsl-ns-stylesheets-%{version} \
 $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets

# Don't ship the extensions.
rm -rf $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets/extensions
# Don't ship install shell script.
rm -rf $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets/install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,-)
%doc BUGS
%doc README COPYING
%doc TODO NEWS
%doc RELEASE-NOTES.*
%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}
%{_datadir}/sgml/docbook/xsl-ns-stylesheets

%post
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://docbook.sourceforge.net/release/xsl-ns/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://docbook.sourceforge.net/release/xsl-ns/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG


%postun
# remove entries only on removal of package
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
   "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
fi

%changelog
* Tue Feb 23 2010 Ondrej Vasik <ovasik@redhat.com> 1.75.2-4
- fix the licenses, use better URL

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.75.2-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.75.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Ondrej Vasik <ovasik@redhat.com> 1.75.2-2
- upstream changed tarballs after release

* Tue Jul 21 2009 Ondrej Vasik <ovasik@redhat.com> 1.75.2-1
- new upstream release 1.75.2

* Thu May 28 2009 Ondrej Vasik <ovasik@redhat.com> 1.75.1-1
- new upstream release 1.75.1

* Mon May 11 2009 Ondrej Vasik <ovasik@redhat.com> 1.75.0-1
- new upstream release 1.75.0

* Wed Mar 11 2009 Ondrej Vasik <ovasik@redhat.com> 1.74.3-1
- new upstream release 1.74.3

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.74.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Ondrej Vasik <ovasik@redhat.com> 1.74.2-1
- new upstream release 1.74.2

* Wed Feb 18 2009 Ondrej Vasik <ovasik@redhat.com> 1.74.1-1
- new upstream release 1.74.1

* Fri Feb 13 2009 Ondrej Vasik <ovasik@redhat.com> 1.74.0-2
- Ship VERSION file (#485297) , ship RELEASE-NOTES

* Mon Nov 10 2008 Ondrej Vasik <ovasik@redhat.com> 1.74.0-1
- Initial Fedora release
