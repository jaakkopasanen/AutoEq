# Bose QuietComfort 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.7; 28 -8.1; 31 -8.4; 34 -8.6; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.8; 60 -8.7; 66 -8.7; 72 -8.8; 79 -9.0; 87 -9.4; 96 -9.6; 106 -9.7; 116 -9.6; 128 -9.6; 141 -9.5; 155 -9.4; 170 -8.8; 187 -8.9; 206 -8.7; 227 -8.4; 249 -8.2; 274 -7.9; 302 -7.5; 332 -7.1; 365 -6.7; 402 -6.3; 442 -5.8; 486 -5.6; 535 -5.3; 588 -4.8; 647 -4.5; 712 -4.5; 783 -4.2; 861 -4.6; 947 -5.1; 1042 -5.6; 1146 -6.2; 1261 -6.8; 1387 -6.9; 1526 -7.3; 1678 -8.1; 1846 -8.5; 2031 -8.1; 2234 -7.5; 2457 -7.2; 2703 -5.8; 2973 -4.2; 3270 -2.4; 3597 -0.5; 3957 -6.6; 4353 -10.8; 4788 -8.1; 5267 -3.9; 5793 -8.5; 6373 -9.2; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 37 Hz   |  1.25 | -1.5 dB |
| Peaking | 124 Hz  |  0.57 | -3.1 dB |
| Peaking | 715 Hz  |  1.17 | 2.9 dB  |
| Peaking | 2965 Hz |  0.58 | -2.4 dB |
| Peaking | 3436 Hz |  4.32 | 8.6 dB  |
| Peaking | 1806 Hz |  5.88 | -1.0 dB |
| Peaking | 2782 Hz |  4.56 | 1.7 dB  |
| Peaking | 4319 Hz |  8.21 | -4.9 dB |
| Peaking | 5284 Hz | 13.12 | 4.5 dB  |
| Peaking | 7255 Hz | 12.08 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)