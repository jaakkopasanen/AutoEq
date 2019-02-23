# VSonic GR07
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.1; 25 -3.5; 28 -3.9; 31 -4.2; 34 -4.5; 37 -4.8; 41 -5.1; 45 -5.4; 49 -5.6; 54 -5.8; 60 -6.1; 66 -6.5; 72 -6.7; 79 -7.1; 87 -7.4; 96 -7.8; 106 -7.9; 116 -8.2; 128 -8.3; 141 -8.5; 155 -8.7; 170 -8.7; 187 -8.7; 206 -8.7; 227 -8.6; 249 -8.6; 274 -8.5; 302 -8.4; 332 -8.2; 365 -8.1; 402 -7.9; 442 -7.5; 486 -7.6; 535 -7.3; 588 -6.8; 647 -6.6; 712 -6.6; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -7.2; 1526 -7.5; 1678 -7.4; 1846 -7.1; 2031 -7.0; 2234 -6.4; 2457 -5.2; 2703 -4.1; 2973 -2.4; 3270 -0.8; 3597 -0.5; 3957 -1.0; 4353 -3.5; 4788 -5.4; 5267 -6.3; 5793 -7.1; 6373 -5.6; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.56 | 3.8 dB  |
| Peaking | 182 Hz  | 0.6  | -2.4 dB |
| Peaking | 1802 Hz | 1.78 | -1.3 dB |
| Peaking | 3503 Hz | 2.33 | 6.6 dB  |
| Peaking | 7358 Hz | 2.01 | -0.2 dB |
| Peaking | 794 Hz  | 3.39 | 0.6 dB  |
| Peaking | 4072 Hz | 8.25 | 1.2 dB  |
| Peaking | 5882 Hz | 2.41 | -2.0 dB |
| Peaking | 6747 Hz | 5.38 | 3.3 dB  |
| Peaking | 8956 Hz | 7.01 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07/VSonic%20GR07.png)