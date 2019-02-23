# Focal Clear snA1BRQE000007
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.8; 25 -3.1; 28 -3.4; 31 -3.6; 34 -3.8; 37 -3.9; 41 -4.1; 45 -4.3; 49 -4.4; 54 -4.7; 60 -4.9; 66 -5.1; 72 -5.5; 79 -5.7; 87 -6.1; 96 -6.4; 106 -6.6; 116 -6.6; 128 -6.9; 141 -6.9; 155 -7.0; 170 -6.9; 187 -6.9; 206 -6.8; 227 -6.6; 249 -6.5; 274 -6.3; 302 -6.1; 332 -6.0; 365 -5.8; 402 -5.7; 442 -5.5; 486 -5.5; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.5; 783 -5.4; 861 -5.8; 947 -6.2; 1042 -6.6; 1146 -7.3; 1261 -7.7; 1387 -7.8; 1526 -7.3; 1678 -7.4; 1846 -6.9; 2031 -6.0; 2234 -5.5; 2457 -5.1; 2703 -5.3; 2973 -5.5; 3270 -5.6; 3597 -5.7; 3957 -2.5; 4353 -2.3; 4788 -2.0; 5267 -0.5; 5793 -3.2; 6373 -4.1; 7010 -3.1; 7711 -5.3; 8482 -7.0; 9330 -6.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Clear snA1BRQE000007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear snA1BRQE000007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 12 Hz   |  0.33 | 3.4 dB  |
| Peaking | 143 Hz  |  0.98 | -1.7 dB |
| Peaking | 1406 Hz |  2.11 | -2.4 dB |
| Peaking | 5060 Hz |  2.2  | 4.7 dB  |
| Peaking | 8854 Hz |  7.65 | -2.7 dB |
| Peaking | 613 Hz  |  2.39 | 0.7 dB  |
| Peaking | 3627 Hz |  5.22 | -1.9 dB |
| Peaking | 4042 Hz |  7.08 | 2.6 dB  |
| Peaking | 4623 Hz |  7.19 | -0.9 dB |
| Peaking | 6779 Hz | 16.4  | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Clear%20snA1BRQE000007/Focal%20Clear%20snA1BRQE000007.png)