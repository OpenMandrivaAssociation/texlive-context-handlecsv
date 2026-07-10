%global tl_name context-handlecsv
%global tl_revision 76721

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Data merging for automatic document creation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-handlecsv
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-handlecsv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-handlecsv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package handles csv data merging for automatic document creation.

