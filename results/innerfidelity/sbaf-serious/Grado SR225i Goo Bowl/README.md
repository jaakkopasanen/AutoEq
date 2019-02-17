# Grado SR225i Goo Bowl
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.5; 45 -2.6; 49 -3.3; 54 -4.0; 60 -5.1; 66 -6.1; 72 -6.8; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.6; 116 -8.7; 128 -8.9; 141 -8.8; 155 -8.7; 170 -8.5; 187 -8.3; 206 -8.0; 227 -7.7; 249 -7.5; 274 -7.1; 302 -7.1; 332 -7.1; 365 -6.8; 402 -6.8; 442 -6.6; 486 -6.6; 535 -6.5; 588 -6.2; 647 -6.2; 712 -6.2; 783 -6.0; 861 -6.3; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.4; 1387 -8.5; 1526 -9.4; 1678 -10.4; 1846 -12.3; 2031 -14.8; 2234 -13.6; 2457 -11.1; 2703 -9.5; 2973 -9.1; 3270 -7.9; 3597 -9.4; 3957 -8.3; 4353 -6.6; 4788 -7.0; 5267 -8.9; 5793 -7.3; 6373 -8.2; 7010 -11.3; 7711 -12.6; 8482 -14.4; 9330 -15.6; 10263 -10.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Goo Bowl GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Goo Bowl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.61 | 6.9 dB  |
| Peaking | 104 Hz   |  0.74 | -3.7 dB |
| Peaking | 2069 Hz  |  2.71 | -8.3 dB |
| Peaking | 3585 Hz  |  3.49 | -1.0 dB |
| Peaking | 8771 Hz  |  2.66 | -9.4 dB |
| Peaking | 788 Hz   |  1.44 | 0.8 dB  |
| Peaking | 1490 Hz  |  5.95 | -0.9 dB |
| Peaking | 4495 Hz  | 11.74 | 1.6 dB  |
| Peaking | 7203 Hz  |  9.59 | -1.9 dB |
| Peaking | 11486 Hz |  5.21 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Goo%20Bowl/Grado%20SR225i%20Goo%20Bowl.png)