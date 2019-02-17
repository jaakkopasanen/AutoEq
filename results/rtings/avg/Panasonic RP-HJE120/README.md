# Panasonic RP-HJE120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.3; 25 -4.6; 28 -5.0; 31 -5.3; 34 -5.5; 37 -5.7; 41 -5.9; 45 -6.1; 49 -6.3; 54 -6.6; 60 -7.1; 66 -7.6; 72 -8.0; 79 -8.4; 87 -9.0; 96 -9.5; 106 -10.1; 116 -10.5; 128 -11.0; 141 -11.4; 155 -11.6; 170 -11.7; 187 -11.6; 206 -11.4; 227 -11.1; 249 -10.5; 274 -9.9; 302 -9.4; 332 -9.1; 365 -8.5; 402 -7.8; 442 -7.0; 486 -6.1; 535 -5.1; 588 -4.1; 647 -2.8; 712 -1.8; 783 -1.4; 861 -1.6; 947 -2.0; 1042 -2.3; 1146 -2.6; 1261 -2.8; 1387 -2.9; 1526 -3.0; 1678 -3.3; 1846 -3.8; 2031 -4.2; 2234 -4.0; 2457 -3.6; 2703 -3.7; 2973 -3.8; 3270 -3.9; 3597 -4.0; 3957 -4.5; 4353 -5.6; 4788 -6.8; 5267 -8.3; 5793 -6.9; 6373 -3.8; 7010 -0.5; 7711 -1.9; 8482 -2.1; 9330 -4.2; 10263 -3.0; 11289 -2.2; 12418 -2.2; 13660 -2.2; 15026 -4.3; 16529 -6.0; 18182 -4.8; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 79 Hz    | 0.44 | -4.5 dB |
| Peaking | 179 Hz   | 0.92 | -6.7 dB |
| Peaking | 351 Hz   | 1.86 | -3.4 dB |
| Peaking | 2464 Hz  | 1.41 | -1.6 dB |
| Peaking | 5182 Hz  | 3.36 | -6.2 dB |
| Peaking | 505 Hz   | 3.06 | -1.0 dB |
| Peaking | 772 Hz   | 2.2  | 2.2 dB  |
| Peaking | 2239 Hz  | 0.24 | -0.2 dB |
| Peaking | 7104 Hz  | 6.94 | 3.1 dB  |
| Peaking | 20388 Hz | 0.38 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HJE120/Panasonic%20RP-HJE120.png)