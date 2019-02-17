# AKG K240DF
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.0; 72 -1.5; 79 -1.8; 87 -2.3; 96 -3.1; 106 -3.7; 116 -4.4; 128 -5.4; 141 -6.2; 155 -6.7; 170 -6.8; 187 -7.3; 206 -7.7; 227 -7.8; 249 -8.0; 274 -7.9; 302 -8.0; 332 -8.0; 365 -8.4; 402 -8.3; 442 -7.9; 486 -8.2; 535 -7.8; 588 -7.2; 647 -7.1; 712 -7.1; 783 -6.8; 861 -6.7; 947 -6.6; 1042 -6.4; 1146 -6.2; 1261 -6.2; 1387 -6.7; 1526 -7.6; 1678 -8.2; 1846 -8.3; 2031 -8.0; 2234 -7.5; 2457 -6.2; 2703 -5.6; 2973 -4.3; 3270 -5.8; 3597 -8.9; 3957 -8.6; 4353 -7.6; 4788 -6.1; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -9.8; 9330 -12.0; 10263 -10.6; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240DF GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240DF ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 39 Hz   |  0.65 | 7.0 dB  |
| Peaking | 1848 Hz |  2.3  | -2.9 dB |
| Peaking | 4264 Hz |  2.06 | -9.6 dB |
| Peaking | 5526 Hz |  0.91 | 10.7 dB |
| Peaking | 9087 Hz |  2.1  | -9.6 dB |
| Peaking | 41 Hz   |  2.67 | -1.5 dB |
| Peaking | 85 Hz   |  1.04 | 2.2 dB  |
| Peaking | 275 Hz  |  0.44 | -2.4 dB |
| Peaking | 1210 Hz |  0.32 | 0.6 dB  |
| Peaking | 3617 Hz | 12.7  | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240DF/AKG%20K240DF.png)