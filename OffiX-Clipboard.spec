Summary:	A drag and drop clipboard patch for xclipboard.
Name:		OffiX-Clipboard
Version:	2.4
Release:	8
Source0:	ftp://ftp.leb.net/pub/offix/Clipboard-%{version}.tar.gz
Source1:	offix-clipboard.desktop
Patch0:		Clipboard-2.4-Xaw3d.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	GPL
Group:		User Interface/X
######		Unknown group!
######		Unknown group!

%define		_prefix		/usr/X11R6

%description
OffiX-Clipboard is a patch to the standard xclipboard program. If you
drop things on the clipboard window, they are inserted into the
current clipboard.

%description -l pl
OffiX-Clipboard to ³ata na standardowy program xclipboard. Po
upuszczeniu na okno schowka, dana rzecz zostaje umieszczona w bie¿±cym
schowku.

%prep
%setup -q -n Clipboard-2.4
%patch -p1

%build
./configure --prefix=%{_prefix} --with-dnd-inc=%{_includedir}/X11 --with-dnd-lib=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults
install -c Clipboard.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Clipboard
make prefix=$RPM_BUILD_ROOT%{_prefix}/ install
strip $RPM_BUILD_ROOT%{_bindir}/clipboard

install -d $RPM_BUILD_ROOT%{_applnkdir}/Applications/
install -o root $RPM_SOURCE_DIR/offix-clipboard.desktop $RPM_BUILD_ROOT%{_applnkdir}/Applications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL README THANKS
%config %{_libdir}/X11/app-defaults/Clipboard
%attr(755,root,root) %{_bindir}/clipboard
%{_mandir}/man1/clipboard.1
%{_applnkdir}/Applications/offix-clipboard.desktop
