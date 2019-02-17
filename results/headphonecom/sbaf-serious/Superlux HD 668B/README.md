# Superlux HD 668B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -1.1; 37 -2.3; 41 -3.9; 45 -5.3; 49 -6.5; 54 -8.1; 60 -9.7; 66 -10.7; 72 -11.3; 79 -11.0; 87 -11.0; 96 -11.0; 106 -11.5; 116 -11.3; 128 -10.9; 141 -10.8; 155 -10.6; 170 -10.1; 187 -9.6; 206 -9.4; 227 -8.7; 249 -8.5; 274 -8.5; 302 -8.4; 332 -7.8; 365 -7.4; 402 -7.3; 442 -7.2; 486 -7.1; 535 -6.9; 588 -6.7; 647 -5.6; 712 -5.9; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -8.4; 1526 -10.0; 1678 -11.0; 1846 -12.3; 2031 -12.2; 2234 -11.6; 2457 -10.7; 2703 -9.8; 2973 -8.4; 3270 -7.2; 3597 -6.0; 3957 -6.3; 4353 -7.9; 4788 -8.4; 5267 -8.5; 5793 -16.0; 6373 -10.5; 7010 -10.2; 7711 -13.1; 8482 -15.4; 9330 -15.5; 10263 -12.2; 11289 -7.1; 12418 -6.9; 13660 -10.7; 15026 -12.4; 16529 -12.4; 18182 -9.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 26 Hz    |  2.69 | 7.7 dB  |
| Peaking | 1983 Hz  |  2.14 | -6.1 dB |
| Peaking | 8468 Hz  |  1.67 | -8.7 dB |
| Peaking | 14903 Hz |  3.71 | -4.3 dB |
| Peaking | 17016 Hz |  2.16 | -5.5 dB |
| Peaking | 37 Hz    |  1.82 | 4.9 dB  |
| Peaking | 92 Hz    |  0.57 | -5.5 dB |
| Peaking | 3743 Hz  |  5.13 | 2.2 dB  |
| Peaking | 5714 Hz  | 10.94 | -8.4 dB |
| Peaking | 7004 Hz  |  5.36 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Superlux%20HD%20668B/Superlux%20HD%20668B.png)