# Denon AH-D1100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.9; 25 -12.3; 28 -12.8; 31 -13.3; 34 -13.6; 37 -13.9; 41 -14.2; 45 -14.5; 49 -14.8; 54 -15.1; 60 -15.4; 66 -15.6; 72 -15.8; 79 -16.0; 87 -16.0; 96 -15.8; 106 -15.4; 116 -15.5; 128 -16.5; 141 -17.5; 155 -16.7; 170 -15.5; 187 -16.5; 206 -16.3; 227 -15.6; 249 -14.2; 274 -12.6; 302 -10.4; 332 -8.1; 365 -5.5; 402 -3.0; 442 -1.3; 486 -1.0; 535 -1.8; 588 -2.9; 647 -3.9; 712 -4.6; 783 -4.9; 861 -4.9; 947 -4.6; 1042 -4.1; 1146 -3.9; 1261 -3.9; 1387 -4.2; 1526 -5.3; 1678 -6.3; 1846 -7.4; 2031 -7.4; 2234 -6.3; 2457 -4.0; 2703 -1.6; 2973 -0.5; 3270 -2.2; 3597 -1.3; 3957 -0.5; 4353 -1.5; 4788 -5.1; 5267 -3.4; 5793 -2.0; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -8.3; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 0.79 | -7.8 dB |
| Peaking | 148 Hz  | 1.63 | -7.9 dB |
| Peaking | 232 Hz  | 2.38 | -8.5 dB |
| Peaking | 747 Hz  | 0.09 | 3.3 dB  |
| Peaking | 24 Hz   | 0.33 | -4.5 dB |
| Peaking | 466 Hz  | 4.27 | 4.5 dB  |
| Peaking | 1991 Hz | 1.93 | -4.7 dB |
| Peaking | 2854 Hz | 3.79 | 4.5 dB  |
| Peaking | 3980 Hz | 5.81 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | 7.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)