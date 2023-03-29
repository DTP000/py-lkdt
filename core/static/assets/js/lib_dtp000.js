const getDataAPI = async (url) => {
    const response = await fetch(url);
    return response.status == 200 ? response.json() : null;
};
const add0Less10 = (number) => ('0' + number).slice(-2);

const timeConverter = (UNIX_timestamp) => {
    let d = new Date(UNIX_timestamp * 1000);
    let year = d.getFullYear();
    let month = add0Less10(d.getMonth() + 1);
    let date = add0Less10(d.getDate());
    let hour = add0Less10(d.getHours());
    let min = add0Less10(d.getMinutes());
    let sec = add0Less10(d.getSeconds());
    let time = `${hour}:${min}:${sec} ${date}-${month}-${year}`;
    return time;
}
// Example POST method implementation:
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}