# Yuin PK2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.9; 96 -2.1; 106 -3.0; 116 -3.7; 128 -4.3; 141 -4.8; 155 -5.1; 170 -5.3; 187 -5.4; 206 -5.4; 227 -5.5; 249 -5.5; 274 -5.4; 302 -5.3; 332 -5.1; 365 -4.9; 402 -5.4; 442 -5.4; 486 -4.8; 535 -4.8; 588 -5.0; 647 -5.2; 712 -5.4; 783 -5.6; 861 -5.9; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.5; 1387 -8.4; 1526 -9.7; 1678 -10.9; 1846 -11.8; 2031 -12.2; 2234 -12.2; 2457 -11.2; 2703 -9.7; 2973 -7.7; 3270 -6.1; 3597 -5.5; 3957 -7.0; 4353 -9.4; 4788 -10.9; 5267 -11.1; 5793 -11.2; 6373 -9.4; 7010 -7.0; 7711 -7.3; 8482 -9.4; 9330 -9.9; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.44 | 6.7 dB  |
| Peaking | 576 Hz   | 1.16 | 1.6 dB  |
| Peaking | 1995 Hz  | 2.07 | -6.4 dB |
| Peaking | 5359 Hz  | 3.13 | -4.8 dB |
| Peaking | 9450 Hz  | 3.18 | -2.4 dB |
| Peaking | 82 Hz    | 5.59 | 1.5 dB  |
| Peaking | 3497 Hz  | 3.39 | 5.4 dB  |
| Peaking | 3592 Hz  | 1.46 | -2.6 dB |
| Peaking | 11169 Hz | 4.85 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)