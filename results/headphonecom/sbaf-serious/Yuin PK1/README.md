# Yuin PK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.8; 79 -1.7; 87 -2.4; 96 -3.0; 106 -3.3; 116 -3.4; 128 -3.6; 141 -3.8; 155 -4.0; 170 -4.0; 187 -4.2; 206 -4.1; 227 -4.2; 249 -4.1; 274 -4.2; 302 -4.1; 332 -4.2; 365 -4.2; 402 -4.4; 442 -4.8; 486 -5.0; 535 -5.1; 588 -5.2; 647 -5.4; 712 -5.6; 783 -5.9; 861 -6.2; 947 -6.6; 1042 -6.9; 1146 -7.1; 1261 -7.5; 1387 -8.1; 1526 -9.1; 1678 -10.1; 1846 -10.7; 2031 -11.1; 2234 -10.8; 2457 -9.8; 2703 -8.1; 2973 -6.3; 3270 -4.8; 3597 -4.4; 3957 -5.8; 4353 -8.2; 4788 -9.3; 5267 -9.5; 5793 -9.9; 6373 -10.4; 7010 -9.2; 7711 -8.8; 8482 -8.8; 9330 -8.3; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.38 | 6.4 dB  |
| Peaking | 366 Hz   | 0.65 | 1.8 dB  |
| Peaking | 2044 Hz  | 1.52 | -4.9 dB |
| Peaking | 3483 Hz  | 2.51 | 5.3 dB  |
| Peaking | 5613 Hz  | 1.06 | -4.0 dB |
| Peaking | 39 Hz    | 2.28 | -0.5 dB |
| Peaking | 66 Hz    | 3.06 | 1.0 dB  |
| Peaking | 97 Hz    | 2.56 | -0.5 dB |
| Peaking | 9208 Hz  | 3.8  | -1.1 dB |
| Peaking | 10793 Hz | 2.25 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK1/Yuin%20PK1.png)