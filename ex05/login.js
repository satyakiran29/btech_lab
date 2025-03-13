function validtion(event){
    event.preventDefault();
const username = document.getElementById('username').value;
const password = document.getElementById('password').value;
const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');
usernameError.textContent = '';
passwordError.textContent = '';
let isValid = true;
const usernamePattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
if (!usernamePattern.test(username)) {
    usernameError.textContent = 'Invalid email';
    isValid = false;
    }
    if (password.length < 6) {
        passwordError.textContent = 'Password must be at least 6 characters';
        isValid = false;
    }
    if (isValid) {
        alert('Login successfully');
    }
    else {
        alert('Login failed');
    }
}