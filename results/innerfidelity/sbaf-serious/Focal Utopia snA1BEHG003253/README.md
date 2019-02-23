# Focal Utopia snA1BEHG003253
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.3; 25 -1.6; 28 -1.8; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.6; 45 -2.8; 49 -3.0; 54 -3.2; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.4; 87 -4.8; 96 -5.2; 106 -5.4; 116 -5.5; 128 -5.8; 141 -5.9; 155 -6.0; 170 -6.0; 187 -5.9; 206 -5.9; 227 -5.7; 249 -5.7; 274 -5.5; 302 -5.3; 332 -5.1; 365 -4.9; 402 -4.8; 442 -4.5; 486 -4.5; 535 -4.3; 588 -4.0; 647 -4.0; 712 -4.2; 783 -4.2; 861 -4.5; 947 -4.7; 1042 -5.0; 1146 -5.6; 1261 -6.3; 1387 -6.3; 1526 -5.6; 1678 -5.5; 1846 -4.7; 2031 -4.1; 2234 -4.1; 2457 -5.0; 2703 -5.0; 2973 -3.9; 3270 -3.3; 3597 -2.4; 3957 -5.4; 4353 -5.2; 4788 -3.2; 5267 -0.5; 5793 -2.8; 6373 -5.0; 7010 -2.3; 7711 -4.4; 8482 -6.8; 9330 -6.4; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -5.0; 18182 -6.9; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia snA1BEHG003253 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia snA1BEHG003253 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  1.05 | 3.5 dB  |
| Peaking | 1348 Hz  |  2.83 | -2.2 dB |
| Peaking | 3112 Hz  |  0.3  | 0.6 dB  |
| Peaking | 5311 Hz  |  8.16 | 4.2 dB  |
| Peaking | 8825 Hz  |  8.22 | -3.8 dB |
| Peaking | 168 Hz   |  1.26 | -1.5 dB |
| Peaking | 3557 Hz  |  7.41 | 2.5 dB  |
| Peaking | 4087 Hz  |  6.11 | -2.3 dB |
| Peaking | 6913 Hz  | 14.16 | 2.7 dB  |
| Peaking | 18252 Hz |  2.26 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Utopia%20snA1BEHG003253/Focal%20Utopia%20snA1BEHG003253.png)