const upload_form_1 = document.getElementById('upload_form_1');
const upload_input_1 = document.getElementById('upload_input_1');
const upload_button_1 = document.getElementById('upload_button_1');

let your_input_1 = upload_form_1.upload_file;

upload_button_1.addEventListener('click', () => {
    upload_input_1.click();
});

your_input_1.onchange = () => {
    upload_form_1.submit();
};

const upload_form_2 = document.getElementById('upload_form_2');
const upload_input_2 = document.getElementById('upload_input_2');
const upload_button_2 = document.getElementById('upload_button_2');

let your_input_2 = upload_form_2.upload_file;

upload_button_2.addEventListener('click', () => {
    upload_input_2.click();
});

your_input_2.onchange = () => {
    upload_form_2.submit();
};