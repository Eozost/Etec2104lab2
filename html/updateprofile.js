window.onload = function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();

        var name = document.getElementById('name').value;
        var dob = document.getElementById('birthdate').value;
        var email = document.getElementById('email').value;
        var image = document.getElementById('ppic').files[0];

        var regex = /^[a-zA-Z0-9 .]+$/; 
        if (!regex.test(name)) {
            alert('Invalid username. Only alphanumeric characters, spaces, and periods are allowed.');
            return;
        }

        document.querySelector('table tr:nth-child(2) td').textContent = 'Real Name: ' + name;
        document.querySelector('table tr:nth-child(3) td').textContent = 'Date of Birth: ' + dob;
        document.querySelector('table tr:nth-child(4) td').textContent = 'Email Address: ' + email;

        var reader = new FileReader();
        reader.onload = function(e) {
            document.querySelector('table tr:nth-child(1) td img').src = e.target.result;
        }
        reader.readAsDataURL(image);
    });
}