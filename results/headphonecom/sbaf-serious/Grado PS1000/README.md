# Grado PS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -2.0; 49 -3.0; 54 -4.3; 60 -5.6; 66 -6.6; 72 -7.5; 79 -8.3; 87 -8.8; 96 -9.0; 106 -9.0; 116 -8.8; 128 -8.4; 141 -7.9; 155 -7.4; 170 -7.0; 187 -6.4; 206 -6.0; 227 -5.5; 249 -5.3; 274 -4.9; 302 -4.4; 332 -3.9; 365 -3.2; 402 -3.7; 442 -3.6; 486 -3.5; 535 -3.4; 588 -3.2; 647 -3.2; 712 -3.1; 783 -3.1; 861 -3.2; 947 -3.4; 1042 -3.8; 1146 -4.1; 1261 -4.4; 1387 -5.1; 1526 -6.0; 1678 -5.8; 1846 -5.0; 2031 -4.8; 2234 -4.7; 2457 -4.7; 2703 -4.7; 2973 -4.9; 3270 -4.4; 3597 -4.7; 3957 -11.9; 4353 -10.9; 4788 -10.1; 5267 -11.3; 5793 -11.9; 6373 -15.8; 7010 -14.5; 7711 -13.0; 8482 -12.4; 9330 -11.4; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 32 Hz   |  0.57 | 7.4 dB   |
| Peaking | 94 Hz   |  0.77 | -6.7 dB  |
| Peaking | 1265 Hz |  0.07 | 3.1 dB   |
| Peaking | 4112 Hz |  8.25 | -5.4 dB  |
| Peaking | 6873 Hz |  1.26 | -11.3 dB |
| Peaking | 634 Hz  |  1.02 | 0.7 dB   |
| Peaking | 1564 Hz |  3.3  | -2.4 dB  |
| Peaking | 3535 Hz |  5.6  | 3.7 dB   |
| Peaking | 3820 Hz | 10.44 | -3.2 dB  |
| Peaking | 4875 Hz |  5.28 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | -7.6 dB |
| Peaking | 16000 Hz | 1.41 | 1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)