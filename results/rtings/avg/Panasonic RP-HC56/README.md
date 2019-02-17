# Panasonic RP-HC56
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -0.9; 25 -1.2; 28 -1.4; 31 -1.6; 34 -1.7; 37 -1.8; 41 -1.9; 45 -1.9; 49 -1.9; 54 -2.0; 60 -2.2; 66 -2.4; 72 -2.5; 79 -2.6; 87 -2.9; 96 -3.0; 106 -3.3; 116 -3.5; 128 -3.7; 141 -3.8; 155 -3.8; 170 -3.7; 187 -3.8; 206 -3.8; 227 -3.9; 249 -4.0; 274 -4.3; 302 -4.8; 332 -5.4; 365 -6.2; 402 -7.2; 442 -8.1; 486 -9.2; 535 -10.1; 588 -10.4; 647 -10.0; 712 -8.9; 783 -7.5; 861 -6.3; 947 -6.2; 1042 -6.7; 1146 -7.0; 1261 -6.4; 1387 -5.9; 1526 -5.1; 1678 -4.1; 1846 -3.2; 2031 -2.3; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -1.3; 4353 -1.6; 4788 -2.3; 5267 -5.4; 5793 -8.0; 6373 -7.5; 7010 -6.6; 7711 -9.2; 8482 -14.5; 9330 -18.1; 10263 -18.4; 11289 -15.7; 12418 -13.5; 13660 -12.8; 15026 -10.0; 16529 -8.9; 18182 -9.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.36 | 4.9 dB   |
| Peaking | 105 Hz   | 0.21 | 3.0 dB   |
| Peaking | 573 Hz   | 1.45 | -5.6 dB  |
| Peaking | 3370 Hz  | 0.78 | 7.3 dB   |
| Peaking | 10248 Hz | 1.2  | -12.9 dB |
| Peaking | 1256 Hz  | 3.53 | -1.3 dB  |
| Peaking | 5838 Hz  | 4.8  | -2.7 dB  |
| Peaking | 7476 Hz  | 3.19 | 3.8 dB   |
| Peaking | 9174 Hz  | 4.14 | -2.3 dB  |
| Peaking | 17804 Hz | 2.02 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.2 dB |
| Peaking | 16000 Hz | 1.41 | -5.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC56/Panasonic%20RP-HC56.png)