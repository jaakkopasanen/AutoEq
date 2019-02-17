# Denon AH-GC20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.4; 23 -15.6; 25 -15.7; 28 -15.9; 31 -16.0; 34 -15.9; 37 -15.8; 41 -15.7; 45 -15.6; 49 -15.5; 54 -15.3; 60 -15.1; 66 -14.8; 72 -14.5; 79 -14.1; 87 -13.8; 96 -13.3; 106 -12.9; 116 -12.5; 128 -12.0; 141 -11.5; 155 -10.9; 170 -10.3; 187 -9.7; 206 -9.1; 227 -8.5; 249 -8.2; 274 -8.1; 302 -8.3; 332 -8.7; 365 -9.3; 402 -10.2; 442 -11.0; 486 -10.9; 535 -9.6; 588 -8.3; 647 -7.3; 712 -6.9; 783 -6.9; 861 -7.2; 947 -7.2; 1042 -5.9; 1146 -3.8; 1261 -1.8; 1387 -0.7; 1526 -0.6; 1678 -0.6; 1846 -0.6; 2031 -0.6; 2234 -0.6; 2457 -0.6; 2703 -4.0; 2973 -4.3; 3270 -0.5; 3597 -5.6; 3957 -10.0; 4353 -4.6; 4788 -6.8; 5267 -4.5; 5793 -3.5; 6373 -8.0; 7010 -5.2; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -7.4; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-GC20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-GC20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 36 Hz    |  0.29 | -9.5 dB |
| Peaking | 465 Hz   |  2.79 | -4.2 dB |
| Peaking | 1414 Hz  |  3.15 | 4.5 dB  |
| Peaking | 2159 Hz  |  1.56 | 5.9 dB  |
| Peaking | 19709 Hz |  1.66 | -2.4 dB |
| Peaking | 248 Hz   |  3.95 | 0.9 dB  |
| Peaking | 934 Hz   |  6.89 | -1.6 dB |
| Peaking | 3317 Hz  | 11.15 | 5.1 dB  |
| Peaking | 3859 Hz  | 10.07 | -5.7 dB |
| Peaking | 5623 Hz  |  9.11 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Denon%20AH-GC20/Denon%20AH-GC20.png)