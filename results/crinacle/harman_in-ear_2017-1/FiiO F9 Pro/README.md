# FiiO F9 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.3; 25 -7.5; 28 -7.7; 31 -7.9; 34 -8.0; 37 -8.2; 41 -8.3; 45 -8.5; 49 -8.6; 54 -8.7; 60 -8.9; 66 -9.1; 72 -9.2; 79 -9.4; 87 -9.6; 96 -9.9; 106 -10.0; 116 -10.0; 128 -10.1; 141 -10.1; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.3; 227 -9.0; 249 -8.6; 274 -8.2; 302 -7.8; 332 -7.2; 365 -6.8; 402 -6.4; 442 -6.0; 486 -5.6; 535 -5.2; 588 -4.8; 647 -4.3; 712 -4.0; 783 -3.7; 861 -3.5; 947 -3.7; 1042 -4.4; 1146 -5.5; 1261 -6.8; 1387 -7.7; 1526 -8.4; 1678 -9.2; 1846 -9.8; 2031 -9.5; 2234 -7.7; 2457 -5.0; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -2.8; 4353 -3.1; 4788 -3.2; 5267 -2.1; 5793 -1.7; 6373 -4.2; 7010 -10.2; 7711 -10.0; 8482 -9.0; 9330 -12.6; 10263 -14.6; 11289 -9.5; 12418 -6.5; 13660 -10.4; 15026 -19.8; 16529 -23.5; 18182 -21.6; 20000 -19.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F9 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F9 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 110 Hz   | 0.67 | -3.8 dB  |
| Peaking | 3228 Hz  | 3.39 | 6.7 dB   |
| Peaking | 5824 Hz  | 2.1  | 9.0 dB   |
| Peaking | 7170 Hz  | 1.87 | -6.1 dB  |
| Peaking | 17808 Hz | 0.74 | -17.9 dB |
| Peaking | 806 Hz   | 1.43 | 3.4 dB   |
| Peaking | 1790 Hz  | 2.61 | -4.5 dB  |
| Peaking | 10252 Hz | 3.8  | -8.5 dB  |
| Peaking | 12604 Hz | 1.46 | 9.0 dB   |
| Peaking | 15277 Hz | 2.35 | -8.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 16000 Hz | 1.41 | -18.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FiiO%20F9%20Pro/FiiO%20F9%20Pro.png)