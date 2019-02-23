# Oppo PM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.9; 25 -4.2; 28 -4.5; 31 -4.7; 34 -4.9; 37 -5.0; 41 -4.8; 45 -4.4; 49 -3.8; 54 -4.9; 60 -6.7; 66 -6.9; 72 -7.0; 79 -7.4; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.4; 128 -8.5; 141 -8.9; 155 -9.0; 170 -9.0; 187 -9.2; 206 -9.0; 227 -8.9; 249 -8.8; 274 -9.2; 302 -9.3; 332 -9.0; 365 -8.1; 402 -7.2; 442 -7.2; 486 -7.9; 535 -8.1; 588 -7.9; 647 -7.8; 712 -8.0; 783 -8.2; 861 -8.4; 947 -7.5; 1042 -6.5; 1146 -5.9; 1261 -5.8; 1387 -7.0; 1526 -6.8; 1678 -6.8; 1846 -6.2; 2031 -5.7; 2234 -5.2; 2457 -4.3; 2703 -4.0; 2973 -3.8; 3270 -3.8; 3597 -3.8; 3957 -3.8; 4353 -3.6; 4788 -2.5; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.9; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.54 | 3.9 dB  |
| Peaking | 136 Hz  | 0.26 | -3.1 dB |
| Peaking | 2953 Hz | 1.83 | 2.3 dB  |
| Peaking | 5771 Hz | 2.11 | 6.3 dB  |
| Peaking | 8972 Hz | 3.83 | -4.0 dB |
| Peaking | 307 Hz  | 5.02 | -0.6 dB |
| Peaking | 413 Hz  | 5.71 | 1.6 dB  |
| Peaking | 882 Hz  | 2.51 | -2.0 dB |
| Peaking | 1146 Hz | 1.76 | 2.1 dB  |
| Peaking | 1457 Hz | 2.83 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)