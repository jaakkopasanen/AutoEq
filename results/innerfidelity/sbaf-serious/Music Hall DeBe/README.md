# Music Hall DeBe
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.7; 25 -2.2; 28 -2.9; 31 -3.5; 34 -4.0; 37 -4.4; 41 -4.8; 45 -5.2; 49 -5.6; 54 -6.0; 60 -6.5; 66 -6.9; 72 -7.4; 79 -7.9; 87 -8.5; 96 -9.1; 106 -9.6; 116 -10.0; 128 -10.6; 141 -11.0; 155 -11.4; 170 -11.6; 187 -11.7; 206 -12.2; 227 -12.5; 249 -12.8; 274 -12.7; 302 -12.5; 332 -12.6; 365 -12.5; 402 -12.2; 442 -12.0; 486 -11.7; 535 -10.5; 588 -8.8; 647 -7.7; 712 -7.8; 783 -8.2; 861 -9.1; 947 -9.6; 1042 -9.8; 1146 -9.8; 1261 -9.8; 1387 -9.6; 1526 -8.8; 1678 -7.7; 1846 -6.1; 2031 -4.3; 2234 -2.6; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -7.4; 5267 -6.8; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Music Hall DeBe GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Music Hall DeBe ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.53 | 6.5 dB  |
| Peaking | 320 Hz  | 0.44 | -9.1 dB |
| Peaking | 1100 Hz | 0.31 | 6.3 dB  |
| Peaking | 1355 Hz | 1.04 | -8.4 dB |
| Peaking | 2885 Hz | 1.17 | 5.1 dB  |
| Peaking | 662 Hz  | 7.71 | 1.6 dB  |
| Peaking | 4258 Hz | 4.99 | 4.0 dB  |
| Peaking | 5014 Hz | 3.8  | -8.1 dB |
| Peaking | 6072 Hz | 2.88 | 8.1 dB  |
| Peaking | 7286 Hz | 1.31 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Music%20Hall%20DeBe/Music%20Hall%20DeBe.png)