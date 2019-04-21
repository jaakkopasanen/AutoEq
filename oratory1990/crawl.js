const rows = [].slice.call(document.getElementsByClassName('md wiki')[0].getElementsByTagName('tr'), 1);

const ignore = [
  'Harman',
  'AE/OE 2018',
  'IE_2017',
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

const manufacturer_replacements = [
    ['Mee Audio', 'MEE Audio'],
    ['1More', '1MORE'],
];

const model_replacements = [
    [/DT(\d\d\d)/g, 'DT $1'],
    ['QC', 'QuietComfort '],
    ['WH1000XM2', 'WH-1000XM2'],
    ['/', ''],
    // Beyerdynamic transformations
    [/( (?:77|88|99)0)$/g, '$1 250 Ohm'],
    [/( (?:77|88|99)0)M$/g, '$1 M 80 Ohm'],
    // Sennheiser transformations
    [/(HD|IE|^CX)(\d(?:\.?)\d(?:\d|X|-1|))/g, '$1 $2'],
    [/((?:HD|IE) \d\d(?:\d|))(C?SR?)/g, '$1 $2'],
];

const massdrop = [
    'Beyerdynamic DT 177X Go',
    'Focal Elex',
    'Fostex T-X0',
    'Fostex TH-X00 Ebony',
    'Fostex TH-X00 Mahogany',
    'Fostex TH-X00 Purpleheart',
    'Hifiman Edition XX',
    'Hifiman HE4XX',
    'Hifiman HE35X',
    'Hifiman HE350',
    'Koss ESP95X',
    'MEE Audio Pinnacle PX',
    'MEE Audio Planamic IEM',
    'Meze 99 Noir',
    'NuForce EDC3',
    'NuForce Stride',
    'Sennheiser HD 58X',
    'Sennheiser PC37X',
]

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
    manufacturer_replacements.forEach(([search, replacement]) => {
        manufacturer = manufacturer.replace(search, replacement);
    });
  }

  new_model = row.children[1].innerText;
  if (new_model !== '-') {
      // New model, update
      model = new_model;
      model_replacements.forEach(([search, replacement]) => {
          model = model.replace(search, replacement);
      });
      notes = {};
  }

  new_notes = row.children[2].children[0].innerText.replace(ignore_regexp, '').trim();
  if (new_model !== '-' || !notes[new_notes]) {
    // Only add to results if this is a different model
    notes[new_notes] = true;
    const full_name = manufacturer + ' ' + model;
    const url = row.children[2].children[0].href.replace('?dl=0', '?dl=1');
    results[
        (massdrop.includes(full_name) ? 'Massdrop x ' : '') +
        full_name +
        (new_notes ? ' (' + new_notes + ')' : '')
    ] = url;
  }
});
console.log(JSON.stringify(results));
