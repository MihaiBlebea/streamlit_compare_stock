import os
import streamlit.components.v1 as components


_RELEASE = True


if not _RELEASE:
	_component_func = components.declare_component(
		"st_compare_stock",
		url="http://localhost:3001",
	)
else:
	parent_dir = os.path.dirname(os.path.abspath(__file__))
	build_dir = os.path.join(parent_dir, "frontend/build")
	_component_func = components.declare_component("st_compare_stock", path=build_dir)


def st_compare_stock(symbol: dict, symbol_benchmark: dict, key=None):
	if isinstance(symbol, dict) == False:
		raise Exception("symbol variable must be a dict")

	if isinstance(symbol_benchmark, dict) == False:
		raise Exception("symbol_benckmark variable must be a dict")

	if "title" not in symbol:
		raise Exception("title not provided in dict symbol")

	if "value" not in symbol:
		raise Exception("value not provided in dict symbol")

	if "title" not in symbol_benchmark:
		raise Exception("title not provided in dict symbol_benckmark")

	if "value" not in symbol_benchmark:
		raise Exception("value not provided in dict symbol_benckmark")


	component_value = _component_func(
		symbol=symbol,
		symbol_benchmark=symbol_benchmark,
		key=key, 
		default=0)

	return component_value


if not _RELEASE:
	import streamlit as st

	num_clicks = st_compare_stock(
		symbol={
			"title": "AAPL",
			"value": 3.25,
			"label": "$",
			"description": "The value of AAPL is more then the other"
		},
		symbol_benchmark={
			"title": "TSLA",
			"value": 2.45,
			"label": "$",
			"description2": "The value of TSLA is more then the other"
		}
	)

