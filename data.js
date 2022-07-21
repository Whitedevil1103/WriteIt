import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.0/firebase-app.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/9.9.0/firebase-analytics.js";


const firebaseConfig = {
    apiKey: "AIzaSyBI1IVhOBYnURYkCEqdgVqPd9uFKw-C3j0",
    authDomain: "writeit-71930.firebaseapp.com",
    projectId: "writeit-71930",
    storageBucket: "writeit-71930.appspot.com",
    messagingSenderId: "1071369971138",
    appId: "1:1071369971138:web:c6a0404306520efe27a25b",
    measurementId: "G-YL1X367HSL",
    databaseURL: "https://WriteIt.firebaseio.com",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const database = getDatabase(app);


var datab = firebase.database().ref('data');
function UserRegister() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    firebase.auth().createUserWithEmailAndPassword(email, password).then(function () {

    }).catch(function (error) {
        var errorcode = error.code;
        var errormsg = error.message;
        window.location.href = 'index.html';

    });
    window.location.href = 'index.html';
}

const auth = firebase.auth();
function SignIn() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    const promise = auth.signInWithEmailAndPassword(email, password);
    promise.catch(e => alert(e.msg));
    window.location.href = 'index.html';

}

document.getElementById('form').addEventListener('submit', (e) => {
    e.preventDefault();
    var userinfo = datab.push();
    userinfo.set({
        name: getId('name'),
        email: getId('email'),
        password: getId('password')

    });
    alert("Successfully Registered")
    console.log("sent");
    document.getElementById('form').reset();
    window.location.href = 'index.html';
});

function getId(id) {
    return document.getElementById(id).value;
}



