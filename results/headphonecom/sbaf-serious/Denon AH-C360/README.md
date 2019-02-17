# Denon AH-C360
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.1; 25 -8.3; 28 -8.6; 31 -8.8; 34 -9.0; 37 -9.2; 41 -9.4; 45 -9.5; 49 -9.7; 54 -10.0; 60 -10.3; 66 -10.5; 72 -10.8; 79 -11.0; 87 -11.2; 96 -11.3; 106 -11.4; 116 -11.4; 128 -11.4; 141 -11.4; 155 -11.3; 170 -11.2; 187 -10.9; 206 -10.5; 227 -10.0; 249 -9.6; 274 -9.1; 302 -8.4; 332 -7.6; 365 -7.0; 402 -6.5; 442 -5.9; 486 -5.3; 535 -4.4; 588 -3.5; 647 -2.6; 712 -1.9; 783 -1.3; 861 -0.8; 947 -1.1; 1042 -0.9; 1146 -0.8; 1261 -0.5; 1387 -0.8; 1526 -1.6; 1678 -1.7; 1846 -0.6; 2031 -1.2; 2234 -1.3; 2457 -1.0; 2703 -0.6; 2973 -0.5; 3270 -0.7; 3597 -1.3; 3957 -3.2; 4353 -5.5; 4788 -7.0; 5267 -7.6; 5793 -8.9; 6373 -8.5; 7010 -6.8; 7711 -7.3; 8482 -9.1; 9330 -7.8; 10263 -1.9; 11289 -1.1; 12418 -1.1; 13660 -1.1; 15026 -2.2; 16529 -1.2; 18182 -1.1; 20000 -1.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C360 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.29 | -7.8 dB |
| Peaking | 157 Hz   | 0.73 | -5.6 dB |
| Peaking | 320 Hz   | 1.26 | -3.2 dB |
| Peaking | 5759 Hz  | 2.16 | -7.8 dB |
| Peaking | 8652 Hz  | 3.96 | -7.4 dB |
| Peaking | 506 Hz   | 2.94 | -1.3 dB |
| Peaking | 865 Hz   | 1.19 | 1.2 dB  |
| Peaking | 3214 Hz  | 2.4  | 1.7 dB  |
| Peaking | 4457 Hz  | 5.49 | -2.2 dB |
| Peaking | 10890 Hz | 6.1  | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB |
| Peaking | 125 Hz   | 1.41 | -8.6 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -7.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C360/Denon%20AH-C360.png)