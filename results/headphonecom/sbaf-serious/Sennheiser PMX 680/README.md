# Sennheiser PMX 680
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.6; 25 -7.9; 28 -8.4; 31 -8.7; 34 -9.0; 37 -9.2; 41 -9.5; 45 -9.6; 49 -9.8; 54 -10.0; 60 -10.2; 66 -10.4; 72 -10.5; 79 -10.5; 87 -10.6; 96 -10.6; 106 -10.5; 116 -10.5; 128 -10.5; 141 -10.7; 155 -10.6; 170 -10.8; 187 -10.7; 206 -10.7; 227 -10.6; 249 -10.5; 274 -10.2; 302 -9.8; 332 -9.3; 365 -8.6; 402 -8.0; 442 -7.5; 486 -6.9; 535 -6.1; 588 -5.5; 647 -4.6; 712 -3.3; 783 -3.1; 861 -3.1; 947 -3.3; 1042 -3.8; 1146 -4.2; 1261 -4.7; 1387 -5.5; 1526 -6.4; 1678 -7.1; 1846 -7.5; 2031 -7.8; 2234 -8.0; 2457 -7.7; 2703 -6.5; 2973 -4.5; 3270 -2.0; 3597 -0.5; 3957 -1.7; 4353 -5.0; 4788 -8.5; 5267 -9.5; 5793 -4.3; 6373 -1.0; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PMX 680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 432 Hz  | 0.08 | -5.2 dB |
| Peaking | 847 Hz  | 0.8  | 8.5 dB  |
| Peaking | 3645 Hz | 2.55 | 9.2 dB  |
| Peaking | 5177 Hz | 3.65 | -6.0 dB |
| Peaking | 6241 Hz | 3.52 | 8.1 dB  |
| Peaking | 116 Hz  | 3.89 | 0.4 dB  |
| Peaking | 1311 Hz | 5.8  | 0.6 dB  |
| Peaking | 2275 Hz | 4.77 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX%20680/Sennheiser%20PMX%20680.png)