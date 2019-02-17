# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.3; 41 -2.1; 45 -2.8; 49 -3.4; 54 -4.1; 60 -4.9; 66 -5.6; 72 -6.2; 79 -6.8; 87 -7.4; 96 -8.0; 106 -8.6; 116 -9.1; 128 -9.5; 141 -9.8; 155 -10.1; 170 -10.1; 187 -10.1; 206 -9.9; 227 -9.6; 249 -9.4; 274 -9.3; 302 -9.1; 332 -8.9; 365 -8.7; 402 -8.4; 442 -8.3; 486 -8.4; 535 -8.1; 588 -7.3; 647 -7.2; 712 -7.0; 783 -6.9; 861 -6.7; 947 -6.5; 1042 -6.4; 1146 -6.3; 1261 -6.4; 1387 -6.6; 1526 -6.5; 1678 -6.4; 1846 -6.7; 2031 -7.3; 2234 -7.7; 2457 -7.5; 2703 -7.6; 2973 -7.7; 3270 -8.8; 3597 -9.3; 3957 -9.9; 4353 -11.1; 4788 -9.1; 5267 -7.5; 5793 -7.9; 6373 -6.7; 7010 -5.0; 7711 -6.2; 8482 -9.2; 9330 -10.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.5; 18182 -12.8; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.54 | 6.7 dB  |
| Peaking | 92 Hz    | 2.06 | 0.3 dB  |
| Peaking | 150 Hz   | 0.48 | -4.3 dB |
| Peaking | 4117 Hz  | 2.33 | -4.1 dB |
| Peaking | 19427 Hz | 1.18 | -9.4 dB |
| Peaking | 2296 Hz  | 5.85 | -0.7 dB |
| Peaking | 7160 Hz  | 6.09 | 2.4 dB  |
| Peaking | 9079 Hz  | 5.56 | -4.4 dB |
| Peaking | 16523 Hz | 0.77 | 1.8 dB  |
| Peaking | 17776 Hz | 2.41 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)