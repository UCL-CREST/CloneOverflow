import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import fire from './fire';
import Form from './Form';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      snapshot: [],
      currentid: 1
    }; // <- set up react state
  }

  componentWillMount(){
    /* Create reference to messages in Firebase Database */
    let clonesRef = fire.database().ref('clones/pairs').orderByKey().limitToLast(100);

    clonesRef.on("value", snapshot => {
      this.setState({snapshot: Object.values(snapshot.val())});
    });

  }

  render() {
    var Highlight = require('react-highlight');
    if (this.state.snapshot.length === 0)
    return (
        <div className="loading-warning">LOADING</div>
    )
    else
    return (
      <div>
        <div id="clone_form">
          <Form message="hello" currentid={this.state.currentid} data={this.state.snapshot}/>
        </div>
        <div id="code1">
              { JSON.stringify(this.state.snapshot[0]["code1"]) }
        </div>
        <div id="code2">
              { JSON.stringify(this.state.snapshot[0]["code2"]) }
        </div>
      </div>
    )
  }
}

export default App;
// export default ShoppingList;
