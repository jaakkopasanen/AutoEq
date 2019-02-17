# Sennheiser RS 170
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.4; 28 -3.5; 31 -4.5; 34 -5.2; 37 -5.9; 41 -6.8; 45 -7.5; 49 -8.1; 54 -8.7; 60 -9.2; 66 -9.6; 72 -10.2; 79 -10.6; 87 -10.4; 96 -10.0; 106 -10.1; 116 -11.0; 128 -11.9; 141 -12.5; 155 -12.7; 170 -12.1; 187 -12.7; 206 -12.2; 227 -11.1; 249 -10.4; 274 -10.0; 302 -9.3; 332 -8.5; 365 -8.0; 402 -8.2; 442 -8.4; 486 -8.3; 535 -7.5; 588 -6.8; 647 -6.2; 712 -5.9; 783 -5.0; 861 -4.3; 947 -6.2; 1042 -6.5; 1146 -6.2; 1261 -8.1; 1387 -9.3; 1526 -10.9; 1678 -12.4; 1846 -8.0; 2031 -10.1; 2234 -10.9; 2457 -11.0; 2703 -10.9; 2973 -10.4; 3270 -10.2; 3597 -9.8; 3957 -8.2; 4353 -4.7; 4788 -0.6; 5267 -4.7; 5793 -4.4; 6373 -6.7; 7010 -6.0; 7711 -6.3; 8482 -8.6; 9330 -11.5; 10263 -10.0; 11289 -6.7; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 170 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 170 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.98 | 6.5 dB  |
| Peaking | 149 Hz  | 0.74 | -6.0 dB |
| Peaking | 1620 Hz | 6.92 | -4.0 dB |
| Peaking | 4131 Hz | 0.87 | -9.6 dB |
| Peaking | 4758 Hz | 2.16 | 14.4 dB |
| Peaking | 67 Hz   | 3.67 | -1.3 dB |
| Peaking | 829 Hz  | 3.03 | 3.1 dB  |
| Peaking | 2322 Hz | 5.41 | -1.6 dB |
| Peaking | 9068 Hz | 1.4  | 3.4 dB  |
| Peaking | 9488 Hz | 3.63 | -7.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20170/Sennheiser%20RS%20170.png)