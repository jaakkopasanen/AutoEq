# AKG K450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.2; 34 -1.7; 37 -2.1; 41 -2.7; 45 -3.2; 49 -3.7; 54 -4.0; 60 -4.3; 66 -4.7; 72 -5.1; 79 -5.6; 87 -5.9; 96 -6.2; 106 -6.6; 116 -6.9; 128 -7.1; 141 -7.4; 155 -7.7; 170 -8.0; 187 -8.3; 206 -8.3; 227 -8.6; 249 -8.4; 274 -8.3; 302 -8.1; 332 -8.0; 365 -7.9; 402 -7.7; 442 -7.4; 486 -7.3; 535 -6.9; 588 -6.3; 647 -6.0; 712 -6.6; 783 -7.9; 861 -9.2; 947 -9.8; 1042 -10.2; 1146 -10.1; 1261 -9.5; 1387 -8.9; 1526 -8.1; 1678 -6.5; 1846 -4.9; 2031 -3.8; 2234 -3.2; 2457 -2.8; 2703 -3.5; 2973 -5.2; 3270 -7.6; 3597 -9.9; 3957 -11.1; 4353 -10.7; 4788 -9.1; 5267 -6.8; 5793 -6.7; 6373 -7.5; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.43 | 6.0 dB  |
| Peaking | 42 Hz   | 1.77 | 2.3 dB  |
| Peaking | 1269 Hz | 1.03 | -5.8 dB |
| Peaking | 2360 Hz | 0.91 | 6.8 dB  |
| Peaking | 3896 Hz | 2.2  | -7.7 dB |
| Peaking | 68 Hz   | 2.15 | 0.9 dB  |
| Peaking | 231 Hz  | 0.87 | -2.0 dB |
| Peaking | 658 Hz  | 2.64 | 2.2 dB  |
| Peaking | 903 Hz  | 3.83 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K450/AKG%20K450.png)