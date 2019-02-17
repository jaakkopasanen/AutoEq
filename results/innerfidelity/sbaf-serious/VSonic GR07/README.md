# VSonic GR07
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.0; 25 -3.3; 28 -3.8; 31 -4.1; 34 -4.4; 37 -4.7; 41 -5.0; 45 -5.2; 49 -5.5; 54 -5.7; 60 -6.0; 66 -6.4; 72 -6.6; 79 -7.0; 87 -7.3; 96 -7.7; 106 -7.8; 116 -8.0; 128 -8.2; 141 -8.4; 155 -8.6; 170 -8.6; 187 -8.6; 206 -8.6; 227 -8.5; 249 -8.5; 274 -8.4; 302 -8.3; 332 -8.1; 365 -8.0; 402 -7.7; 442 -7.4; 486 -7.4; 535 -7.2; 588 -6.7; 647 -6.5; 712 -6.5; 783 -6.2; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.8; 1387 -7.1; 1526 -7.4; 1678 -7.3; 1846 -7.0; 2031 -6.9; 2234 -6.2; 2457 -5.1; 2703 -4.0; 2973 -2.3; 3270 -0.8; 3597 -0.5; 3957 -0.9; 4353 -3.4; 4788 -5.3; 5267 -6.2; 5793 -7.0; 6373 -5.5; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.45 | 4.5 dB  |
| Peaking | 179 Hz  | 0.61 | -2.4 dB |
| Peaking | 1779 Hz | 2.29 | -1.3 dB |
| Peaking | 3498 Hz | 2.36 | 6.7 dB  |
| Peaking | 9616 Hz | 2.28 | -0.2 dB |
| Peaking | 790 Hz  | 3.29 | 0.7 dB  |
| Peaking | 4027 Hz | 8.55 | 1.3 dB  |
| Peaking | 6010 Hz | 2.11 | -2.0 dB |
| Peaking | 6830 Hz | 5.44 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07/VSonic%20GR07.png)