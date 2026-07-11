%global tl_name soul
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2
Release:	%{tl_revision}.1
Summary:	Hyphenation for letterspacing, underlining, and more
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/soul
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides hyphenable spacing out (letterspacing),
underlining, striking out, etc., using the TeX hyphenation algorithm to
find the proper hyphens automatically. It also provides a mechanism that
can be used to implement similar tasks, that have to treat text syllable
by syllable. This is shown in two examples. This version is a merge of
the original soul package from Melchior Franz and the soulutf8 package
from Heiko Oberdiek and supports also UTF8.

