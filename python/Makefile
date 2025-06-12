-include local.mk

CXX_INPUTS =	core/scan_wrap.cxx \
				core/tools_wrap.cxx \
				core/misc_wrap.cxx \
				core/parsers_wrap.cxx

GENERATED_FILES =		MOODS/misc.py \
						MOODS/parsers.py \
						MOODS/scan.py \
						MOODS/tools.py

PYTHON ?= python3
SWIG ?= swig


all: wheel

.PHONY: all clean ext wheel

clean:
	$(RM) -rf build dist $(CXX_INPUTS) $(GENERATED_FILES)

wheel: $(CXX_INPUTS)
	$(PYTHON) setup.py bdist_wheel

ext: $(CXX_INPUTS)
	$(PYTHON) setup.py build_ext --inplace

core:
	ln -sf ../core

$(CXX_INPUTS): core

%_wrap.cxx: %.i
	$(SWIG) -c++ -python -outdir MOODS/ $<
