# HiFiMan Ananda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.4; 31 -1.8; 34 -2.0; 37 -2.3; 41 -2.6; 45 -2.9; 49 -3.1; 54 -3.3; 60 -3.6; 66 -3.9; 72 -4.1; 79 -4.3; 87 -4.6; 96 -4.8; 106 -5.1; 116 -5.4; 128 -5.7; 141 -6.0; 155 -6.2; 170 -6.4; 187 -6.5; 206 -6.4; 227 -6.5; 249 -6.4; 274 -6.3; 302 -6.0; 332 -5.3; 365 -5.7; 402 -6.5; 442 -7.0; 486 -7.0; 535 -7.1; 588 -7.3; 647 -6.0; 712 -4.7; 783 -4.5; 861 -5.1; 947 -5.9; 1042 -4.6; 1146 -2.9; 1261 -3.1; 1387 -3.6; 1526 -2.7; 1678 -2.1; 1846 -3.0; 2031 -4.0; 2234 -4.4; 2457 -5.7; 2703 -6.1; 2973 -7.6; 3270 -7.1; 3597 -6.9; 3957 -6.6; 4353 -6.7; 4788 -5.8; 5267 -3.8; 5793 -3.0; 6373 -7.5; 7010 -7.8; 7711 -8.5; 8482 -9.1; 9330 -6.0; 10263 -5.7; 11289 -5.7; 12418 -6.4; 13660 -7.7; 15026 -7.5; 16529 -6.9; 18182 -9.1; 20000 -19.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.02 | 4.9 dB   |
| Peaking | 52 Hz    | 1.56 | 1.6 dB   |
| Peaking | 1186 Hz  | 5.21 | 2.5 dB   |
| Peaking | 1663 Hz  | 3.83 | 3.7 dB   |
| Peaking | 20018 Hz | 1.05 | -13.4 dB |
| Peaking | 499 Hz   | 2.85 | -1.7 dB  |
| Peaking | 3143 Hz  | 5.13 | -1.8 dB  |
| Peaking | 5614 Hz  | 5.77 | 5.3 dB   |
| Peaking | 8423 Hz  | 1.16 | -4.9 dB  |
| Peaking | 9975 Hz  | 2.2  | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Ananda/HiFiMan%20Ananda.png)