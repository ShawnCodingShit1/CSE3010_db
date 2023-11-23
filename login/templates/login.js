
document.getElementById('login').addEventListener('submit', function(event) {
    event.preventDefault();
    
    //只读
    const loginData = {
        useraccount: this.useraccount.value,
        userpassword: this.userpassword.value,
    };
    fetch('https://httpbin.org/post', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(loginData) 
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));

});