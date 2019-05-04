# HiFiMan Ananda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.8; 34 -2.0; 37 -2.3; 41 -2.6; 45 -2.9; 49 -3.1; 54 -3.4; 60 -3.7; 66 -3.9; 72 -4.1; 79 -4.3; 87 -4.5; 96 -4.8; 106 -5.1; 116 -5.4; 128 -5.7; 141 -5.9; 155 -6.2; 170 -6.5; 187 -6.6; 206 -6.5; 227 -6.6; 249 -6.5; 274 -6.5; 302 -6.0; 332 -5.4; 365 -5.9; 402 -6.7; 442 -7.1; 486 -7.3; 535 -7.4; 588 -7.5; 647 -6.3; 712 -4.9; 783 -4.8; 861 -5.5; 947 -6.1; 1042 -4.8; 1146 -3.2; 1261 -3.6; 1387 -4.0; 1526 -3.0; 1678 -2.5; 1846 -3.6; 2031 -4.7; 2234 -5.4; 2457 -6.8; 2703 -7.0; 2973 -7.7; 3270 -7.2; 3597 -6.7; 3957 -6.4; 4353 -6.6; 4788 -6.4; 5267 -4.1; 5793 -3.1; 6373 -6.6; 7010 -8.4; 7711 -9.6; 8482 -8.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -6.8; 13660 -7.2; 15026 -7.4; 16529 -7.1; 18182 -9.4; 20000 -19.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.9  | 5.1 dB   |
| Peaking | 56 Hz    | 1.46 | 1.4 dB   |
| Peaking | 1191 Hz  | 5.02 | 2.5 dB   |
| Peaking | 1648 Hz  | 4.64 | 3.6 dB   |
| Peaking | 7848 Hz  | 4.79 | -4.4 dB  |
| Peaking | 201 Hz   | 2.19 | -1.0 dB  |
| Peaking | 515 Hz   | 3.53 | -1.8 dB  |
| Peaking | 3042 Hz  | 3.06 | -1.9 dB  |
| Peaking | 5627 Hz  | 8.36 | 3.9 dB   |
| Peaking | 19951 Hz | 1.3  | -13.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Ananda/HiFiMan%20Ananda.png)