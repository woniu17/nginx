version=1.0.0
release=1
rpmdir=${PWD}/RPMBUILD
mkdir -p ${rpmdir}
rm -rf ${rpmdir}/*

tar zcvf ${rpmdir}/nginx-${version}-${release}.tar.gz auto conf configure contrib html man src nginx.spec

cd ${rpmdir}

# 通过tar包构建rpm包，似乎不需要指定sourcedir和specdir
                #--define="_sourcedir ${rpmdir}/source"  \
                #--define="_specdir ${rpmdir}/spec"    \
rpmbuild -tb --define="_topdir ${rpmdir}" \
                --define="_builddir ${rpmdir}/build"   \
                --define="_buildrootdir ${rpmdir}/buildroot"   \
                --define="_rpmdir ${rpmdir}/rpm"       \
                --define="_srcrpmdir ${rpmdir}/srcrpm" \
                nginx-${version}-${release}.tar.gz
