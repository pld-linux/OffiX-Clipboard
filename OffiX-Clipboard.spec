Summary:	A drag and drop clipboard patch for xclipboard
Summary(pl):	Xclipboard z ³at± do obs³ugi "przenie¶ i upu¶æ"
Name:		OffiX-Clipboard
Version:	2.4
Release:	8
License:	GPL
Group:		X11
Source0:	ftp://ftp.leb.net/pub/offix/Clipboard-%{version}.tar.gz
# Source0-md5:	3fa71e8f5d775d0bfd3e21cbcd370106
Source1:	offix-clipboard.desktop
Patch0:		Clipboard-2.4-Xaw3d.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
%configure2_13 \
	--with-dnd-inc=%{_includedir}/X11 \
	--with-dnd-lib=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults
install -c Clipboard.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Clipboard
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix}/ install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Applications/
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL README THANKS
%config %{_libdir}/X11/app-defaults/Clipboard
%attr(755,root,root) %{_bindir}/clipboard
%{_mandir}/man1/clipboard.1
%{_applnkdir}/Office/offix-clipboard.desktop
