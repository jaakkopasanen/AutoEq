# Blue Lola
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.2; 25 -8.4; 28 -8.5; 31 -8.7; 34 -8.7; 37 -8.9; 41 -9.0; 45 -9.1; 49 -9.2; 54 -9.3; 60 -9.5; 66 -9.6; 72 -9.7; 79 -9.9; 87 -10.2; 96 -10.6; 106 -10.4; 116 -10.2; 128 -10.4; 141 -10.8; 155 -11.2; 170 -10.1; 187 -10.4; 206 -10.1; 227 -9.4; 249 -8.6; 274 -7.7; 302 -7.1; 332 -6.9; 365 -6.9; 402 -7.2; 442 -6.8; 486 -6.1; 535 -4.9; 588 -5.7; 647 -6.2; 712 -6.7; 783 -6.7; 861 -7.0; 947 -7.6; 1042 -7.8; 1146 -8.0; 1261 -8.2; 1387 -8.3; 1526 -8.7; 1678 -8.9; 1846 -8.3; 2031 -7.5; 2234 -7.0; 2457 -5.9; 2703 -5.4; 2973 -4.8; 3270 -4.3; 3597 -1.9; 3957 -1.8; 4353 -5.5; 4788 -5.9; 5267 -2.3; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue Lola GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue Lola ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 60 Hz   |  0.47 | -3.2 dB |
| Peaking | 162 Hz  |  1.3  | -3.3 dB |
| Peaking | 1523 Hz |  1.71 | -2.7 dB |
| Peaking | 3655 Hz |  4.14 | 4.6 dB  |
| Peaking | 6031 Hz |  4.13 | 6.5 dB  |
| Peaking | 216 Hz  |  7.94 | -0.8 dB |
| Peaking | 536 Hz  |  5.55 | 1.9 dB  |
| Peaking | 1001 Hz |  4.99 | -0.7 dB |
| Peaking | 2683 Hz |  5.44 | 0.8 dB  |
| Peaking | 4603 Hz | 14.51 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20Lola/Blue%20Lola.png)