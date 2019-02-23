# Denon AH-C360
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.2; 25 -9.3; 28 -9.4; 31 -9.6; 34 -9.7; 37 -9.9; 41 -9.9; 45 -10.0; 49 -10.1; 54 -10.4; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.2; 87 -11.4; 96 -11.7; 106 -11.7; 116 -11.7; 128 -11.7; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.1; 206 -10.8; 227 -10.3; 249 -9.9; 274 -9.3; 302 -8.7; 332 -8.1; 365 -7.4; 402 -6.7; 442 -5.9; 486 -5.4; 535 -4.6; 588 -3.7; 647 -3.0; 712 -2.5; 783 -1.8; 861 -1.5; 947 -1.4; 1042 -1.4; 1146 -1.4; 1261 -1.4; 1387 -2.0; 1526 -2.7; 1678 -2.6; 1846 -0.9; 2031 -0.5; 2234 -1.0; 2457 -0.7; 2703 -1.0; 2973 -1.2; 3270 -1.5; 3597 -2.6; 3957 -4.3; 4353 -7.1; 4788 -8.9; 5267 -9.5; 5793 -8.9; 6373 -6.4; 7010 -4.7; 7711 -5.2; 8482 -6.0; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C360 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.23 | -3.2 dB |
| Peaking | 158 Hz  | 0.48 | -5.1 dB |
| Peaking | 828 Hz  | 0.93 | 4.1 dB  |
| Peaking | 2921 Hz | 0.75 | 5.2 dB  |
| Peaking | 5012 Hz | 2.25 | -7.2 dB |
| Peaking | 1290 Hz | 3.52 | 0.9 dB  |
| Peaking | 1623 Hz | 2.85 | -1.7 dB |
| Peaking | 1904 Hz | 5.61 | 1.9 dB  |
| Peaking | 7075 Hz | 4.73 | 2.9 dB  |
| Peaking | 7145 Hz | 2.03 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C360/Denon%20AH-C360.png)