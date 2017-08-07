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
    this.pagesize = 20;
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
    document.title = "Cloverflow: Manual Clone Classification Tool";
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
    if (this.currentid > 0) {
      if (this.currentid > this.page * this.pagesize) {
        this.currentid--;
        this.setState({pageoffset: this.state.pageoffset - 1});
      } else {
        this.previousSetSelectLast();
      }
    }
  }

  increaseId(event) {
    if (this.currentid < this.maxid - 1) {
      this.currentid++;
      this.setState({pageoffset: parseInt(this.state.pageoffset) + 1});
    } else if (this.currentid == this.maxid - 1 && this.currentid < this.total - 1) {
      this.nextSet();
    }
  }

  previousSetSelectLast(event) {
    if (this.page > 0) {
      this.page--;
      this.currentid = this.page * this.pagesize + this.pagesize - 1;
      this.setState({pageoffset: this.pagesize - 1});
      this.queryDB();
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
    if ((this.page + 1) * this.pagesize + 1 < this.total) {
      this.page++;
      this.currentid = this.page * this.pagesize;
      this.setState({pageoffset: 0});
      this.queryDB();
    }
  }

  handleFileIdChange(event) {
    this.currentid = parseInt(event.target.value);
    this.setState({pageoffset: parseInt(event.target.value) - (this.page * this.pagesize)});
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
      this.total = this.state.snapshot[0]["total"];

      this.maxid = this.page * this.pagesize + this.pagesize;
      if (this.state.snapshot.length < this.pagesize)
        this.maxid = this.page * this.pagesize + this.state.snapshot.length;

      return (
        <div>
          <div id="clone_form" className="container">
            <div className="addspace hasborder addpadding">
              <div className="addspaceleft addmarginbottom">
              <label>
              Invesitgating clone pairs no.&nbsp;
              {this.page * this.pagesize} to {this.maxid - 1} from the total of {this.state.snapshot[0]["total"]} pairs.
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
                      { _.range(this.page * this.pagesize, this.maxid)
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
            <div className="codecontainer">
              <div className="filename">
                <label>
                <a href={"https://stackoverflow.com/questions/" + this.state.snapshot[this.state.pageoffset]["file1"].split("_")[0]}
                  target="_blank">
                {this.state.snapshot[this.state.pageoffset]["file1"]}</a><br />
                {"Start: " + this.state.snapshot[this.state.pageoffset]["start1"]
                + ", End: " + this.state.snapshot[this.state.pageoffset]["end1"]}</label>
              </div>
              <div id="code1">
                {/* using https://github.com/conorhastings/react-syntax-highlighter for syntax highlight */}
                <SyntaxHighlighter language='java' style={docco} showLineNumbers='true'>
                      { this.state.snapshot[this.state.pageoffset]["code1"] }
                </SyntaxHighlighter>
              </div>
            </div>
            <div className="codecontainer">
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
