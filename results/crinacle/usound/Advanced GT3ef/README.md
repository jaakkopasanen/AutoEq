# Advanced GT3ef
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.6; 28 -5.7; 31 -5.7; 34 -5.7; 37 -5.6; 41 -5.6; 45 -5.5; 49 -5.5; 54 -5.5; 60 -5.4; 66 -5.5; 72 -5.8; 79 -5.9; 87 -6.0; 96 -6.3; 106 -6.5; 116 -6.6; 128 -6.8; 141 -7.0; 155 -7.1; 170 -7.1; 187 -7.1; 206 -7.0; 227 -6.9; 249 -6.7; 274 -6.5; 302 -6.3; 332 -6.0; 365 -5.7; 402 -5.3; 442 -5.0; 486 -4.5; 535 -4.0; 588 -3.5; 647 -3.0; 712 -2.4; 783 -1.7; 861 -1.2; 947 -0.9; 1042 -0.9; 1146 -1.3; 1261 -1.8; 1387 -1.9; 1526 -1.6; 1678 -1.0; 1846 -0.6; 2031 -0.5; 2234 -0.6; 2457 -1.4; 2703 -2.7; 2973 -4.5; 3270 -6.3; 3597 -7.2; 3957 -6.4; 4353 -5.7; 4788 -7.0; 5267 -9.4; 5793 -11.3; 6373 -9.1; 7010 -7.3; 7711 -9.8; 8482 -12.1; 9330 -8.1; 10263 -5.1; 11289 -5.1; 12418 -5.7; 13660 -10.8; 15026 -13.1; 16529 -13.0; 18182 -16.0; 20000 -24.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3ef GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3ef ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 187 Hz   | 0.6  | -2.2 dB  |
| Peaking | 939 Hz   | 1.07 | 4.1 dB   |
| Peaking | 2087 Hz  | 2.02 | 4.5 dB   |
| Peaking | 6035 Hz  | 1.33 | -4.5 dB  |
| Peaking | 19944 Hz | 0.53 | -18.0 dB |
| Peaking | 3445 Hz  | 7.52 | -2.0 dB  |
| Peaking | 7079 Hz  | 8.03 | 2.7 dB   |
| Peaking | 8517 Hz  | 3.86 | -6.4 dB  |
| Peaking | 11285 Hz | 1.22 | 5.0 dB   |
| Peaking | 14314 Hz | 2.27 | -4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20GT3ef/Advanced%20GT3ef.png)