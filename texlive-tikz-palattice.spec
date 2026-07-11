%global tl_name tikz-palattice
%global tl_revision 43442

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Draw particle accelerator lattices with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-palattice
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-palattice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-palattice.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows for drawing a map of a particle accelerator just by
giving a list of elements -- similar to lattice files for simulation
software. The package includes 12 common element types like dipoles,
quadrupoles, cavities, or screens, as well as automatic labels with
element names, a legend, a rule, and an environment to fade out parts of
the accelerator. The coordinate of any element can be saved and used for
custom TikZ drawings or annotations. Thereby, lattices can be connected
to draw injection/extraction or even a complete accelerator facility.

