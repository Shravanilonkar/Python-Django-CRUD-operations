function validateForm() {
    var pass1 = document.getElementById("password").value;
    var pass2 = document.getElementById("cpassword").value;
    var errorElement = document.getElementById("error-message1");
    if (pass1 != pass2) {
        errorElement.innerHTML = "Password does not match";
        return false;
    }
    else if (pass1.length < 5) {
        errorElement.innerHTML = "Password should have more than 5 characters";
        return false;
    }
    else if (pass1.length > 9) {
        errorElement.innerHTML = "Password should have less than 9 characters";
        return false;
    }
    else {
        errorElement.innerHTML = ""
        return true;
    }
}
function validateName() {
    var productName = document.getElementById("uname").value;
    var errorElement = document.getElementById("error-message");

    var nameRegex = /^[a-zA-Z0-9\s]+$/;

    if (productName.trim() === "") {
        errorElement.innerHTML = "Name is required.";
        return false;
    } else if (!nameRegex.test(productName)) {
        errorElement.innerHTML = "Invalid Name.Use only Alphabets.";
        return false;
    }

    errorElement.innerHTML = "";
    return true;
}
