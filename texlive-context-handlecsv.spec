Name:		texlive-context-handlecsv
Version:	51306
Release:	2
Summary:	Data merging for automatic document creation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/context-handlecsv
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-handlecsv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-handlecsv.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package handles csv data merging for automatic document
creation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/context/third/handlecsv
%doc %{_texmfdistdir}/doc/context/third/handlecsv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
