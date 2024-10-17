Name:		texlive-tikz-palattice
Version:	43442
Release:	2
Summary:	Draw particle accelerator lattices with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tikz-palattice
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-palattice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-palattice.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows for drawing a map of a particle accelerator
just by giving a list of elements -- similar to lattice files
for simulation software. The package includes 12 common element
types like dipoles, quadrupoles, cavities, or screens, as well
as automatic labels with element names, a legend, a rule, and
an environment to fade out parts of the accelerator. The
coordinate of any element can be saved and used for custom TikZ
drawings or annotations. Thereby, lattices can be connected to
draw injection/extraction or even a complete accelerator
facility.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-palattice
%doc %{_texmfdistdir}/doc/latex/tikz-palattice

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
