import React, { Component } from 'react';
import fire from './fire';

class Form extends Component {

  constructor(props) {
    super(props);

    this.state = {
      classifications: [],
      selectedOption: 'QS',
      notes: 'Any notes?',
      currentid: this.props.currentid,
      changeSelection: false
    }; // <- set up react state

    // alert(this.props.currentid);
    this.onPatternChanged = this.onPatternChanged.bind(this);
    this.submitForm = this.submitForm.bind(this);
    this.handleTextAreaChange = this.handleTextAreaChange.bind(this);
  }

  componentWillMount(props) {
    // set the classification
    this.setState({selectedOption: this.props.data["classification"]});
    this.setState({notes: this.props.data["notes"]});
  }

  onPatternChanged(event) {
    this.setState({selectedOption: event.target.value});
    this.setState({changeSelection: true});
  }

  handleTextAreaChange(event) {
    this.setState({notes: event.target.value});
    this.setState({changeSelection: true});
  }

  submitForm(event) {
    var id = this.props.currentid;
    /* Create reference to messages in Firebase Database */
    let clonesRef = fire.database().ref('clones/pairs').child(id);
    var classification = this.state.selectedOption;
    var notes = this.state.notes;
    clonesRef.update({
                    'classification': classification,
                    'notes': notes
                });

    this.setState({changeSelection: false});
    alert("Updated");
  }

  render() {
    // alert(this.props.data["classification"]);
    if (!this.state.changeSelection) {
      this.setState({selectedOption: this.props.data["classification"]});
      this.setState({notes: this.props.data["notes"]});
    }
    return (
      <div id="form_container">
        <div className="row">
          <div className="col-sm-12">
            <form>
              <div className="container">
                <div className="radio">
                  <label>
                    <input type="radio" value="QS"
                      checked={this.state.selectedOption === 'QS'}
                      onChange={this.onPatternChanged}  />
                    QS
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="SQ"
                      checked={this.state.selectedOption === 'SQ'}
                      onChange={this.onPatternChanged}  />
                    SQ
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="EX"
                      checked={this.state.selectedOption === 'EX'}
                      onChange={this.onPatternChanged}  />
                    EX
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="UD"
                      checked={this.state.selectedOption === 'UD'}
                      onChange={this.onPatternChanged} />
                    UD
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="BP"
                      checked={this.state.selectedOption === 'BP'}
                      onChange={this.onPatternChanged} />
                    BP
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="IN"
                      checked={this.state.selectedOption === 'IN'}
                      onChange={this.onPatternChanged} />
                    IN
                  </label>
                </div>
                <div className="radio">
                  <label>
                    <input type="radio" value="AC"
                      checked={this.state.selectedOption === 'AC'}
                      onChange={this.onPatternChanged} />
                    AC
                  </label>
                </div>
              </div>
              <div className="container">
                <div>
                  <textarea rows="2" cols="100"
                    className="normalfont"
                    value={this.state.notes}
                    onChange={this.handleTextAreaChange} />
                </div>
                <div className="addspaceleft" onClick={this.submitForm}>
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
