Name:           ea-nginx-njs
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 1
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        njs scripting language for ea-nginx
License:        2-clause BSD-like license
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  ea-nginx

Source0:        ngx_njs_module.conf

Requires: ea-nginx

%description
njs is a subset of the JavaScript language that allows extending nginx
functionality. njs is created in compliance with ECMAScript 5.1 (strict mode)
with some ECMAScript 6 and later extensions. The compliance is still evolving.
More information on how to use it can be found at https://nginx.org/en/docs/njs/
This package covers the 'Download and install' portions of that document as
well as loading the modules. All you need to do is add the njs directives
into your customer configurations.

%build
echo "TODO: build dynamic module using ea-nginx w/ --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx etc"
# nginx -V 2>&1| grep "configure arguments"| sed 's/configure arguments: //'
# ./configure <^^^ configure flags sans other dynamic or static modules sourceballs> --add-dynamic-module=.

%install
mkdir -p %{buildroot}/etc/nginx/conf.d/modules
install %{SOURCE0} %{buildroot}/etc/nginx/conf.d/modules/ngx_njs_module.conf

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
/etc/nginx/conf.d/modules/ngx_njs_module.conf
%attr(0755,root,root) %{_libdir}/nginx/modules/ngx_http_js_module.so
%attr(0755,root,root) %{_libdir}/nginx/modules/ngx_stream_js_module.so

%changelog
* Thu Feb 24 2022 Daniel Muey <dan@cpanel.net> - 1.0-1
- ZC-9697: Initial version
