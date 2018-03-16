%define __ver   1.0.0
%define __rel   1

Summary: Nginx Server
Name: nginx
Version: %{__ver}
Release: %{__rel}
License: Copyright
Group: Utilities/System
URL: http://m.linqingxiang.com
Packager: woniu17 <qinglucklin@foxmail.com>
Vendor: linqingxiang.com
Source0: %{name}-%{version}-%{release}.tar.gz
# BuildRoot是软件make install的测试安装目录，也就是测试中的根目录
# _tmppath默认为/var/tmp
# 该设置在centos5有效，在centos6无效，因此使用rpmbuild命令选项_buildrootdir指定
# BuildRoot: %{_tmppath}/%{name}-%{version}-root
# BuildRoot: /var/tmp/nginx-1.0.0-root

%description
nginx server


%package devel
Summary: Nginx server
Group: Development/Libraries
Requires: nginx = %{version}-%{release}

%description devel
nginx server debuginfo

# 准备阶段
%prep
# 这个宏(%setup)的作用静默模式解压并cd到%_builddir
%setup -c

# 编译阶段
%build
./configure --prefix=/usr/local/nginx  \
            --sbin-path=sbin/nginx \
            --conf-path=conf/nginx.conf \
            --pid-path=logs/nginx.pid \
            --without-http_gzip_module \
            --without-http_rewrite_module \
            --with-debug

make -j2

# 安装阶段
%install
rm -rf %{buildroot}
# DESTDIR软件要安装的根目录。约定俗成？
make DESTDIR=%{buildroot} install

# 清理阶段
%clean
# rm -rf %{buildroot}
echo "buildroot %{buildroot}"

%pre


%post
CONFFILEBAK=/usr/local/nginx/conf/nginx.conf.rpmsave

if [ -e $CONFFILEBAK ]
then
        rm -f /usr/local/nginx/conf/nginx.conf
        mv -f  $CONFFILEBAK /usr/local/nginx/conf/nginx.conf
        echo "Restore nginx's config file from nginx.conf.rpmsave"
else
        :
fi

echo "OK, nginx is already installed for you!"

%preun

%postun
echo "OK, nginx is already uninstalled for you!"
echo "Thanks for using!"


%files
%defattr(-,root,root)
# config表明这是个配置文件
%config /usr/local/nginx/conf/nginx.conf
/usr/local/nginx/*

%changelog
