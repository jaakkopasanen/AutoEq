# Focal Utopia snA1BEHG003253
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.3; 25 -1.6; 28 -1.8; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.6; 45 -2.8; 49 -3.0; 54 -3.2; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.4; 87 -4.8; 96 -5.2; 106 -5.4; 116 -5.5; 128 -5.8; 141 -5.9; 155 -6.0; 170 -6.0; 187 -5.9; 206 -5.9; 227 -5.7; 249 -5.7; 274 -5.5; 302 -5.3; 332 -5.1; 365 -4.9; 402 -4.8; 442 -4.5; 486 -4.5; 535 -4.3; 588 -4.0; 647 -4.0; 712 -4.2; 783 -4.2; 861 -4.5; 947 -4.7; 1042 -5.0; 1146 -5.6; 1261 -6.3; 1387 -6.3; 1526 -5.6; 1678 -5.5; 1846 -4.7; 2031 -4.1; 2234 -4.1; 2457 -5.0; 2703 -5.0; 2973 -3.9; 3270 -3.3; 3597 -2.4; 3957 -5.4; 4353 -5.2; 4788 -3.2; 5267 -0.5; 5793 -2.8; 6373 -5.0; 7010 -2.6; 7711 -4.7; 8482 -6.8; 9330 -6.5; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.1; 18182 -6.9; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia snA1BEHG003253 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia snA1BEHG003253 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.34 | 3.9 dB  |
| Peaking | 49 Hz    | 2.12 | 1.7 dB  |
| Peaking | 5293 Hz  | 6.41 | 4.9 dB  |
| Peaking | 6918 Hz  | 9.39 | 2.7 dB  |
| Peaking | 8857 Hz  | 7.68 | -3.0 dB |
| Peaking | 182 Hz   | 1.04 | -1.3 dB |
| Peaking | 904 Hz   | 0.56 | 1.3 dB  |
| Peaking | 1301 Hz  | 2.42 | -2.4 dB |
| Peaking | 3479 Hz  | 8.28 | 2.5 dB  |
| Peaking | 18306 Hz | 2.6  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Utopia%20snA1BEHG003253/Focal%20Utopia%20snA1BEHG003253.png)