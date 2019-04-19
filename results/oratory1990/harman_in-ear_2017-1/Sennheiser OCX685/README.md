# Sennheiser OCX685
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.3; 25 -4.5; 28 -4.9; 31 -5.2; 34 -5.4; 37 -5.6; 41 -5.8; 45 -6.1; 49 -6.3; 54 -6.6; 60 -6.9; 66 -7.3; 72 -7.6; 79 -8.0; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.5; 128 -9.8; 141 -10.0; 155 -10.1; 170 -10.2; 187 -10.1; 206 -10.0; 227 -9.8; 249 -9.6; 274 -9.3; 302 -8.9; 332 -8.3; 365 -7.7; 402 -7.2; 442 -6.7; 486 -6.1; 535 -5.5; 588 -4.9; 647 -4.3; 712 -3.7; 783 -3.4; 861 -3.2; 947 -3.2; 1042 -3.5; 1146 -3.9; 1261 -4.1; 1387 -4.1; 1526 -3.9; 1678 -3.8; 1846 -3.7; 2031 -3.7; 2234 -3.7; 2457 -4.0; 2703 -4.2; 2973 -3.8; 3270 -3.2; 3597 -3.0; 3957 -3.5; 4353 -5.3; 4788 -8.5; 5267 -9.3; 5793 -4.9; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -8.1; 10263 -8.4; 11289 -5.6; 12418 -5.6; 13660 -7.4; 15026 -11.6; 16529 -12.0; 18182 -9.0; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser OCX685 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser OCX685 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 198 Hz   | 0.55 | -5.7 dB |
| Peaking | 1080 Hz  | 0.24 | 2.7 dB  |
| Peaking | 5078 Hz  | 5.55 | -6.1 dB |
| Peaking | 6372 Hz  | 6.41 | 5.7 dB  |
| Peaking | 16260 Hz | 1.39 | -7.2 dB |
| Peaking | 21 Hz    | 1.34 | 1.7 dB  |
| Peaking | 788 Hz   | 4.58 | 1.0 dB  |
| Peaking | 3695 Hz  | 6    | 1.6 dB  |
| Peaking | 9840 Hz  | 6.71 | -4.0 dB |
| Peaking | 12464 Hz | 3.51 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20OCX685/Sennheiser%20OCX685.png)