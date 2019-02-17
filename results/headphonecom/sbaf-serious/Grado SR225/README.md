# Grado SR225
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.9; 60 -3.2; 66 -4.2; 72 -5.1; 79 -5.8; 87 -6.4; 96 -6.9; 106 -7.3; 116 -7.6; 128 -7.6; 141 -7.6; 155 -7.6; 170 -7.6; 187 -7.5; 206 -7.5; 227 -7.3; 249 -7.2; 274 -7.2; 302 -7.1; 332 -6.6; 365 -6.2; 402 -6.1; 442 -6.3; 486 -6.1; 535 -6.0; 588 -6.0; 647 -5.8; 712 -5.8; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.5; 1387 -8.4; 1526 -9.6; 1678 -10.6; 1846 -11.3; 2031 -11.8; 2234 -12.0; 2457 -11.3; 2703 -11.1; 2973 -10.8; 3270 -10.7; 3597 -11.8; 3957 -15.8; 4353 -17.4; 4788 -14.8; 5267 -13.9; 5793 -14.7; 6373 -12.3; 7010 -8.9; 7711 -8.4; 8482 -12.3; 9330 -17.8; 10263 -17.8; 11289 -12.8; 12418 -9.7; 13660 -10.1; 15026 -9.9; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.36 | 7.8 dB   |
| Peaking | 100 Hz   | 0.7  | -5.8 dB  |
| Peaking | 2033 Hz  | 2.06 | -4.8 dB  |
| Peaking | 4477 Hz  | 1.85 | -9.6 dB  |
| Peaking | 9991 Hz  | 2.7  | -12.0 dB |
| Peaking | 707 Hz   | 1.6  | 1.1 dB   |
| Peaking | 4918 Hz  | 6.1  | 3.0 dB   |
| Peaking | 5920 Hz  | 2.12 | -2.9 dB  |
| Peaking | 7447 Hz  | 5.33 | 4.5 dB   |
| Peaking | 14514 Hz | 3.86 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | -6.8 dB |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR225/Grado%20SR225.png)