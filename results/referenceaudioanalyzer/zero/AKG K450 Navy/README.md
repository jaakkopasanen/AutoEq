# AKG K450 Navy
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.3; 28 -5.7; 31 -5.9; 34 -6.1; 37 -6.2; 41 -6.4; 45 -6.6; 49 -6.8; 54 -6.9; 60 -7.1; 66 -7.2; 72 -7.2; 79 -7.4; 87 -7.6; 96 -7.8; 106 -8.1; 116 -8.2; 128 -8.2; 141 -8.2; 155 -8.1; 170 -7.9; 187 -7.8; 206 -7.5; 227 -7.1; 249 -6.8; 274 -6.6; 302 -6.5; 332 -6.2; 365 -5.9; 402 -5.4; 442 -4.9; 486 -4.1; 535 -3.5; 588 -2.8; 647 -1.9; 712 -1.6; 783 -2.8; 861 -4.7; 947 -5.6; 1042 -6.5; 1146 -7.5; 1261 -7.9; 1387 -7.4; 1526 -6.4; 1678 -5.0; 1846 -3.5; 2031 -2.3; 2234 -1.2; 2457 -0.5; 2703 -0.6; 2973 -2.1; 3270 -4.8; 3597 -7.5; 3957 -8.9; 4353 -8.5; 4788 -7.1; 5267 -7.4; 5793 -9.3; 6373 -9.5; 7010 -6.7; 7711 -5.2; 8482 -5.4; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K450 Navy GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K450 Navy ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 125 Hz  | 0.6  | -2.8 dB |
| Peaking | 650 Hz  | 3.12 | 4.4 dB  |
| Peaking | 2569 Hz | 2.74 | 6.2 dB  |
| Peaking | 3974 Hz | 3.23 | -4.3 dB |
| Peaking | 6090 Hz | 4.86 | -4.5 dB |
| Peaking | 16 Hz   | 1.84 | 1.1 dB  |
| Peaking | 484 Hz  | 4.87 | 0.9 dB  |
| Peaking | 771 Hz  | 7.63 | 1.6 dB  |
| Peaking | 1276 Hz | 2.21 | -3.1 dB |
| Peaking | 1956 Hz | 3.88 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K450%20Navy/AKG%20K450%20Navy.png)