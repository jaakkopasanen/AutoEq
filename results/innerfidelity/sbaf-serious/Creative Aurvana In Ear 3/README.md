# Creative Aurvana In Ear 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.2; 45 -1.9; 49 -2.4; 54 -3.1; 60 -3.9; 66 -4.6; 72 -5.2; 79 -5.9; 87 -6.6; 96 -7.3; 106 -7.8; 116 -8.2; 128 -8.6; 141 -9.1; 155 -9.4; 170 -9.6; 187 -9.7; 206 -9.8; 227 -9.7; 249 -9.8; 274 -9.6; 302 -9.5; 332 -9.3; 365 -9.0; 402 -8.7; 442 -8.3; 486 -8.1; 535 -7.7; 588 -7.1; 647 -6.8; 712 -6.6; 783 -6.2; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.0; 1387 -7.6; 1526 -8.1; 1678 -8.6; 1846 -8.5; 2031 -8.1; 2234 -7.4; 2457 -6.0; 2703 -4.7; 2973 -2.7; 3270 -1.2; 3597 -1.3; 3957 -2.7; 4353 -5.1; 4788 -6.1; 5267 -6.4; 5793 -7.3; 6373 -7.6; 7010 -7.4; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana In Ear 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana In Ear 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.59 | 6.6 dB  |
| Peaking | 189 Hz  | 0.61 | -3.9 dB |
| Peaking | 1865 Hz | 2.37 | -2.7 dB |
| Peaking | 3401 Hz | 2.54 | 6.2 dB  |
| Peaking | 6084 Hz | 2.78 | -1.6 dB |
| Peaking | 381 Hz  | 2.41 | -0.5 dB |
| Peaking | 792 Hz  | 2.49 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana%20In%20Ear%203/Creative%20Aurvana%20In%20Ear%203.png)