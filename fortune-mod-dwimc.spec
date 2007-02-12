Summary:	Collection of Dude! Where Is My Car ?!
Summary(pl.UTF-8):   Zestaw fortunek z filmu Stary! Gdzie jest moja bryka?
Name:		fortune-mod-dwimc
Version:	1.0
Release:	1
License:	BSD
Group:		Applications/Games
BuildRequires:	fortune-mod
Requires:	fortune-mod
Source0:	dwimc.tgz
# Source0-md5:	ff5b1c6bb8208b208d7aba9026b2b635
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

%description -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

%prep
%setup -q -n dwimc

%build
strfile dwimc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install dwimc* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
