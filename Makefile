.PHONY: install release

release: install
	cd LoremIpsum/frontend && npm run build

install:
	cd LoremIpsum/frontend && npm install

# EOF
