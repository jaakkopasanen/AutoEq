# Lime Ears Aether Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.0; 25 -13.0; 28 -13.0; 31 -13.0; 34 -12.9; 37 -12.9; 41 -12.8; 45 -12.7; 49 -12.6; 54 -12.4; 60 -12.2; 66 -12.2; 72 -12.2; 79 -12.1; 87 -12.1; 96 -12.1; 106 -12.1; 116 -11.9; 128 -11.8; 141 -11.7; 155 -11.5; 170 -11.3; 187 -11.0; 206 -10.7; 227 -10.4; 249 -10.0; 274 -9.7; 302 -9.2; 332 -8.7; 365 -8.2; 402 -7.8; 442 -7.5; 486 -7.2; 535 -6.9; 588 -6.7; 647 -6.7; 712 -6.7; 783 -6.8; 861 -6.9; 947 -7.2; 1042 -7.7; 1146 -8.3; 1261 -8.8; 1387 -8.7; 1526 -8.1; 1678 -7.2; 1846 -6.3; 2031 -5.3; 2234 -4.3; 2457 -3.8; 2703 -3.4; 2973 -2.4; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -3.7; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -9.5; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -13.2; 16529 -15.4; 18182 -15.7; 20000 -18.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Aether Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Aether Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.13 | -6.4 dB  |
| Peaking | 1355 Hz  | 2.73 | -2.9 dB  |
| Peaking | 3779 Hz  | 1.28 | 6.5 dB   |
| Peaking | 6273 Hz  | 5.83 | 4.5 dB   |
| Peaking | 19160 Hz | 0.55 | -11.4 dB |
| Peaking | 200 Hz   | 1.57 | -0.6 dB  |
| Peaking | 536 Hz   | 1.7  | 0.9 dB   |
| Peaking | 9219 Hz  | 4.89 | -3.6 dB  |
| Peaking | 13614 Hz | 1.38 | 4.7 dB   |
| Peaking | 15622 Hz | 2.32 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -9.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Aether%20Bass/Lime%20Ears%20Aether%20Bass.png)