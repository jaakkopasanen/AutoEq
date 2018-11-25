// Run in Chrome developer console on page https://www.rtings.com/headphones/reviews
function toUrl(str) {
    str = str.trim();
    str = str.replace(new RegExp('&amp;', 'g'), '-');
    str = str.replace(new RegExp(' & ', 'g'), '-');
    str = str.replace(new RegExp(' ', 'g'), '-');
    str = str.replace(new RegExp('&', 'g'), '-');
    str = str.replace(new RegExp('\\.', 'g'), '-');
    str = str.replace(new RegExp('\'', 'g'), '');
    str = str.replace(new RegExp('/', 'g'), '-');
    str = str.replace(new RegExp('\t', 'g'), '');
    str = str.replace(new RegExp('ö', 'g'), 'o');
    str = str.replace(new RegExp('Ö', 'g'), 'o');
    str = str.replace(new RegExp('ä', 'g'), 'a');
    str = str.replace(new RegExp('Ä', 'g'), 'a');
    str = str.toLowerCase();
    return str;
}
function toName(str) {
    str = str.trim();
    return str
}
//groups = document.getElementsByClassName('tree-node');

uls = document.getElementsByClassName('silo_reviews_page e-page')[0].children[1].children;
groups = [];
for (let i = 0; i < uls.length; ++i) {
	let lis = uls[i].children;
    for (let j = 0; j < lis.length; ++j) {
        groups.push(lis[j]);
    }
}

results = {};
for (let i = 0; i < groups.length; ++i) {
    manufacturer = groups[i].children[0].innerHTML;
    manufacturer = manufacturer.replace(new RegExp('&amp;', 'g'), '&');
    manufacturer = manufacturer.replace(new RegExp('\t', 'g'), '');

    for (let j = 0; j < groups[i].children[1].children.length; ++j) {
		model = groups[i].children[1].children[j].children[0].innerHTML;
		model = toName(model);
		if (model !== 'Lineup') {
        	url = 'https://www.rtings.com/images/graphs/headphones/' +
        	toUrl(manufacturer) + '/' +
        	toUrl(model) +
        	'/frequency-response-graph.png';
			results[manufacturer + ' ' + model] = url;
        }
    }
}
console.log(JSON.stringify(results));
