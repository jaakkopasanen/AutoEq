# Hyla CE-5 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.2; 25 -6.2; 28 -6.2; 31 -6.2; 34 -6.2; 37 -6.2; 41 -6.1; 45 -6.1; 49 -6.0; 54 -5.9; 60 -5.9; 66 -5.8; 72 -5.8; 79 -5.9; 87 -5.9; 96 -5.9; 106 -5.8; 116 -5.7; 128 -5.6; 141 -5.4; 155 -5.2; 170 -4.9; 187 -4.6; 206 -4.2; 227 -3.8; 249 -3.4; 274 -3.1; 302 -2.7; 332 -2.4; 365 -2.0; 402 -1.8; 442 -1.5; 486 -1.3; 535 -1.1; 588 -1.0; 647 -0.8; 712 -0.7; 783 -0.6; 861 -0.6; 947 -0.9; 1042 -1.6; 1146 -2.8; 1261 -4.0; 1387 -5.1; 1526 -5.6; 1678 -5.7; 1846 -5.7; 2031 -5.7; 2234 -5.4; 2457 -4.8; 2703 -3.8; 2973 -2.9; 3270 -2.3; 3597 -2.4; 3957 -3.0; 4353 -3.9; 4788 -4.2; 5267 -2.7; 5793 -0.7; 6373 -0.5; 7010 -2.8; 7711 -2.8; 8482 -3.1; 9330 -3.2; 10263 -4.6; 11289 -3.1; 12418 -3.1; 13660 -4.0; 15026 -7.3; 16529 -3.2; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla CE-5 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla CE-5 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.17 | -3.1 dB |
| Peaking | 942 Hz   | 0.44 | 4.4 dB  |
| Peaking | 1645 Hz  | 1.11 | -6.3 dB |
| Peaking | 6102 Hz  | 6.7  | 3.2 dB  |
| Peaking | 14933 Hz | 4.43 | -4.7 dB |
| Peaking | 949 Hz   | 7.24 | 0.5 dB  |
| Peaking | 2369 Hz  | 4.66 | -1.0 dB |
| Peaking | 3407 Hz  | 2.38 | 1.5 dB  |
| Peaking | 4785 Hz  | 2.6  | -2.2 dB |
| Peaking | 5497 Hz  | 4.91 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hyla%20CE-5%20sample%201/Hyla%20CE-5%20sample%201.png)