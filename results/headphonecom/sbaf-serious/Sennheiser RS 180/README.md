# Sennheiser RS 180
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.7; 31 -3.4; 34 -4.0; 37 -4.5; 41 -5.0; 45 -5.5; 49 -5.9; 54 -6.1; 60 -6.3; 66 -7.2; 72 -7.5; 79 -7.5; 87 -8.0; 96 -8.3; 106 -8.6; 116 -8.5; 128 -8.6; 141 -8.8; 155 -8.9; 170 -8.9; 187 -9.0; 206 -8.7; 227 -8.1; 249 -7.8; 274 -7.7; 302 -7.2; 332 -6.8; 365 -6.5; 402 -6.2; 442 -5.9; 486 -5.5; 535 -5.2; 588 -5.0; 647 -4.6; 712 -4.6; 783 -3.6; 861 -2.5; 947 -3.0; 1042 -3.1; 1146 -2.8; 1261 -2.5; 1387 -2.2; 1526 -3.9; 1678 -6.2; 1846 -8.0; 2031 -9.1; 2234 -9.3; 2457 -7.5; 2703 -4.5; 2973 -0.9; 3270 -5.5; 3597 -1.3; 3957 -2.1; 4353 -3.4; 4788 -8.4; 5267 -7.3; 5793 -5.3; 6373 -6.1; 7010 -1.0; 7711 -4.9; 8482 -10.3; 9330 -11.5; 10263 -6.0; 11289 -3.2; 12418 -3.2; 13660 -3.2; 15026 -3.2; 16529 -3.2; 18182 -3.2; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.9  | -3.0 dB |
| Peaking | 199 Hz   | 0.66 | -4.9 dB |
| Peaking | 2107 Hz  | 3.68 | -6.8 dB |
| Peaking | 9040 Hz  | 4.45 | -9.5 dB |
| Peaking | 22050 Hz | 2.17 | -5.7 dB |
| Peaking | 21 Hz    | 2.47 | 3.4 dB  |
| Peaking | 1265 Hz  | 3.77 | 1.8 dB  |
| Peaking | 4163 Hz  | 2.74 | 5.5 dB  |
| Peaking | 4823 Hz  | 2.84 | -7.8 dB |
| Peaking | 7038 Hz  | 9.9  | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20180/Sennheiser%20RS%20180.png)