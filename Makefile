# Settings
INSTALL_DIR=$(HOME)/sites/sensibleadventures.com
JEKYLL=jekyll
DST=_site

# Controls
.PHONY : commands clean
all : commands

## commands   : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILES} | sed -e 's/## //g'

## serve      : run a local server.
serve :
	${JEKYLL} serve --config _config.yml,_config_dev.yml

## site       : build files but do not run a server.
site :
	${JEKYLL} build

## install    : build into installation directory for sharing.
install :
	rm -rf $(INSTALL_DIR)
	cp -r _site $(INSTALL_DIR)

## clean      : clean up junk files.
clean :
	@rm -rf ${DST}
	@rm -rf .sass-cache
	@find . -name .DS_Store -exec rm {} \;
	@find . -name '*~' -exec rm {} \;
	@find . -name '*.pyc' -exec rm {} \;
