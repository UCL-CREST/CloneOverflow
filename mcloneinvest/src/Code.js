import React, { Component } from 'react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/styles';

class Code extends Component {
  constructor(props) {
    super(props);

    this.state = {
    }; // <- set up react state
  }

  componentDidMount() {
    var myCode = document.getElementById(this.props.codename)
    if (this.props.codename === "code1") {
      myCode.scrollTop = 20 + 15 * (parseInt(this.props.snapshot[this.props.pageoffset]["start1"], 10) - 1);
    } else if (this.props.codename === "code2") {
      myCode.scrollTop = 20 + 15 * (parseInt(this.props.snapshot[this.props.pageoffset]["start2"], 10) - 1);
    } else {
      myCode.scrollTop = 20 + 15 * (parseInt(this.props.snapshot[this.props.pageoffset]["start2"], 10) - 1);
    }
  }

  componentDidUpdate() {
    var myCode = document.getElementById(this.props.codename)
    if (this.props.codename === "code1") {
      myCode.scrollTop = 20 + 15 * (parseInt(this.props.snapshot[this.props.pageoffset]["start1"], 10) - 1);
    } else if (this.props.codename === "code2") {
      myCode.scrollTop = 20 + 15 * (parseInt(this.props.snapshot[this.props.pageoffset]["start2"], 10) - 1);
    } else {
      myCode.scrollTop = 20 + 15 * (parseInt(this.props.snapshot[this.props.pageoffset]["start2"], 10) - 1);
    }
  }

  render() {
    return (
      <div id={this.props.codename} ref={this.props.codename}>
        {/* using https://github.com/conorhastings/react-syntax-highlighter for syntax highlight */}
        <SyntaxHighlighter language='java' style={docco} showLineNumbers='true'>
              { this.props.snapshot[this.props.pageoffset][this.props.codename] }
        </SyntaxHighlighter>
      </div>
    );
  }
}

export default Code;
