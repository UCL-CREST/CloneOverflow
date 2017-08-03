import React, { Component } from 'react';
import fire from './fire';

class Form extends Component {

  constructor(props) {
    super(props);

    this.state = {
      classifications: [],
      selectedOption: 'qs',
      value: 'Any notes?',
      currentid: this.props.currentid
    }; // <- set up react state

    this.handleChange = this.handleChange.bind(this);
    this.onPatternChanged = this.onPatternChanged.bind(this);
    this.decreaseId = this.decreaseId.bind(this);
    this.increaseId = this.increaseId.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  onPatternChanged(event) {
    this.setState({selectedOption: event.target.value});
  }

  decreaseId(event) {
    this.setState({currentid: this.state.currentid - 1});
  }

  increaseId(event) {
    this.setState({currentid: this.state.currentid + 1});
  }

  render() {
    return (
      <div id="form_container">
        <div className="row">
          <div className="col-sm-12">
            <form>
              <div className="addspace addspaceleft"><label>Please choose a pattern for onlin clone pair no.&nbsp;
                <input className="addspaceleft addspaceright"
                  type="button"
                  onClick={this.decreaseId}
                  value="<<" />
                <input type="text"
                  value={this.state.currentid}
                  onChange={this.handleChange} />/{Object.keys(this.props.data).length}
                </label>
                <input
                  className="addspaceleft"
                  type="button"
                  onClick={this.increaseId}
                  value=">>" />
              </div>

              <div className="container">
                <div className="radio">
                  <label>
                    <input type="radio" value="qs"
                      checked={this.state.selectedOption === 'qs'}
                      onChange={this.onPatternChanged}  />
                    QS
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="sq"
                      checked={this.state.selectedOption === 'sq'}
                      onChange={this.onPatternChanged}  />
                    SQ
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="ex"
                      checked={this.state.selectedOption === 'ex'}
                      onChange={this.onPatternChanged}  />
                    EX
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="ud"
                      checked={this.state.selectedOption === 'ud'}
                      onChange={this.onPatternChanged} />
                    UD
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="bp"
                      checked={this.state.selectedOption === 'bp'}
                      onChange={this.onPatternChanged} />
                    BP
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="in"
                      checked={this.state.selectedOption === 'in'}
                      onChange={this.onPatternChanged} />
                    IN
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="ac"
                      checked={this.state.selectedOption === 'ac'}
                      onChange={this.onPatternChanged} />
                    AC
                  </label>
                </div>
              </div>
              <div className="container">
                <div>
                  <textarea rows="2" cols="100"
                    value={this.state.value}
                    onChange={this.handleChange} />
                </div>
                <div className="addspaceleft">
                  <input type="button" value="Submit" />
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    )
  }
}

export default Form;
