# Fostex T50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -1.2; 141 -2.7; 155 -3.1; 170 -3.0; 187 -3.1; 206 -3.3; 227 -3.5; 249 -3.6; 274 -3.8; 302 -4.1; 332 -4.3; 365 -4.8; 402 -5.9; 442 -5.8; 486 -5.5; 535 -5.7; 588 -5.7; 647 -5.8; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.2; 1042 -6.5; 1146 -6.2; 1261 -6.1; 1387 -6.3; 1526 -6.9; 1678 -7.3; 1846 -7.2; 2031 -7.5; 2234 -7.0; 2457 -6.1; 2703 -5.1; 2973 -4.6; 3270 -2.7; 3597 -2.6; 3957 -3.5; 4353 -2.4; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.27 | 6.1 dB  |
| Peaking | 107 Hz  | 1.78 | 2.2 dB  |
| Peaking | 258 Hz  | 1.43 | 1.5 dB  |
| Peaking | 3461 Hz | 4.38 | 3.1 dB  |
| Peaking | 5406 Hz | 2.26 | 6.7 dB  |
| Peaking | 75 Hz   | 3.58 | 0.2 dB  |
| Peaking | 1934 Hz | 3.56 | -1.4 dB |
| Peaking | 6527 Hz | 6.59 | 2.5 dB  |
| Peaking | 7736 Hz | 2.21 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 4.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50/Fostex%20T50.png)