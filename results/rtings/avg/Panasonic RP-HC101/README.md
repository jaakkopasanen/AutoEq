# Panasonic RP-HC101
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.2; 45 -2.4; 49 -3.5; 54 -4.5; 60 -5.5; 66 -6.2; 72 -6.7; 79 -7.1; 87 -7.5; 96 -7.8; 106 -8.2; 116 -8.5; 128 -8.7; 141 -8.9; 155 -9.0; 170 -9.0; 187 -9.0; 206 -8.8; 227 -8.7; 249 -8.7; 274 -8.8; 302 -9.0; 332 -9.3; 365 -10.2; 402 -11.1; 442 -11.7; 486 -11.8; 535 -11.2; 588 -10.5; 647 -9.5; 712 -8.3; 783 -7.1; 861 -6.0; 947 -5.2; 1042 -4.5; 1146 -4.3; 1261 -4.6; 1387 -5.3; 1526 -6.2; 1678 -7.6; 1846 -8.5; 2031 -8.2; 2234 -6.4; 2457 -4.0; 2703 -2.3; 2973 -2.0; 3270 -2.4; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -4.1; 7010 -8.1; 7711 -10.8; 8482 -8.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.6; 16529 -12.2; 18182 -13.9; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC101 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC101 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.61 | 7.9 dB  |
| Peaking | 98 Hz   | 0.42 | -3.6 dB |
| Peaking | 475 Hz  | 2.06 | -5.2 dB |
| Peaking | 4673 Hz | 1.12 | 7.1 dB  |
| Peaking | 7630 Hz | 3.73 | -7.3 dB |
| Peaking | 650 Hz  | 3.23 | -1.4 dB |
| Peaking | 1135 Hz | 1.53 | 2.9 dB  |
| Peaking | 1919 Hz | 2.44 | -4.2 dB |
| Peaking | 2702 Hz | 3.86 | 2.7 dB  |
| Peaking | 4534 Hz | 7.43 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -5.8 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC101/Panasonic%20RP-HC101.png)