function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    console.log('Username:', username);
    console.log('Password:', password);

    document.getElementById('output-username').value = username;
    document.getElementById('output-password').value = password;
}
