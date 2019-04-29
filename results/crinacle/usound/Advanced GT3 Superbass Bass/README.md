# Advanced GT3 Superbass Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.1; 25 -10.2; 28 -10.3; 31 -10.4; 34 -10.4; 37 -10.4; 41 -10.3; 45 -10.2; 49 -10.1; 54 -10.0; 60 -10.0; 66 -10.0; 72 -10.0; 79 -10.1; 87 -10.3; 96 -10.5; 106 -10.6; 116 -10.8; 128 -10.9; 141 -11.1; 155 -11.2; 170 -11.3; 187 -11.4; 206 -11.3; 227 -11.3; 249 -11.3; 274 -11.3; 302 -11.2; 332 -11.1; 365 -10.9; 402 -10.8; 442 -10.6; 486 -10.3; 535 -10.4; 588 -10.0; 647 -9.4; 712 -8.9; 783 -8.4; 861 -7.9; 947 -7.5; 1042 -7.3; 1146 -7.4; 1261 -7.5; 1387 -7.2; 1526 -6.5; 1678 -5.4; 1846 -4.1; 2031 -2.9; 2234 -1.9; 2457 -1.3; 2703 -1.0; 2973 -1.3; 3270 -1.9; 3597 -2.8; 3957 -3.6; 4353 -3.7; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -9.9; 16529 -12.0; 18182 -14.6; 20000 -15.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Superbass Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Superbass Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.62 | -3.3 dB |
| Peaking | 240 Hz   | 0.32 | -4.9 dB |
| Peaking | 2625 Hz  | 1.48 | 5.9 dB  |
| Peaking | 5744 Hz  | 2.6  | 6.1 dB  |
| Peaking | 19232 Hz | 0.69 | -9.9 dB |
| Peaking | 933 Hz   | 3.58 | 0.7 dB  |
| Peaking | 1370 Hz  | 4.9  | -1.0 dB |
| Peaking | 7880 Hz  | 6.07 | -1.2 dB |
| Peaking | 13052 Hz | 2.05 | 2.0 dB  |
| Peaking | 15741 Hz | 1.53 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20GT3%20Superbass%20Bass/Advanced%20GT3%20Superbass%20Bass.png)