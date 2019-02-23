# Sennheiser RS 180
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.7; 31 -3.4; 34 -4.0; 37 -4.5; 41 -5.0; 45 -5.5; 49 -5.9; 54 -6.1; 60 -6.3; 66 -7.2; 72 -7.5; 79 -7.5; 87 -8.0; 96 -8.3; 106 -8.6; 116 -8.5; 128 -8.6; 141 -8.8; 155 -8.9; 170 -8.9; 187 -9.0; 206 -8.7; 227 -8.1; 249 -7.8; 274 -7.7; 302 -7.2; 332 -6.8; 365 -6.5; 402 -6.2; 442 -5.9; 486 -5.5; 535 -5.2; 588 -5.0; 647 -4.6; 712 -4.6; 783 -3.6; 861 -2.5; 947 -3.0; 1042 -3.1; 1146 -2.8; 1261 -2.5; 1387 -2.2; 1526 -3.9; 1678 -6.2; 1846 -8.0; 2031 -9.1; 2234 -9.3; 2457 -7.5; 2703 -4.5; 2973 -0.9; 3270 -5.5; 3597 -1.3; 3957 -2.1; 4353 -3.4; 4788 -8.4; 5267 -7.3; 5793 -5.3; 6373 -6.1; 7010 -3.5; 7711 -5.8; 8482 -10.3; 9330 -11.5; 10263 -6.6; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.42 | 5.8 dB  |
| Peaking | 1259 Hz | 1.26 | 5.0 dB  |
| Peaking | 2191 Hz | 1.69 | -8.3 dB |
| Peaking | 2957 Hz | 1.63 | 6.7 dB  |
| Peaking | 9041 Hz | 6.1  | -6.9 dB |
| Peaking | 153 Hz  | 0.74 | -3.1 dB |
| Peaking | 665 Hz  | 1.42 | 0.8 dB  |
| Peaking | 4061 Hz | 5.76 | 2.7 dB  |
| Peaking | 4927 Hz | 6.97 | -4.5 dB |
| Peaking | 6930 Hz | 9.58 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20180/Sennheiser%20RS%20180.png)