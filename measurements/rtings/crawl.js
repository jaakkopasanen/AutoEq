// Run in Chrome developer console on page https://www.rtings.com/headphones/1-2/graph
const name_replacements = [
    ['Harman/Kardon', 'Harman Kardon']
];

options = document.getElementById('product_select').children
data = {}
for (var i = 0; i < options.length; ++i) {
    var name = options[i].innerText.trim();
    name_replacements.forEach(([search, replacement]) => {
        name = name.replace(search, replacement);
    });
    data[name] = 'https://www.rtings.com/images/graphs/' + options[i].getAttribute('data-urlpart') + '/graph-frequency-response.json';
}
console.log(JSON.stringify(data))
