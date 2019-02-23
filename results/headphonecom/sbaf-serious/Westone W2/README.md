# Westone W2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.1; 25 -6.2; 28 -6.3; 31 -6.3; 34 -6.4; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.0; 54 -7.2; 60 -7.5; 66 -7.8; 72 -8.1; 79 -8.4; 87 -9.0; 96 -9.3; 106 -9.5; 116 -9.8; 128 -9.9; 141 -10.1; 155 -10.4; 170 -10.5; 187 -10.7; 206 -10.7; 227 -10.6; 249 -10.6; 274 -10.6; 302 -10.3; 332 -10.1; 365 -9.7; 402 -9.6; 442 -9.3; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.3; 783 -7.1; 861 -7.2; 947 -7.5; 1042 -7.8; 1146 -8.2; 1261 -8.5; 1387 -9.1; 1526 -9.8; 1678 -10.2; 1846 -10.2; 2031 -10.0; 2234 -9.2; 2457 -7.3; 2703 -4.6; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.5; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 122 Hz  | 0.91 | -2.3 dB |
| Peaking | 268 Hz  | 0.8  | -3.5 dB |
| Peaking | 2032 Hz | 1.3  | -6.4 dB |
| Peaking | 3414 Hz | 1.34 | 8.5 dB  |
| Peaking | 5989 Hz | 3.92 | 4.6 dB  |
| Peaking | 25 Hz   | 1.15 | 0.6 dB  |
| Peaking | 1471 Hz | 5.86 | -0.4 dB |
| Peaking | 4517 Hz | 9.36 | 1.5 dB  |
| Peaking | 6657 Hz | 7.21 | 1.8 dB  |
| Peaking | 7731 Hz | 1.93 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20W2/Westone%20W2.png)