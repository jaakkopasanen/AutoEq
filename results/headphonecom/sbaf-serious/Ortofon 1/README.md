# Ortofon 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.8; 365 -4.0; 402 -6.7; 442 -8.1; 486 -8.6; 535 -8.4; 588 -7.7; 647 -5.3; 712 -5.6; 783 -5.9; 861 -6.2; 947 -6.2; 1042 -6.7; 1146 -6.0; 1261 -5.6; 1387 -6.0; 1526 -7.2; 1678 -6.9; 1846 -4.0; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -4.5; 4353 -4.7; 4788 -6.1; 5267 -7.7; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -8.3; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -7.7; 18182 -8.2; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 100 Hz  |  0.11 | 6.6 dB  |
| Peaking | 484 Hz  |  2.68 | -6.6 dB |
| Peaking | 2477 Hz |  0.31 | -6.6 dB |
| Peaking | 2766 Hz |  1.02 | 12.9 dB |
| Peaking | 6260 Hz |  4.75 | 7.8 dB  |
| Peaking | 307 Hz  |  5.26 | 2.1 dB  |
| Peaking | 1858 Hz |  2.85 | -3.7 dB |
| Peaking | 1996 Hz |  5.23 | 5.9 dB  |
| Peaking | 3613 Hz | 11.53 | 2.5 dB  |
| Peaking | 5146 Hz | 12.99 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%201/Ortofon%201.png)