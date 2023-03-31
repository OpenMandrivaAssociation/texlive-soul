Name:		texlive-soul
Version:	56495
Release:	2
Summary:	Hyphenation for letterspacing, underlining, and more
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/soul
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soul.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides hyphenatable spacing out (letterspacing), underlining,
striking out, etc., using the TeX hyphenation algorithm to find
the proper hyphens automatically. The package also provides a
mechanism that can be used to implement similar tasks, that
have to treat text syllable by syllable. This is shown in two
examples. The package itself does not support UTF-8 input in
ordinary (PDF)LaTeX; some UTF-8 support is offered by package
soulutf8.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/soul
%doc %{_texmfdistdir}/doc/generic/soul
#- source
%doc %{_texmfdistdir}/source/generic/soul

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
