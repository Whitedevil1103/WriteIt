import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
const firebase = require("firebase");

var firebaseConfig = {
    apiKey: "AIzaSyBI1IVhOBYnURYkCEqdgVqPd9uFKw-C3j0",
    authDomain: "writeit-71930.firebaseapp.com",
    databaseURL: "https://writeit-71930-default-rtdb.firebaseio.com",
    projectId: "writeit-71930",
    storageBucket: "writeit-71930.appspot.com",
    messagingSenderId: "1071369971138",
    appId: "1:1071369971138:web:c6a0404306520efe27a25b",
    measurementId: "G-YL1X367HSL"
};
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
firebase.initializeApp(firebaseConfig);

var database = firebase.database();

// Submit form function
document.querySelector('#blog-form').addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form values
    var title = document.querySelector('#title').value;
    var content = document.querySelector('#content').value;

    // Save to Firebase database
    database.ref('blogs/').push({
        title: title,
        content: content
    });

    // Clear form values
    document.querySelector('#title').value = '';
    document.querySelector('#content').value = '';
});
