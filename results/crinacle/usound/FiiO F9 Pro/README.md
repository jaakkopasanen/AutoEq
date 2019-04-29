# FiiO F9 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.8; 28 -5.1; 31 -5.3; 34 -5.4; 37 -5.6; 41 -5.7; 45 -5.9; 49 -6.0; 54 -6.1; 60 -6.3; 66 -6.4; 72 -6.6; 79 -6.8; 87 -7.0; 96 -7.2; 106 -7.3; 116 -7.4; 128 -7.5; 141 -7.4; 155 -7.4; 170 -7.2; 187 -7.0; 206 -6.7; 227 -6.3; 249 -6.0; 274 -5.6; 302 -5.2; 332 -4.8; 365 -4.4; 402 -4.1; 442 -3.7; 486 -3.4; 535 -3.0; 588 -2.7; 647 -2.2; 712 -1.9; 783 -1.6; 861 -1.4; 947 -1.5; 1042 -2.1; 1146 -3.3; 1261 -4.8; 1387 -6.1; 1526 -7.1; 1678 -7.9; 1846 -8.5; 2031 -8.6; 2234 -7.4; 2457 -5.3; 2703 -2.7; 2973 -0.8; 3270 -0.5; 3597 -1.6; 3957 -2.9; 4353 -2.8; 4788 -2.6; 5267 -1.5; 5793 -1.4; 6373 -4.2; 7010 -11.1; 7711 -11.5; 8482 -9.3; 9330 -10.1; 10263 -10.8; 11289 -6.6; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F9 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F9 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 873 Hz   | 1.33 | 4.9 dB   |
| Peaking | 2034 Hz  | 1.18 | -6.5 dB  |
| Peaking | 3032 Hz  | 1.76 | 7.7 dB   |
| Peaking | 5898 Hz  | 2.17 | 11.0 dB  |
| Peaking | 7202 Hz  | 1.42 | -11.6 dB |
| Peaking | 16 Hz    | 1.85 | 0.8 dB   |
| Peaking | 94 Hz    | 0.88 | -2.0 dB  |
| Peaking | 168 Hz   | 1.69 | -1.6 dB  |
| Peaking | 10325 Hz | 4.37 | -5.7 dB  |
| Peaking | 11098 Hz | 1.48 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FiiO%20F9%20Pro/FiiO%20F9%20Pro.png)