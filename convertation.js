function RequestToServer(form, url) {
    const formData = new FormData(form);
    console.log('Sending request to server...');
    formData.append('key1', 'value1'); // Ensure this is required

    return new Promise((resolve, reject) => {
        fetch(url, {
            method: "POST",
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => resolve(data))
        .catch(error => {
            console.error('Error:', error);
            reject(error);
        });
    });
}

function convert() {
    const Form = document.querySelector('#full_form');
    const urlSearch = '/convert2';
    const res = document.getElementById('outputText');
    console.log('test')
    RequestToServer(Form, urlSearch)

    .then(response => {
        res.innerHTML = `<p>${response.message}</p>`;
    });


}
