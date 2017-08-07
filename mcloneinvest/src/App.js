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
      pageoffset: 0,
      showorig: false
    }; // <- set up react state

    // normal variable
    this.pagesize = 10;
    this.page = 0;
    this.currentid = 0;
    this.total = 0;

    this.decreaseId = this.decreaseId.bind(this);
    this.increaseId = this.increaseId.bind(this);
    this.handleFileIdChange = this.handleFileIdChange.bind(this);
    this.showOriginalCode = this.showOriginalCode.bind(this);
    this.showFormattedCode = this.showFormattedCode.bind(this);
    this.queryDB = this.queryDB.bind(this);
    this.previousSet = this.previousSet.bind(this);
    this.nextSet = this.nextSet.bind(this);
  }

  componentWillMount(){
    this.queryDB();
  }

  queryDB() {
    /* Create reference to messages in Firebase Database */
    let clonesRef = fire.database().ref('clones/pairs')
                        .orderByKey()
                        .startAt(this.page * this.pagesize + '')
                        .endAt((this.page * this.pagesize + this.pagesize - 1) + '');

    clonesRef.once("value", snapshot => {
      this.setState({snapshot: Object.values(snapshot.val())});
    });
  }

  decreaseId(event) {
    if (this.currentid > this.page * this.pagesize) {
      this.currentid--;
      this.setState((prevState) => ({
        pageoffset: parseInt(prevState.pageoffset) - 1
      }));
    }
  }

  increaseId(event) {
    // alert(this.currentid + "," + (this.page * this.pagesize + this.pagesize - 1));
    if (this.currentid < this.page * this.pagesize + this.pagesize - 1) {
      this.currentid++;
      this.setState((prevState) => ({
        pageoffset: parseInt(prevState.pageoffset) + 1
      }));
    }
  }

  previousSet(event) {
    if (this.page > 0) {
      this.page--;
      this.currentid = this.page * this.pagesize;
      this.setState({pageoffset: 0});
      this.queryDB();
    }
  }

  nextSet(event) {
      this.page++;
      this.currentid = this.page * this.pagesize;
      this.setState({pageoffset: 0});
      this.queryDB();
  }

  handleFileIdChange(event) {
    this.currentid = parseInt(event.target.value);
    this.setState({pageoffset: parseInt(event.target.value)});
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
              <div className="addspaceleft addmarginbottom">
              <label>
              Invesitgating clone pairs no.&nbsp;
              {this.page * this.pagesize} to {this.page * this.pagesize + this.pagesize - 1} from the total of {this.state.snapshot[this.state.pageoffset]["total"]} pairs.
              </label>
              </div>
              <label className="addspaceleft">Please classify the clone pair below:</label>
              <div className="addpadding addmargin">
              <input className="addsmallspaceleft"
                type="button"
                onClick={this.previousSet}
                value="Previous set" />
                <input className="addsmallspaceleft"
                  type="button"
                  onClick={this.decreaseId}
                  value="<<" />
                  <select className="addsmallspaceleft" onChange={this.handleFileIdChange}
                  value={this.page * this.pagesize + this.state.pageoffset}>
                      { _.range(this.page * this.pagesize,
                        this.page * this.pagesize + this.pagesize)
                        .map(value => <option key={value} value={value}>{value}</option>) }
                  </select>
                <input
                  className="addsmallspaceleft"
                  type="button"
                  onClick={this.increaseId}
                  value=">>" />
                <input
                  className="addsmallspaceleft"
                  type="button"
                  onClick={this.nextSet}
                  value="Next set" />
              </div>
            </div>
            <Form currentid={this.currentid} data={this.state.snapshot[this.state.pageoffset]}/>
          </div>
          <div className="container">
            <div>
              <div className="filename">
                <label>
                <a href={"https://stackoverflow.com/questions/" + this.state.snapshot[this.state.pageoffset]["file1"].split("_")[0]}
                  target="_blank">
                {this.state.snapshot[this.state.pageoffset]["file1"]}</a><br />
                {"Start: " + this.state.snapshot[this.state.pageoffset]["start1"]
                + ", End: " + this.state.snapshot[this.state.pageoffset]["end1"]}</label>
              </div>
              {/* using https://github.com/conorhastings/react-syntax-highlighter for syntax highlight */}
              <div id="code1">
                <SyntaxHighlighter language='java' style={docco} showLineNumbers='true'>
                    { this.state.snapshot[this.state.pageoffset]["code1"] }
                </SyntaxHighlighter>
              </div>
            </div>
            <div>
              <div className="filename">
                <b>{this.state.snapshot[this.state.pageoffset]["file2"]}</b><br />
                {"Start: " + this.state.snapshot[this.state.pageoffset]["start2"]
                + ", End: " + this.state.snapshot[this.state.pageoffset]["end2"]}
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
                      { this.state.showorig? this.state.snapshot[this.state.pageoffset]["code1"]: 
                      this.state.snapshot[this.state.pageoffset]["code2"] }
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
