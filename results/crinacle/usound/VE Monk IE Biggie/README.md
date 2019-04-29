# VE Monk IE Biggie
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.1; 25 -7.4; 28 -7.8; 31 -8.1; 34 -8.4; 37 -8.6; 41 -8.9; 45 -9.1; 49 -9.4; 54 -9.7; 60 -10.1; 66 -10.5; 72 -10.8; 79 -11.3; 87 -11.7; 96 -12.2; 106 -12.8; 116 -13.2; 128 -13.6; 141 -14.1; 155 -14.4; 170 -14.7; 187 -15.0; 206 -15.2; 227 -15.4; 249 -15.6; 274 -15.7; 302 -15.8; 332 -15.8; 365 -15.8; 402 -15.6; 442 -15.3; 486 -14.8; 535 -14.0; 588 -13.0; 647 -11.6; 712 -10.0; 783 -8.2; 861 -6.4; 947 -4.9; 1042 -3.9; 1146 -3.5; 1261 -3.5; 1387 -3.8; 1526 -4.4; 1678 -5.1; 1846 -5.4; 2031 -4.5; 2234 -2.6; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -2.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VE Monk IE Biggie GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VE Monk IE Biggie ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 140 Hz  | 0.39 | -4.6 dB |
| Peaking | 495 Hz  | 0.41 | -8.2 dB |
| Peaking | 1031 Hz | 1.22 | 8.3 dB  |
| Peaking | 3074 Hz | 1.28 | 7.0 dB  |
| Peaking | 5820 Hz | 3.41 | 5.2 dB  |
| Peaking | 1939 Hz | 3.54 | -2.5 dB |
| Peaking | 2691 Hz | 1.26 | 2.9 dB  |
| Peaking | 3010 Hz | 3.33 | -3.2 dB |
| Peaking | 6602 Hz | 6.66 | 2.5 dB  |
| Peaking | 7347 Hz | 1.57 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.6 dB |
| Peaking | 500 Hz   | 1.41 | -8.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/VE%20Monk%20IE%20Biggie/VE%20Monk%20IE%20Biggie.png)