BUILDROOT =
DATADIR = /usr/share/ansible

install:
	mkdir -p $(BUILDROOT)$(DATADIR)/roles/dci-cvp
	chmod 755 $(BUILDROOT)$(DATADIR)/roles/dci-cvp

	cp -r defaults $(BUILDROOT)$(DATADIR)/roles/dci-cvp
	cp -r tasks $(BUILDROOT)$(DATADIR)/roles/dci-cvp
	cp -r files $(BUILDROOT)$(DATADIR)/roles/dci-cvp
