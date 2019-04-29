# Campfire Atlas
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.5; 25 -10.6; 28 -10.8; 31 -10.8; 34 -10.9; 37 -10.8; 41 -10.8; 45 -10.8; 49 -10.8; 54 -10.8; 60 -10.9; 66 -11.0; 72 -11.1; 79 -11.3; 87 -11.4; 96 -11.5; 106 -11.6; 116 -11.6; 128 -11.6; 141 -11.5; 155 -11.3; 170 -11.1; 187 -10.8; 206 -10.3; 227 -9.9; 249 -9.4; 274 -8.8; 302 -8.2; 332 -7.6; 365 -7.0; 402 -6.4; 442 -5.8; 486 -5.2; 535 -4.6; 588 -4.0; 647 -3.5; 712 -2.9; 783 -2.4; 861 -2.0; 947 -1.8; 1042 -2.0; 1146 -2.7; 1261 -3.3; 1387 -3.7; 1526 -3.6; 1678 -3.1; 1846 -2.5; 2031 -2.0; 2234 -1.5; 2457 -1.1; 2703 -0.6; 2973 -0.5; 3270 -0.7; 3597 -1.2; 3957 -1.7; 4353 -2.6; 4788 -4.6; 5267 -7.8; 5793 -7.9; 6373 -3.7; 7010 -2.9; 7711 -5.4; 8482 -8.9; 9330 -6.8; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Atlas GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Atlas ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.29 | -4.9 dB |
| Peaking | 154 Hz  | 0.59 | -4.8 dB |
| Peaking | 831 Hz  | 1.16 | 3.6 dB  |
| Peaking | 3010 Hz | 1.14 | 5.0 dB  |
| Peaking | 5419 Hz | 6.73 | -5.2 dB |
| Peaking | 1403 Hz | 7.36 | -0.6 dB |
| Peaking | 6812 Hz | 7.53 | 3.3 dB  |
| Peaking | 8642 Hz | 4.68 | -4.6 dB |
| Peaking | 9681 Hz | 4.8  | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Atlas/Campfire%20Atlas.png)