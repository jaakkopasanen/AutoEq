# Yuin PK2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.5; 106 -2.4; 116 -3.1; 128 -3.7; 141 -4.2; 155 -4.5; 170 -4.7; 187 -4.8; 206 -4.8; 227 -4.9; 249 -4.9; 274 -4.8; 302 -4.7; 332 -4.5; 365 -4.3; 402 -4.8; 442 -4.8; 486 -4.2; 535 -4.2; 588 -4.3; 647 -4.5; 712 -4.8; 783 -5.0; 861 -5.3; 947 -5.7; 1042 -6.0; 1146 -6.3; 1261 -6.8; 1387 -7.8; 1526 -9.1; 1678 -10.3; 1846 -11.2; 2031 -11.6; 2234 -11.6; 2457 -10.6; 2703 -9.1; 2973 -7.1; 3270 -5.5; 3597 -4.9; 3957 -6.4; 4353 -8.8; 4788 -10.3; 5267 -10.5; 5793 -10.6; 6373 -8.8; 7010 -6.4; 7711 -6.6; 8482 -8.8; 9330 -9.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.38 | 6.6 dB  |
| Peaking | 576 Hz  | 0.9  | 2.1 dB  |
| Peaking | 1991 Hz | 2.25 | -5.9 dB |
| Peaking | 5375 Hz | 3.73 | -4.6 dB |
| Peaking | 9041 Hz | 6.06 | -3.0 dB |
| Peaking | 86 Hz   | 5.73 | 1.3 dB  |
| Peaking | 2524 Hz | 4.64 | -1.7 dB |
| Peaking | 3509 Hz | 3.02 | 3.1 dB  |
| Peaking | 4488 Hz | 6.18 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)