import setuptools

setuptools.setup(
	name="st_compare_stock",
	version="0.0.1",
	author="Mihai Blebea",
	author_email="mihaiserban.blebea@gmail.com",
	description="This package provides a comparison component for stocks in Streamlit",
	long_description="This package provides a comparison component for stocks in Streamlit",
	long_description_content_type="text/plain",
	url="",
	packages=setuptools.find_packages(),
	include_package_data=True,
	classifiers=[],
	python_requires=">=3.6",
	install_requires=[
		# By definition, a Custom Component depends on Streamlit.
		# If your component has other Python dependencies, list
		# them here.
		"streamlit >= 0.63",
	],
)
