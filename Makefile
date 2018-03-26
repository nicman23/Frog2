all: ammos frogc
mac: ammosmac frogcmac
ammos:
	cd AMMOS && make -e all
frogc:
	cd iMolecule/code_c && make -e all

clean: clean-mol clean-bored

clean-mol:
	cd iMolecule/ && make -e clean
clean-bored:
	find -type f -name *o -exec rm -rf {} \;
	find -type f -name *pyc -exec rm -rf {} \;
