import {
	// Streamlit,
	StreamlitComponentBase,
	withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"


class CompareStock extends StreamlitComponentBase {
	public state = { }

	private symbol = this.props.args["symbol"]
	private symbolBenchmark = this.props.args["symbol_benchmark"]

	private wrapperStyle = { padding: "1.25rem" }

	private symbolValueIsGreater = () : boolean => {
		return this.symbol.value > this.symbolBenchmark.value
	}

	private showPercentageDiff = () : string => {
		let percentage = (this.symbol.value / this.symbolBenchmark.value) * 100
		let prefix = !this.symbolValueIsGreater() ? "-" : "+"
		return prefix + percentage.toFixed(2) + "%"
	}

	private hasDescription = () : boolean => {
		if (this.symbolValueIsGreater()) {
			return this.symbol.description !== undefined
		}

		return this.symbolBenchmark.description !== undefined
	}

	public render = (): ReactNode => {

		return (
			<div className="row">
				<div className="col-6 col-sm-4">
					<div className="card">
						<div className="card-body">
							<h5 className="card-title">
								<strong>{ this.symbol.title }</strong>
							</h5>
							<p className="card-text d-flex flex-wrap justify-content-between">
								<span>{ this.symbol.label }{ this.symbol.value }</span>
								<span className={ this.symbolValueIsGreater() ? "text-success" : "text-danger" }>
									{ this.showPercentageDiff() }
								</span>
							</p>
						</div>
					</div>
				</div>
				<div className="col-6 col-sm-2" style={ this.wrapperStyle }>
					<h5 className="card-title">{ this.symbolBenchmark.title }</h5>
					<p className="card-text">{ this.symbolBenchmark.label }{ this.symbolBenchmark.value }</p>
				</div>
				<div className={this.hasDescription() ? "col border-left border-secondary" : "d-none"} style={ this.wrapperStyle }>
					{ this.symbolValueIsGreater() ? this.symbol.description : this.symbolBenchmark.description }
				</div>
			</div>
		)
	}
}

export default withStreamlitConnection(CompareStock)
