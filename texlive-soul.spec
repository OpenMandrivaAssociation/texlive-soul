# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/soul
# catalog-date 2009-10-10 00:35:28 +0200
# catalog-license lppl
# catalog-version 2.4
Name:		texlive-soul
Version:	2.4
Release:	1
Summary:	Hyphenation for letterspacing, underlining, and more
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/soul
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides hyphenatable spacing out (letterspacing), underlining,
striking out, etc., using the TeX hyphenation algorithm to find
the proper hyphens automatically. The package also provides a
mechanism that can be used to implement similar tasks, that
have to treat text syllable by syllable. This is shown in two
examples. The package itself does not support UTF-8 input in
ordinary (PDF)LaTeX; some UTF-8 support is offered by package
soulutf8.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/soul/soul.sty
%doc %{_texmfdistdir}/doc/latex/soul/soul.pdf
%doc %{_texmfdistdir}/doc/latex/soul/soul.txt
#- source
%doc %{_texmfdistdir}/source/latex/soul/Makefile
%doc %{_texmfdistdir}/source/latex/soul/soul.dtx
%doc %{_texmfdistdir}/source/latex/soul/soul.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
