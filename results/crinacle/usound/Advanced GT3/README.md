# Advanced GT3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.1; 25 -7.0; 28 -6.9; 31 -6.8; 34 -6.8; 37 -6.7; 41 -6.7; 45 -6.6; 49 -6.5; 54 -6.4; 60 -6.4; 66 -6.5; 72 -6.6; 79 -6.7; 87 -7.0; 96 -7.2; 106 -7.5; 116 -7.7; 128 -7.8; 141 -7.9; 155 -8.0; 170 -8.0; 187 -8.0; 206 -7.9; 227 -7.8; 249 -7.6; 274 -7.4; 302 -7.2; 332 -6.9; 365 -6.5; 402 -6.2; 442 -5.8; 486 -5.3; 535 -4.9; 588 -4.3; 647 -3.8; 712 -3.1; 783 -2.5; 861 -1.9; 947 -1.5; 1042 -1.5; 1146 -1.9; 1261 -2.4; 1387 -2.4; 1526 -2.0; 1678 -1.4; 1846 -0.8; 2031 -0.6; 2234 -0.5; 2457 -0.9; 2703 -1.7; 2973 -2.8; 3270 -4.1; 3597 -5.3; 3957 -5.2; 4353 -5.2; 4788 -7.0; 5267 -9.6; 5793 -11.3; 6373 -9.3; 7010 -7.8; 7711 -10.2; 8482 -12.3; 9330 -8.6; 10263 -5.4; 11289 -5.4; 12418 -6.6; 13660 -11.4; 15026 -13.4; 16529 -13.1; 18182 -15.8; 20000 -24.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 174 Hz   | 0.42 | -2.6 dB  |
| Peaking | 891 Hz   | 1.19 | 3.6 dB   |
| Peaking | 2234 Hz  | 1.22 | 5.0 dB   |
| Peaking | 6154 Hz  | 1.44 | -4.7 dB  |
| Peaking | 20143 Hz | 0.47 | -17.6 dB |
| Peaking | 22 Hz    | 1.49 | -1.6 dB  |
| Peaking | 7034 Hz  | 7.55 | 3.1 dB   |
| Peaking | 8505 Hz  | 3.61 | -6.0 dB  |
| Peaking | 11036 Hz | 1.57 | 4.7 dB   |
| Peaking | 14359 Hz | 2.42 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 16000 Hz | 1.41 | -10.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20GT3/Advanced%20GT3.png)