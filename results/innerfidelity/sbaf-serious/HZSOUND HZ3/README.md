# HZSOUND HZ3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.3; 25 -2.6; 28 -2.9; 31 -3.2; 34 -3.4; 37 -3.6; 41 -3.8; 45 -4.0; 49 -4.2; 54 -4.5; 60 -4.8; 66 -5.2; 72 -5.5; 79 -5.8; 87 -6.3; 96 -6.7; 106 -6.8; 116 -7.0; 128 -7.3; 141 -7.5; 155 -7.6; 170 -7.7; 187 -7.6; 206 -7.7; 227 -7.5; 249 -7.4; 274 -7.2; 302 -7.0; 332 -6.7; 365 -6.4; 402 -6.1; 442 -5.6; 486 -5.4; 535 -5.1; 588 -4.4; 647 -4.1; 712 -3.9; 783 -3.5; 861 -3.6; 947 -2.3; 1042 -3.1; 1146 -3.4; 1261 -2.9; 1387 -2.6; 1526 -3.4; 1678 -3.6; 1846 -3.5; 2031 -3.2; 2234 -3.0; 2457 -2.6; 2703 -2.1; 2973 -1.5; 3270 -0.5; 3597 -0.9; 3957 -1.4; 4353 -3.1; 4788 -7.6; 5267 -11.1; 5793 -8.1; 6373 -3.0; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HZSOUND HZ3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 19 Hz   |  0.68 | 2.7 dB   |
| Peaking | 171 Hz  |  0.73 | -3.3 dB  |
| Peaking | 3879 Hz |  0.88 | 5.5 dB   |
| Peaking | 5275 Hz |  3.02 | -11.1 dB |
| Peaking | 6523 Hz |  6.19 | 4.4 dB   |
| Peaking | 885 Hz  |  1.01 | 3.7 dB   |
| Peaking | 946 Hz  |  0.52 | -2.2 dB  |
| Peaking | 1356 Hz |  6.43 | 1.5 dB   |
| Peaking | 4159 Hz | 14.7  | 2.3 dB   |
| Peaking | 9477 Hz |  1.83 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ3/HZSOUND%20HZ3.png)