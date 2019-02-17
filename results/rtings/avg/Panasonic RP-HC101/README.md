# Panasonic RP-HC101
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.4; 41 -2.9; 45 -4.1; 49 -5.2; 54 -6.3; 60 -7.2; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.6; 106 -9.9; 116 -10.2; 128 -10.5; 141 -10.6; 155 -10.7; 170 -10.8; 187 -10.7; 206 -10.6; 227 -10.4; 249 -10.4; 274 -10.6; 302 -10.7; 332 -11.0; 365 -12.0; 402 -12.8; 442 -13.4; 486 -13.5; 535 -13.0; 588 -12.2; 647 -11.2; 712 -10.1; 783 -8.9; 861 -7.8; 947 -6.9; 1042 -6.3; 1146 -6.1; 1261 -6.3; 1387 -7.0; 1526 -7.9; 1678 -9.3; 1846 -10.2; 2031 -10.0; 2234 -8.1; 2457 -5.8; 2703 -4.0; 2973 -3.8; 3270 -4.1; 3597 -3.4; 3957 -1.3; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -2.6; 6373 -5.8; 7010 -9.8; 7711 -12.6; 8482 -9.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.4; 16529 -13.9; 18182 -15.7; 20000 -17.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC101 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC101 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.72 | 9.0 dB  |
| Peaking | 97 Hz   | 0.31 | -4.9 dB |
| Peaking | 492 Hz  | 1.54 | -5.8 dB |
| Peaking | 4737 Hz | 1.84 | 7.2 dB  |
| Peaking | 7623 Hz | 3.94 | -7.9 dB |
| Peaking | 679 Hz  | 3.26 | -0.9 dB |
| Peaking | 1129 Hz | 1.7  | 2.0 dB  |
| Peaking | 1924 Hz | 2.23 | -4.9 dB |
| Peaking | 2714 Hz | 3.24 | 2.8 dB  |
| Peaking | 4693 Hz | 4.18 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -7.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC101/Panasonic%20RP-HC101.png)