Summary:	Tool which converts a PNG file to a C source
Summary(pl.UTF-8):	Narzędzie konwertujące grafikę w PNG do kodu w C
Name:		png2c
Version:	1.1
Release:	1
Epoch:		0
License:	distributable
Vendor:		David Gerber <zapek@meanmachine.ch>
Group:		Development
Source0:	http://zapek.com/software/png2c/%{name}.tar.gz
# Source0-md5:	6133382233fa3e10f5e634b78dac7b5b
Patch0:		%{name}-ISO-C.patch
Patch1:		%{name}-makefile.patch
URL:		http://zapek.com/software/png2c/
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
png2c is a tool which converts a PNG file to a C source. It makes it
easy to embed PNG pictures within your program.

Formats currently supported:
 - 32-bit RGBA -> output to ARGB
 - 24-bit -> output to RGB

%description -l pl.UTF-8
png2c to narzędzie konwertujące grafikę w PNG do kodu w C. Dzięki
niemu można w bardzo łatwy sposób wbudować grafikę do swoich
programów.

Formaty obecnie obsługiwane:
 - 32-bit RGBA -> na wyjściu ARGB
 - 24-bit -> na wyjściu RGB

%prep
%setup -q -n %{name}
%patch -P0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install png2c $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_bindir}/*
