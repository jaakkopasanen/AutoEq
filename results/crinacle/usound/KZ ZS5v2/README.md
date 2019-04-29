# KZ ZS5v2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.7; 25 -8.1; 28 -8.5; 31 -8.8; 34 -9.1; 37 -9.4; 41 -9.7; 45 -9.9; 49 -10.0; 54 -10.1; 60 -10.4; 66 -10.6; 72 -10.8; 79 -11.0; 87 -11.3; 96 -11.5; 106 -11.5; 116 -11.6; 128 -11.6; 141 -11.6; 155 -11.5; 170 -11.3; 187 -11.0; 206 -10.6; 227 -10.2; 249 -9.8; 274 -9.3; 302 -8.8; 332 -8.3; 365 -7.7; 402 -7.2; 442 -6.7; 486 -6.2; 535 -5.7; 588 -5.2; 647 -4.7; 712 -4.2; 783 -3.7; 861 -3.4; 947 -3.3; 1042 -3.7; 1146 -4.5; 1261 -5.5; 1387 -6.4; 1526 -7.0; 1678 -7.5; 1846 -8.1; 2031 -8.5; 2234 -8.2; 2457 -6.8; 2703 -5.1; 2973 -4.0; 3270 -3.9; 3597 -4.1; 3957 -1.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -11.5; 8482 -14.0; 9330 -12.2; 10263 -12.8; 11289 -15.3; 12418 -17.2; 13660 -18.8; 15026 -16.4; 16529 -9.7; 18182 -8.5; 20000 -20.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 72 Hz    | 0.59 | -4.1 dB  |
| Peaking | 171 Hz   | 1.22 | -3.4 dB  |
| Peaking | 5769 Hz  | 1.18 | 9.4 dB   |
| Peaking | 8152 Hz  | 3.77 | -8.5 dB  |
| Peaking | 13256 Hz | 0.98 | -12.9 dB |
| Peaking | 292 Hz   | 2.45 | -1.0 dB  |
| Peaking | 868 Hz   | 1.33 | 3.5 dB   |
| Peaking | 2068 Hz  | 1.74 | -3.9 dB  |
| Peaking | 2981 Hz  | 1.62 | 1.6 dB   |
| Peaking | 20945 Hz | 2.76 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 16000 Hz | 1.41 | -12.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ZS5v2/KZ%20ZS5v2.png)