document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('contact-form');

    Array.from(form.elements).forEach(element => {
        element.addEventListener('blur', function () {
            if (!this.checkValidity()) {
                this.classList.add('invalid');
            } else {
                this.classList.remove('invalid');
            }
        });
    });

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        validateForm();
    });

    function validateForm() {
        let isValid = true;
        Array.from(form.elements).forEach(element => {
            if (!element.checkValidity()) {
                element.classList.add('invalid');
                isValid = false;
            } else {
                element.classList.remove('invalid');
            }
        });
        if (isValid) {
            console.log('Form is valid and ready to be submitted!');
        }
    }
});
