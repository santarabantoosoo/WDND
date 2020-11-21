document.getElementById('form').onsubmit = function (e) {
    e.preventDefault();
    // console.log(e)
    fetch(
        '/account/create', {
            method: 'POST',
            body: JSON.stringify({
                'first_name': document.getElementById('fname').value,
                'last_name': document.getElementById('lname').value,
                'balance': document.getElementById('ibalance').value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }
    ).then(function (response) {
        // console.log(response)
        return response.json();
    }).then(function (jsonRes) {
        console.log(jsonRes);
        const greetMessage = document.createElement('p');
        greetMessage.setAttribute('account_id', jsonRes.account_id);
        greetMessage.setAttribute('class', 'helloUser');
        greetMessage.innerHTML = 'Hello ' + jsonRes.first_name + ' ' + jsonRes.last_name + ' your account number is ' +
            jsonRes.account_id + ' and you have $' + jsonRes.balance;
        document.getElementById('greet').appendChild(greetMessage);
        document.getElementById('create_account').disabled = true;
        document.getElementById('open_account').disabled = true;
        document.querySelector('#panel').style.display = 'inline';

    })
}

// ACCESS ACCOUNT
document.getElementById('i_form').onsubmit = function (e) {
    const acc_id = document.getElementById('i_id').value;
    e.preventDefault();
    fetch('/account/' + acc_id + '/inquire', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        return response.json();
    }).then(function (jsonRes) {
        const greetMessage = document.createElement('p');
        greetMessage.setAttribute('account_id', jsonRes.account_id);
        greetMessage.setAttribute('class', 'helloUser');
        greetMessage.innerHTML = 'Hello ' + jsonRes.first_name + ' your account number is ' +
            jsonRes.account_id + ' and you have $' + jsonRes.balance;
        document.getElementById('greet').appendChild(greetMessage);

        if (jsonRes.svg_id != 'null') {
            console.log(jsonRes);
            const svg_message = document.createElement('p');
            svg_message.innerText = 'You have $' + jsonRes.svg_balance + ' in your savings account';
            svg_message.setAttribute('svg_id', jsonRes.svg_id)
            document.getElementById('greet').appendChild(svg_message);
            document.getElementById('svg_btn').style.display = 'none';

        } else {
            document.getElementById('svg_btn').style.display = 'inline';
        }


        document.getElementById('open_account').disabled = true;
        document.getElementById('create_account').disabled = true;
        document.querySelector('#panel').style.display = 'inline';
    })

};


// WITHDRAW FORM
document.getElementById('w_form').onsubmit = function (e) {
    e.preventDefault();
    const amount = document.getElementById('w_amount').value;
    // const user_id = document.getElementsByClassName('helloUser')[0].getAttribute('account_id');
    // console.log(document.getElementById('i_id').value);
    const user_id = document.getElementById('i_id').value
    fetch(
        '/account/' + user_id + '/withdraw', {
            method: 'POST',
            body: JSON.stringify({
                'amount': amount
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }
    ).then(response => {
        if (!response.ok) {
            throw response
        } else {
            return response.json();
        }
    }).then(function (jsonRes) {
        document.getElementById('op_message').innerHTML = '';
        console.log(jsonRes);
        const updatedBalance = document.createElement('p');
        updatedBalance.innerHTML = 'Your updated balance is ' + jsonRes.balance;
        document.getElementById('op_message').appendChild(updatedBalance);
        document.getElementById('withdraw_button').disabled = true;

    }).catch(error => {
        console.log(error);
        return error.json().then(jsonErr => {
            console.log(jsonErr)
            document.getElementById('op_message').innerHTML = '';
            const errorMessage = document.createElement('p');
            errorMessage.innerHTML = jsonErr.error;
            document.getElementById('op_message').appendChild(errorMessage);
            document.getElementById('withdraw_button').disabled = true;
        });
    });
}

// DEPOSIT FORM
document.getElementById('d_form').onsubmit = function (e) {
    e.preventDefault();
    const amount = document.getElementById('d_amount').value;
    // const user_id = document.getElementsByClassName('helloUser')[0].getAttribute('account_id');
    const user_id = document.getElementById('i_id').value
    fetch(
        '/account/' + user_id + '/deposit', {
            method: 'POST',
            body: JSON.stringify({
                'amount': amount
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }
    ).then(function (response) {
        return response.json();
    }).then(function (jsonRes) {
        document.getElementById('op_message').innerHTML = '';
        console.log(jsonRes);
        const updatedBalance = document.createElement('p');
        updatedBalance.innerHTML = 'Your updated balance is ' + jsonRes.balance;
        document.getElementById('op_message').appendChild(updatedBalance);
        document.getElementById('deposit_button').disabled = true;

    }).catch(err => {
        console.log(err);
    })
}

// DELETE ACCOUNT BY id
function confirm_delete() {
    // const user_id = document.getElementsByClassName('helloUser')[0].getAttribute('account_id');
    const user_id = document.getElementById('i_id').value
    // console.log(user_id)
    fetch(
        'account/' + user_id, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        }

    ).then(res => {
        document.location.href = "/";
    });
}

// CREATE SAVINGS ACCOUNT
function create_svg() {
    // const user_id = document.getElementsByClassName('helloUser')[0].getAttribute('account_id');
    const user_id = document.getElementById('i_id').value
    fetch(
        '/savings/' + user_id + '/create', {
            method: 'POST',
            body: JSON.stringify({
                'svg_init_balance': document.getElementById('s_amount').value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }
    ).then(function (response) {
        return response.json();
    }).then(function (jsonRes) {
        const created_svg = document.createElement('p');
        created_svg.innerHTML = 'You have successfully created savings account with balance ' + jsonRes.svg_balance;
        document.getElementById('op_message').appendChild(created_svg);
        document.getElementById('svg_submit').disabled = true;

    });
}



function withdraw() {
    document.getElementById('withdraw').style.display = 'inline';
    document.getElementById('deposit').style.display = 'none';
    document.getElementById('del').style.display = 'none';
    document.getElementById('sv').style.display = 'none';
}

function deposit() {
    document.getElementById('deposit').style.display = 'inline';
    document.getElementById('withdraw').style.display = 'none';
    document.getElementById('del').style.display = 'none';
    document.getElementById('sv').style.display = 'none';
}

function delete_account() {
    document.getElementById('deposit').style.display = 'none';
    document.getElementById('withdraw').style.display = 'none';
    document.getElementById('del').style.display = 'inline';
    document.getElementById('sv').style.display = 'none';
}

function create_saving() {
    document.getElementById('deposit').style.display = 'none';
    document.getElementById('withdraw').style.display = 'none';
    document.getElementById('del').style.display = 'none';
    document.getElementById('sv').style.display = 'inline';
}