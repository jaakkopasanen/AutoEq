# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.2; 37 -1.8; 41 -2.5; 45 -3.1; 49 -3.6; 54 -4.0; 60 -4.5; 66 -4.5; 72 -4.3; 79 -4.6; 87 -4.7; 96 -4.6; 106 -5.1; 116 -5.4; 128 -5.9; 141 -6.0; 155 -6.1; 170 -5.9; 187 -5.2; 206 -4.7; 227 -5.3; 249 -5.5; 274 -5.3; 302 -5.1; 332 -4.8; 365 -4.6; 402 -4.6; 442 -4.3; 486 -4.4; 535 -4.4; 588 -4.2; 647 -3.2; 712 -3.7; 783 -3.6; 861 -3.8; 947 -4.0; 1042 -4.4; 1146 -4.9; 1261 -5.6; 1387 -6.7; 1526 -7.7; 1678 -8.2; 1846 -9.1; 2031 -9.9; 2234 -10.4; 2457 -9.9; 2703 -9.1; 2973 -8.3; 3270 -7.1; 3597 -5.6; 3957 -4.4; 4353 -6.5; 4788 -8.8; 5267 -8.7; 5793 -8.6; 6373 -6.7; 7010 -6.0; 7711 -11.4; 8482 -14.3; 9330 -13.9; 10263 -11.6; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.56 | 6.2 dB  |
| Peaking | 1259 Hz  | 0.33 | 4.0 dB  |
| Peaking | 2075 Hz  | 1.19 | -7.3 dB |
| Peaking | 9043 Hz  | 2.47 | -9.1 dB |
| Peaking | 11729 Hz | 3.04 | 1.9 dB  |
| Peaking | 97 Hz    | 4.77 | 0.7 dB  |
| Peaking | 143 Hz   | 4.87 | -0.6 dB |
| Peaking | 3871 Hz  | 4.56 | 4.1 dB  |
| Peaking | 5137 Hz  | 1.36 | -2.8 dB |
| Peaking | 6800 Hz  | 7.07 | 5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)