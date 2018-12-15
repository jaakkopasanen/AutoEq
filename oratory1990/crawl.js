t = document.getElementsByClassName('s90z9tc-19 iDFCDm')[0]
rows = t.getElementsByTagName('tr')

manufacturer = '';
model = '';
results = {};
for (let i = 1; i < rows.length; ++i) {
    if (rows[i].children[0].innerText !== '-') {
        // Manufacturer not mentioned, use previous
        manufacturer = rows[i].children[0].innerText;
    }
    if (rows[i].children[1].innerText === '-') {
        // Model not mentioned, skip (only use first target of each model)
        continue;
    }
    model = rows[i].children[1].innerText;
    url = rows[i].children[2].children[0].href;
    url = url.replace('?dl=0', '?dl=1')
    results[manufacturer + ' ' + model] = url;
}
console.log(JSON.stringify(results));
