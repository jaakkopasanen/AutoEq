# Brainwavz B400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.4; 34 -2.0; 37 -2.6; 41 -3.3; 45 -3.9; 49 -4.5; 54 -5.1; 60 -5.7; 66 -6.4; 72 -7.0; 79 -7.7; 87 -8.4; 96 -9.1; 106 -9.7; 116 -10.2; 128 -10.7; 141 -11.2; 155 -11.6; 170 -11.9; 187 -12.1; 206 -12.2; 227 -12.2; 249 -12.2; 274 -12.1; 302 -11.8; 332 -11.4; 365 -11.2; 402 -10.9; 442 -10.5; 486 -10.0; 535 -9.5; 588 -8.9; 647 -8.3; 712 -7.6; 783 -6.9; 861 -6.3; 947 -6.0; 1042 -6.2; 1146 -6.6; 1261 -6.8; 1387 -6.6; 1526 -5.8; 1678 -4.7; 1846 -3.3; 2031 -1.8; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -1.3; 3270 -3.2; 3597 -4.1; 3957 -3.4; 4353 -1.2; 4788 -1.1; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -9.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.9; 15026 -19.7; 16529 -21.6; 18182 -19.0; 20000 -17.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz B400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz B400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.62 | 6.4 dB   |
| Peaking | 212 Hz   | 0.51 | -6.2 dB  |
| Peaking | 2413 Hz  | 1.89 | 6.2 dB   |
| Peaking | 5552 Hz  | 1.59 | 6.6 dB   |
| Peaking | 17451 Hz | 0.88 | -16.1 dB |
| Peaking | 912 Hz   | 3.43 | 1.4 dB   |
| Peaking | 1345 Hz  | 4.27 | -1.0 dB  |
| Peaking | 8928 Hz  | 3.98 | -3.4 dB  |
| Peaking | 13023 Hz | 1.53 | 6.8 dB   |
| Peaking | 15076 Hz | 2.68 | -8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 0.1 dB   |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -17.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Brainwavz%20B400/Brainwavz%20B400.png)