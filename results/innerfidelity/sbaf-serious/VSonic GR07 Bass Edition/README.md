# VSonic GR07 Bass Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.1; 25 -5.3; 28 -5.6; 31 -5.9; 34 -6.1; 37 -6.3; 41 -6.5; 45 -6.6; 49 -6.8; 54 -7.0; 60 -7.2; 66 -7.5; 72 -7.7; 79 -8.0; 87 -8.2; 96 -8.4; 106 -8.5; 116 -8.5; 128 -8.6; 141 -8.6; 155 -8.6; 170 -8.5; 187 -8.3; 206 -8.2; 227 -7.9; 249 -7.8; 274 -7.5; 302 -7.2; 332 -7.0; 365 -6.7; 402 -6.5; 442 -6.1; 486 -5.9; 535 -5.7; 588 -5.3; 647 -5.1; 712 -5.1; 783 -4.8; 861 -5.0; 947 -5.2; 1042 -5.4; 1146 -5.5; 1261 -5.7; 1387 -6.0; 1526 -6.4; 1678 -6.7; 1846 -6.4; 2031 -6.2; 2234 -5.7; 2457 -4.4; 2703 -3.9; 2973 -3.1; 3270 -1.5; 3597 -0.5; 3957 -1.1; 4353 -3.6; 4788 -5.7; 5267 -7.7; 5793 -8.8; 6373 -5.1; 7010 -3.4; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Bass Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Bass Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 106 Hz  | 0.85 | -2.5 dB |
| Peaking | 211 Hz  | 1.36 | -1.5 dB |
| Peaking | 3650 Hz | 2.63 | 6.0 dB  |
| Peaking | 5682 Hz | 3.26 | -4.6 dB |
| Peaking | 6743 Hz | 5.6  | 4.0 dB  |
| Peaking | 20 Hz   | 2.09 | 1.2 dB  |
| Peaking | 355 Hz  | 2.19 | -0.4 dB |
| Peaking | 783 Hz  | 1.23 | 1.1 dB  |
| Peaking | 1808 Hz | 1.73 | -1.4 dB |
| Peaking | 2567 Hz | 4.4  | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07%20Bass%20Edition/VSonic%20GR07%20Bass%20Edition.png)