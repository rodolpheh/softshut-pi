DESTDIR=
PKGNAME=softshut

default:
	echo "Nothing to compile - nothing to do! :D"

install:
	install -D -m 644 softshut.service "${DESTDIR}/usr/lib/systemd/system/softshut.service"
	install -D -m 755 softshut.py "${DESTDIR}/usr/share/${PKGNAME}/softshut.py"
	
remove:
	rm -f "${DESTDIR}/usr/lib/systemd/system/softshut.service"
	rm -f "${DESTDIR}/usr/share/${PKGNAME}/softshut.py"
