Summary: A drag and drop clipboard patch for xclipboard.
Name: OffiX-Clipboard
Version: 2.4
Release: 8
Source: ftp://ftp.leb.net/pub/offix/Clipboard-2.4.tar.gz
Source1: offix-clipboard.desktop
Patch: Clipboard-2.4-Xaw3d.patch
BuildRoot: /var/tmp/OffiX-Clipboard-build
Copyright: GPL
Group: User Interface/X

%description
OffiX-Clipboard is a patch to the standard xclipboard program. If you
drop things on the clipboard window, they are inserted into the
current clipboard.

%prep
%setup -q -n Clipboard-2.4
%patch -p1

%build
./configure --prefix=/usr/X11R6 --with-dnd-inc=/usr/X11R6/include/X11 --with-dnd-lib=/usr/X11R6/lib
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults
install -c -m 644 Clipboard.ad $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Clipboard
make prefix=$RPM_BUILD_ROOT/usr/X11R6/ install
strip $RPM_BUILD_ROOT/usr/X11R6/bin/clipboard

install -d $RPM_BUILD_ROOT/etc/X11/applnk/Applications/ 
install -m 644 -o root -g root $RPM_SOURCE_DIR/offix-clipboard.desktop $RPM_BUILD_ROOT/etc/X11/applnk/Applications/ 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README THANKS
%config /usr/X11R6/lib/X11/app-defaults/Clipboard
/usr/X11R6/bin/clipboard
/usr/X11R6/man/man1/clipboard.1
/etc/X11/applnk/Applications/offix-clipboard.desktop

%changelog
* Fri Jun 25 1999 Tim Powers <timp@redhat.com>
- rebuilt against DND v1.1 from Offix-devel-2.4-7, built for powertools 6.1

* Mon Apr 12 1999 Michael Maher <mike@redhat.com>
- built package for 6.0, added gnome desktop file

* Wed Oct 06 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file.
- built for powertools 5.2

* Tue May 19 1998 Michael Maher <mike@redhat.com>
- Checked config file for accuracy, rebuilt.

* Tue Jan 27 1998 Otto Hammersmith <otto@redhat.com>
- added desktop

* Thu Jan 22 1998 Otto Hammersmith <otto@redhat.com>
- snagged contrib package and cleaned itup
