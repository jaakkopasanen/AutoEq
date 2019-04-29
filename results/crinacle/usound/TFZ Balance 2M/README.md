# TFZ Balance 2M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.5; 25 -13.4; 28 -13.3; 31 -13.2; 34 -13.1; 37 -12.9; 41 -12.8; 45 -12.7; 49 -12.5; 54 -12.4; 60 -12.2; 66 -12.1; 72 -12.1; 79 -12.0; 87 -11.9; 96 -11.8; 106 -11.7; 116 -11.6; 128 -11.4; 141 -11.2; 155 -11.0; 170 -10.6; 187 -10.3; 206 -9.8; 227 -9.4; 249 -9.0; 274 -8.5; 302 -8.0; 332 -7.5; 365 -7.1; 402 -6.7; 442 -6.3; 486 -5.9; 535 -5.5; 588 -5.2; 647 -4.6; 712 -4.1; 783 -3.9; 861 -3.8; 947 -3.9; 1042 -4.4; 1146 -5.4; 1261 -6.5; 1387 -7.4; 1526 -7.9; 1678 -8.3; 1846 -8.7; 2031 -9.1; 2234 -8.6; 2457 -6.9; 2703 -4.7; 2973 -2.8; 3270 -1.5; 3597 -0.8; 3957 -0.8; 4353 -2.1; 4788 -4.9; 5267 -6.6; 5793 -2.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Balance 2M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Balance 2M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.26 | -7.3 dB |
| Peaking | 139 Hz  | 0.35 | -4.7 dB |
| Peaking | 1532 Hz | 0.32 | 6.2 dB  |
| Peaking | 1926 Hz | 0.94 | -9.7 dB |
| Peaking | 3447 Hz | 2.18 | 5.0 dB  |
| Peaking | 905 Hz  | 6.08 | 0.5 dB  |
| Peaking | 4264 Hz | 5.27 | 1.6 dB  |
| Peaking | 5203 Hz | 4.77 | -4.2 dB |
| Peaking | 6279 Hz | 3.71 | 6.7 dB  |
| Peaking | 7281 Hz | 1.28 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Balance%202M/TFZ%20Balance%202M.png)