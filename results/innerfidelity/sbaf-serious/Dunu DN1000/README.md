# Dunu DN1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.8; 25 -9.8; 28 -9.8; 31 -9.8; 34 -9.8; 37 -9.8; 41 -9.8; 45 -9.8; 49 -9.8; 54 -9.9; 60 -10.0; 66 -10.1; 72 -10.2; 79 -10.3; 87 -10.4; 96 -10.6; 106 -10.5; 116 -10.4; 128 -10.3; 141 -10.3; 155 -10.1; 170 -9.9; 187 -9.6; 206 -9.4; 227 -9.0; 249 -8.7; 274 -8.3; 302 -8.0; 332 -7.6; 365 -7.3; 402 -7.0; 442 -6.5; 486 -6.4; 535 -6.1; 588 -5.6; 647 -5.4; 712 -5.3; 783 -5.1; 861 -5.2; 947 -5.5; 1042 -5.8; 1146 -5.9; 1261 -6.2; 1387 -6.5; 1526 -6.9; 1678 -6.9; 1846 -6.4; 2031 -5.9; 2234 -5.2; 2457 -4.0; 2703 -3.3; 2973 -1.9; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -5.2; 4788 -7.1; 5267 -4.4; 5793 -4.0; 6373 -3.8; 7010 -4.4; 7711 -6.9; 8482 -11.2; 9330 -13.9; 10263 -11.7; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 33 Hz    |  0.3  | -3.2 dB |
| Peaking | 141 Hz   |  0.9  | -2.7 dB |
| Peaking | 3388 Hz  |  2.44 | 6.6 dB  |
| Peaking | 6633 Hz  |  3.46 | 3.4 dB  |
| Peaking | 9307 Hz  |  3.52 | -8.6 dB |
| Peaking | 754 Hz   |  1.6  | 1.6 dB  |
| Peaking | 1619 Hz  |  4.08 | -1.1 dB |
| Peaking | 3953 Hz  | 11.18 | 2.3 dB  |
| Peaking | 4602 Hz  |  9.47 | -3.2 dB |
| Peaking | 11623 Hz |  6.7  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN1000/Dunu%20DN1000.png)