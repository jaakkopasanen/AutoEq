# Creative Aurvana In Ear 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.2; 49 -1.8; 54 -2.5; 60 -3.2; 66 -3.9; 72 -4.6; 79 -5.2; 87 -5.9; 96 -6.6; 106 -7.1; 116 -7.5; 128 -7.9; 141 -8.5; 155 -8.7; 170 -8.9; 187 -9.1; 206 -9.2; 227 -9.1; 249 -9.2; 274 -9.0; 302 -8.8; 332 -8.6; 365 -8.4; 402 -8.1; 442 -7.7; 486 -7.4; 535 -7.1; 588 -6.4; 647 -6.1; 712 -6.0; 783 -5.5; 861 -5.6; 947 -5.7; 1042 -5.9; 1146 -6.1; 1261 -6.4; 1387 -7.0; 1526 -7.5; 1678 -7.9; 1846 -7.8; 2031 -7.5; 2234 -6.8; 2457 -5.4; 2703 -4.1; 2973 -2.0; 3270 -0.6; 3597 -0.7; 3957 -2.0; 4353 -4.5; 4788 -5.5; 5267 -5.8; 5793 -6.7; 6373 -7.0; 7010 -6.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana In Ear 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana In Ear 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.42 | 7.4 dB  |
| Peaking | 154 Hz  |  0.36 | -4.1 dB |
| Peaking | 790 Hz  |  1.03 | 1.9 dB  |
| Peaking | 1809 Hz |  1.93 | -2.2 dB |
| Peaking | 3379 Hz |  2.58 | 6.7 dB  |
| Peaking | 3895 Hz | 11.07 | 0.8 dB  |
| Peaking | 6173 Hz |  4.2  | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana%20In%20Ear%203/Creative%20Aurvana%20In%20Ear%203.png)