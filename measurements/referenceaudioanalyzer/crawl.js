els = document.querySelectorAll('article.ar3')[0].children;

function toUrl(str) {
    str = str.trim();
    str = str.replace(new RegExp(' ', 'g'), '-');
    str = str.replace(new RegExp('&', 'g'), '');
    str = str.replace(new RegExp('\\.', 'g'), '');
    str = str.replace(new RegExp('\'', 'g'), '');
    str = str.replace(new RegExp('/', 'g'), '');
    str = str.replace(new RegExp('\t', 'g'), '');
    str = str.replace(new RegExp('ö', 'g'), 'o');
    str = str.replace(new RegExp('Ö', 'g'), 'o');
    str = str.replace(new RegExp('ä', 'g'), 'a');
    str = str.replace(new RegExp('Ä', 'g'), 'a');
    str = str.toLowerCase();
    return str;
}

var manufacturer = null;
var results = {};
for (var i = 0; i < els.length; ++i) {
    if (els[i].tagName === 'H3') {
        // Manufacturers are H3 elements
        manufacturer = els[i].innerText;
    } else if (els[i].tagName === 'A' && els[i].getAttribute('name') === null) {
        // Link to a headphone
        var fullName = els[i].innerText;
        var model = fullName.substr(manufacturer.length);
        var url = 'https://reference-audio-analyzer.pro/report/hp/';
        url += toUrl(manufacturer) + '/' + toUrl(fullName) + '/' + toUrl(fullName) + '_def.png';
        results[fullName] = url;
    }
}
console.log(JSON.stringify(results));
