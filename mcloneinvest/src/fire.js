import firebase from 'firebase'
var config = {
  apiKey: "AIzaSyBVW19g-4x85V4AEPdVO8fPE5p9CbtWIi4",
  authDomain: "cloverflow-4dd16.firebaseapp.com",
  databaseURL: "https://cloverflow-4dd16.firebaseio.com",
  projectId: "cloverflow-4dd16",
  storageBucket: "cloverflow-4dd16.appspot.com",
  messagingSenderId: "242250119195"
};
var fire = firebase.initializeApp(config);
export default fire;
