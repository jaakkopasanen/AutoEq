const rows = [].slice.call(document.getElementsByClassName('md wiki')[0].getElementsByTagName('tr'), 1);

const ignore = [
  'Harman AE/OE',
  'Harman IE',
  'oratory1990',
  'Diffuse Field',
  'Audeze Reveal Settings',
  '(?:(?:5|6|10) Band )?(?:(?:Old )?Android )?(?:Spotify )?(?:Graphic )?EQ',
  '(?:very )?preliminary(?:! \\(probably ignore bass shelf\\)?)?',
  '(?:(?:RME ADI-2)|(?:preferred)) setting',
  'v(?:1|2)',
  '-',
  '\\(|\\)',
];
const ignore_regexp = new RegExp(ignore.join('|'), 'g');

let manufacturer = '';
let model = '';
let notes = {};
const results = {};
rows.forEach(row => {
  new_manufacturer = row.children[0].innerText;
  if (new_manufacturer !== '-') {
    // New manufacturer, update
    manufacturer = new_manufacturer;
  }

  new_model = row.children[1].innerText;
  if (new_model !== '-') {
      // New model, update
      model = new_model;
      notes = {};
  }

  if (model === '') {
    return
  }


  new_notes = row.children[2].children[0].innerText.replace(ignore_regexp, '').trim();
  const full_name = manufacturer + ' ' + model;
  if (new_model !== '-' || !notes[new_notes]) {
    // Only add to results if this is a different model
    notes[new_notes] = true;
    const url = row.children[2].children[0].href.replace('?dl=0', '?dl=1');
    results[full_name + (new_notes ? ' (' + new_notes + ')' : '')] = url;
  }
});
console.log(JSON.stringify(results));
