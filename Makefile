default: test_ animals

# DECORRELATION figures
White_pdf = figures/whitening.pdf figures/whitening_corr.pdf figures/whitening_atick.pdf
White_src = $(White_pdf:.pdf=.svg)

Test_pdf =  test_Image.pdf test_LogGabor.pdf test_MatchingPursuit.pdf test_SparseEdgeFactory.pdf
Test_src = $(Test_pdf:.pdf=.ipynb)
test_: $(Test_pdf)

update_user:
	pip install -U --user git+https://github.com/bicv/SLIP.git
	pip install -U --user git+https://github.com/bicv/LogGabor.git
	pip install -U --user git+https://github.com/bicv/SparseEdges.git

update:
	pip install -U git+https://github.com/bicv/SLIP.git
	pip install -U git+https://github.com/bicv/LogGabor.git
	pip install -U git+https://github.com/bicv/SparseEdges.git

get_backup:
	 scp -r laurentperrinet@10.164.5.254:/data/2017_backup/archives/2017_science/PerrinetBednar15/test .

ENIGMA = lup@truc.hd.free.fr:/Users/lup/science/PerrinetBednar15
RIOU = /hpc/invibe/perrinet.l/science/PerrinetBednar15
FRIOUL = perrinet.l@frioul.int.univ-amu.fr
OPTIONS = -av --progress --exclude .AppleDouble --exclude .git
animals:
	python experiment_animals.py

show_best:
	cat results/*SVM*serre07_distractors_serre07_targets_*first*txt |sort -n | tail -n 10
	cat results/*SVM*serre07_distractors_serre07_targets_*full*txt |sort -n | tail -n 10
	cat results/*SVM*serre07_distractors_serre07_targets_*chevron*txt |sort -n | tail -n 10

show_worst:
	cat results/*SVM*serre07_distractors_serre07_targets_*first*txt |sort -n -r | tail -n 10
	cat results/*SVM*serre07_distractors_serre07_targets_*full*txt |sort -n -r | tail -n 10
	cat results/*SVM*serre07_distractors_serre07_targets_*chevron*txt |sort -n -r | tail -n 10

cluster_run_single_threads:
	frioul_batch  -c 1 -M 36 'python experiment_testing.py'
	frioul_batch  -c 1 -M 36 'python experiment_ms.py'
	frioul_batch  -c 1 -M 36 'python experiment_animals.py'

cluster_run_parallel:
	#frioul_batch  -c 16 -M 1 'python experiment_testing.py'
	frioul_batch  -c 16 -M 4 'python experiment_ms.py'
	frioul_batch  -c 12 -M 6 'python experiment_ms.py'
	#frioul_batch  -c 16 -M 4 'python experiment_animals.py'

transfer_to_ENIGMA:
	rsync $(OPTIONS) -bwlimit=300 data_cache results *pdf  $(ENIGMA)/

transfer_from_ENIGMA:
	rsync $(OPTIONS) -bwlimit=300  $(ENIGMA)/database .

transfer_to_riou:
	rsync $(OPTIONS) test/{*.log,results,data_cache} $(FRIOUL):$(RIOU)/
transfer_from_riou:
	rsync $(OPTIONS) $(FRIOUL):$(RIOU)/{*.log,results,data_cache} test

web:
	zip web.zip $(Test_src)

todo:
	grep -R * (^|#)[ ]*(TODO|FIXME|XXX|HINT|TIP)( |:)([^#]*)
# macros for tests
test_%.pdf: test_%.ipynb
	ipython nbconvert --SphinxTransformer.author='Laurent Perrinet (INT, UMR7289)' --to latex --post PDF $<

experiment_%: experiment_%.py
	python  $<

linux_view:
	evince $(Test_pdf) &

mac_view:
	open $(Test_pdf) &

# cleaning macros
clean_tmp:
	#find . -name .AppleDouble -type d -exec rm -fr {} \;
	find .  -name *lock* -exec rm -fr {} \;
	rm frioul.*
	rm log-edge-debug.log

clean_SVM:
	rm frioul.* results/*png results/*SVM*txt data_cache/*hist* data_cache/*SVM* data_cache/*lock results/*lock
clean:
	rm -f results/* white*.npy $(latexfile).pdf *.pyc *.py~ *.npy

.PHONY: clean
