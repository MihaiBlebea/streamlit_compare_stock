compile: compile-fe compile-be

compile-be:
	python3 ./template/setup.py sdist bdist_wheel

compile-fe:
	cd ./template/st_compare_stock/frontend && npm run build

publish:
	python3 -m twine upload --repository pypi dist/* 