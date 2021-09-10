/**
    To customize your embedded form validation messages, place this code before the closing script tag.
 */
$mcj.extend($mcj.validator.messages, {
    required: "This field is required.",
    remote: "Please fix this field.",
    email: "Por favor, introduce una dirección de correo electrónico válida.",
    url: "Please enter a valid URL.",
    date: "Please enter a valid date.",
    dateISO: "Please enter a valid date (ISO).",
    number: "Please enter a valid number.",
    digits: "Please enter only digits.",
    creditcard: "Please enter a valid credit card number.",
    equalTo: "Please enter the same value again.",
    accept: "Porfavor introduzca un valor with a valid extension.",
    maxlength: $mcj.validator.format("Please enter no more than {0} characters."),
    minlength: $mcj.validator.format("Please enter at least {0} characters."),
    rangelength: $mcj.validator.format("Porfavor introduzca un valor between {0} and {1} characters long."),
    range: $mcj.validator.format("Porfavor introduzca un valor between {0} and {1}."),
    max: $mcj.validator.format("Porfavor introduzca un valor less than or equal to {0}."),
    min: $mcj.validator.format("Porfavor introduzca un valor greater than or equal to {0}."),
    mc_birthday: "Please enter a valid month and day.",
    mc_date: "Please enter a valid date.",
    mc_phone: "Please enter a valid phone number.",
    noSpace: 'There can be no spaces in this input.',

});