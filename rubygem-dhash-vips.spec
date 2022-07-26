# Generated from dhash-vips-0.1.1.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name dhash-vips

Name: rubygem-%{gem_name}
Version: 0.1.1.5
Release: 1%{?dist}
Summary: dHash and IDHash perceptual image hashing/fingerprinting
License: MIT
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

%description
dHash and IDHash perceptual image hashing/fingerprinting.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/extconf.rb/


%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/common.rb
%{gem_instdir}/idhash.c
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/dhash-vips.gemspec
%{gem_instdir}/test.rb

%changelog
* Tue Jul 26 2022 Pavel Valena <pvalena@redhat.com> - 0.1.1.5-1
- Initial package
