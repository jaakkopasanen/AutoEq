# Focal Clear snA1BRQE000007
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.7; 25 -3.0; 28 -3.3; 31 -3.5; 34 -3.7; 37 -3.9; 41 -4.1; 45 -4.2; 49 -4.4; 54 -4.6; 60 -4.8; 66 -5.0; 72 -5.4; 79 -5.7; 87 -6.0; 96 -6.4; 106 -6.5; 116 -6.6; 128 -6.8; 141 -6.8; 155 -6.9; 170 -6.8; 187 -6.8; 206 -6.7; 227 -6.5; 249 -6.4; 274 -6.2; 302 -6.0; 332 -5.9; 365 -5.7; 402 -5.6; 442 -5.4; 486 -5.4; 535 -5.3; 588 -5.1; 647 -5.2; 712 -5.4; 783 -5.3; 861 -5.7; 947 -6.1; 1042 -6.5; 1146 -7.2; 1261 -7.6; 1387 -7.7; 1526 -7.2; 1678 -7.4; 1846 -6.9; 2031 -5.9; 2234 -5.4; 2457 -5.0; 2703 -5.2; 2973 -5.4; 3270 -5.6; 3597 -5.6; 3957 -2.4; 4353 -2.2; 4788 -1.9; 5267 -0.5; 5793 -3.1; 6373 -4.1; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Clear snA1BRQE000007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear snA1BRQE000007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.09 | 3.8 dB  |
| Peaking | 49 Hz   | 1.81 | 1.5 dB  |
| Peaking | 565 Hz  | 1.8  | 1.5 dB  |
| Peaking | 4125 Hz | 6.42 | 3.0 dB  |
| Peaking | 5233 Hz | 2.94 | 5.5 dB  |
| Peaking | 146 Hz  | 2.21 | -0.7 dB |
| Peaking | 1396 Hz | 2.64 | -1.5 dB |
| Peaking | 2474 Hz | 3.56 | 1.5 dB  |
| Peaking | 6761 Hz | 9.29 | 3.5 dB  |
| Peaking | 7494 Hz | 1.47 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Clear%20snA1BRQE000007/Focal%20Clear%20snA1BRQE000007.png)