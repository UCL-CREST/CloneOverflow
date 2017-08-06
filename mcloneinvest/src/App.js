import React, { Component } from 'react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/styles';
import './App.css';
import fire from './fire';
import Form from './Form';
import _ from 'lodash';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      snapshot: [],
      currentid: 0,
      showorig: false
    }; // <- set up react state

    this.decreaseId = this.decreaseId.bind(this);
    this.increaseId = this.increaseId.bind(this);
    this.handleFileIdChange = this.handleFileIdChange.bind(this);
    this.showOriginalCode = this.showOriginalCode.bind(this);
    this.showFormattedCode = this.showFormattedCode.bind(this);
  }

  componentWillMount(){
    /* Create reference to messages in Firebase Database */
    let clonesRef = fire.database().ref('clones/pairs').orderByKey().limitToLast(683);

    clonesRef.on("value", snapshot => {
      this.setState({snapshot: Object.values(snapshot.val())});
    });

  }

  decreaseId(event) {
    if (this.state.currentid > 0)
      this.setState({currentid: this.state.currentid - 1});
  }

  increaseId(event) {
    if (this.state.currentid < Object.keys(this.state.snapshot).length - 1)
      this.setState({currentid: this.state.currentid + 1});
  }

  handleFileIdChange(event) {
    this.setState({currentid: event.target.value});
  }

  showOriginalCode(event) {
    this.setState({showorig: true});
  }

  showFormattedCode(event) {
    this.setState({showorig: false});
  }

  render() {
    if (this.state.snapshot.length === 0)
    return (
        <div className="loading-warning">LOADING</div>
    )
    else {
      return (
        <div>
          <div id="clone_form" className="container">
            <div className="addspace hasborder addpadding">
              <label class="addspaceleft">Please choose a pattern for the clone pair no.</label>
              <div className="addpadding addmargin">
                <input className="addspaceright"
                  type="button"
                  onClick={this.decreaseId}
                  value="<<" />
                  <select onChange={this.handleFileIdChange} value={this.state.currentid}>
                      { _.range(0, 100).map(value => <option key={value} value={value}>{value}</option>) }
                  </select>
                  /{Object.keys(this.state.snapshot).length - 1}
                <input
                  className="addspaceleft"
                  type="button"
                  onClick={this.increaseId}
                  value=">>" />
              </div>
            </div>
            <Form currentid={this.state.currentid} data={this.state.snapshot[this.state.currentid]}/>
          </div>
          <div className="container">
            <div>
              <div className="filename">
                <label>
                <a href={"https://stackoverflow.com/questions/" + this.state.snapshot[this.state.currentid]["file1"].split("_")[0]}
                  target="_blank">
                {this.state.snapshot[this.state.currentid]["file1"]}</a><br />
                {"Start: " + this.state.snapshot[this.state.currentid]["start1"]
                + ", End: " + this.state.snapshot[this.state.currentid]["end1"]}</label>
              </div>
              {/* using https://github.com/conorhastings/react-syntax-highlighter for syntax highlight */}
              <div id="code1">
                <SyntaxHighlighter language='java' style={docco} showLineNumbers='true'>
                    { this.state.snapshot[this.state.currentid]["code1"] }
                </SyntaxHighlighter>
              </div>
            </div>
            <div>
              <div className="filename">
                <b>{this.state.snapshot[this.state.currentid]["file2"]}</b><br />
                {"Start: " + this.state.snapshot[this.state.currentid]["start2"]
                + ", End: " + this.state.snapshot[this.state.currentid]["end2"]}
                <input
                  className="addspaceleft"
                  type="button"
                  onClick={this.showFormattedCode}
                  value="formatted" />
                <input
                  className="addspaceleft"
                  type="button"
                  onClick={this.showOriginalCode}
                  value="original" />
              </div>
              <div id="code2">
                  <SyntaxHighlighter language='java' style={docco} showLineNumbers='true'>
                      { this.state.showorig? this.state.snapshot[this.state.currentid]["code2orig"]: this.state.snapshot[this.state.currentid]["code2"] }
                  </SyntaxHighlighter>
              </div>
            </div>
          </div>
        </div>
      )
    }
  }
}

export default App;
// export default ShoppingList;
