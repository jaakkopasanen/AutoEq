# Sennheiser RS 170
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.4; 31 -2.3; 34 -3.1; 37 -3.8; 41 -4.7; 45 -5.4; 49 -5.9; 54 -6.6; 60 -7.0; 66 -7.5; 72 -8.1; 79 -8.4; 87 -8.3; 96 -7.9; 106 -8.0; 116 -8.9; 128 -9.8; 141 -10.4; 155 -10.6; 170 -9.9; 187 -10.5; 206 -10.1; 227 -9.0; 249 -8.3; 274 -7.9; 302 -7.2; 332 -6.4; 365 -5.9; 402 -6.1; 442 -6.3; 486 -6.2; 535 -5.4; 588 -4.7; 647 -4.0; 712 -3.8; 783 -2.9; 861 -2.2; 947 -4.0; 1042 -4.3; 1146 -4.0; 1261 -6.0; 1387 -7.2; 1526 -8.7; 1678 -10.2; 1846 -5.9; 2031 -7.9; 2234 -8.8; 2457 -8.9; 2703 -8.7; 2973 -8.3; 3270 -8.1; 3597 -7.7; 3957 -6.1; 4353 -2.6; 4788 -0.5; 5267 -2.6; 5793 -2.3; 6373 -4.6; 7010 -4.7; 7711 -6.2; 8482 -6.8; 9330 -9.4; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 170 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 170 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.43 | 6.4 dB  |
| Peaking | 158 Hz  | 1.04 | -4.2 dB |
| Peaking | 844 Hz  | 1.22 | 5.0 dB  |
| Peaking | 3528 Hz | 0.42 | -4.6 dB |
| Peaking | 5008 Hz | 1.7  | 9.8 dB  |
| Peaking | 74 Hz   | 4.56 | -1.3 dB |
| Peaking | 352 Hz  | 5.95 | 1.1 dB  |
| Peaking | 1683 Hz | 6.17 | -3.6 dB |
| Peaking | 1853 Hz | 7.6  | 4.0 dB  |
| Peaking | 9503 Hz | 9.7  | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20170/Sennheiser%20RS%20170.png)