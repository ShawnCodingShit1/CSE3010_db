//查找页面中的信息，并且监听提交按钮
document.getElementById('registration').addEventListener('click', function(event) {
    let arr = Array.from(document.querySelectorAll('input'))
    // 里面的值得顺序为页面结构的顺序
    let finalArr = []
    arr.forEach(item => {
        finalArr.push(item.value)
    })
    //防止默认的刷新行为
    event.preventDefault();
    //创建常量对象
    const formData = {
        useraccount: finalArr[0],
        userpassword: finalArr[1],
        phonenumber: finalArr[3],
        firstname: finalArr[4],
        lastname: finalArr[5],
        birthday: finalArr[6],
        email: finalArr[7]
    };
    
    fetch('https://httpbin.org/post', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData) 
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error))
})