# Panasonic RP-HC800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.0; 25 -11.9; 28 -11.8; 31 -11.7; 34 -11.5; 37 -11.4; 41 -11.2; 45 -11.1; 49 -10.9; 54 -10.8; 60 -10.8; 66 -10.8; 72 -10.8; 79 -10.9; 87 -11.0; 96 -11.2; 106 -11.3; 116 -11.5; 128 -11.7; 141 -11.8; 155 -11.9; 170 -11.9; 187 -11.8; 206 -11.7; 227 -11.4; 249 -11.2; 274 -11.0; 302 -10.8; 332 -10.5; 365 -10.0; 402 -9.6; 442 -9.2; 486 -8.5; 535 -7.3; 588 -5.9; 647 -3.7; 712 -1.0; 783 -0.6; 861 -0.6; 947 -0.6; 1042 -0.6; 1146 -1.4; 1261 -2.2; 1387 -1.7; 1526 -1.3; 1678 -1.5; 1846 -3.1; 2031 -4.3; 2234 -6.1; 2457 -6.3; 2703 -3.0; 2973 -0.5; 3270 -1.7; 3597 -2.6; 3957 -3.8; 4353 -6.4; 4788 -7.7; 5267 -7.5; 5793 -10.0; 6373 -12.4; 7010 -9.0; 7711 -7.1; 8482 -8.2; 9330 -8.5; 10263 -9.5; 11289 -12.4; 12418 -11.8; 13660 -9.3; 15026 -10.4; 16529 -10.9; 18182 -9.6; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.99 | -3.5 dB |
| Peaking | 821 Hz   | 1.59 | 9.7 dB  |
| Peaking | 1147 Hz  | 0    | -4.6 dB |
| Peaking | 1485 Hz  | 1.58 | 7.1 dB  |
| Peaking | 3310 Hz  | 1.71 | 8.9 dB  |
| Peaking | 186 Hz   | 1.38 | -1.1 dB |
| Peaking | 6358 Hz  | 5.7  | -5.1 dB |
| Peaking | 7848 Hz  | 1.72 | 3.7 dB  |
| Peaking | 11702 Hz | 4.7  | -3.2 dB |
| Peaking | 13761 Hz | 3.17 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -5.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC800/Panasonic%20RP-HC800.png)