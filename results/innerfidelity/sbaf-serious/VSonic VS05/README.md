# VSonic VS05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.1; 25 -2.6; 28 -3.1; 31 -3.5; 34 -3.8; 37 -4.1; 41 -4.5; 45 -4.8; 49 -5.1; 54 -5.5; 60 -5.9; 66 -6.3; 72 -6.7; 79 -7.1; 87 -7.5; 96 -8.0; 106 -8.3; 116 -8.5; 128 -8.8; 141 -9.0; 155 -9.2; 170 -9.3; 187 -9.3; 206 -9.4; 227 -9.1; 249 -9.1; 274 -8.8; 302 -8.7; 332 -8.4; 365 -8.1; 402 -7.7; 442 -7.2; 486 -7.0; 535 -6.5; 588 -5.9; 647 -5.5; 712 -5.2; 783 -4.7; 861 -4.6; 947 -4.6; 1042 -4.6; 1146 -4.6; 1261 -4.6; 1387 -4.7; 1526 -4.5; 1678 -4.3; 1846 -3.8; 2031 -3.3; 2234 -2.9; 2457 -2.1; 2703 -1.8; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -3.8; 4788 -5.3; 5267 -6.3; 5793 -8.2; 6373 -8.9; 7010 -7.7; 7711 -8.0; 8482 -9.8; 9330 -9.7; 10263 -6.0; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VS05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VS05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.81 | 3.7 dB  |
| Peaking | 183 Hz   | 0.51 | -4.9 dB |
| Peaking | 3394 Hz  | 1.34 | 5.0 dB  |
| Peaking | 5988 Hz  | 1.9  | -4.9 dB |
| Peaking | 8892 Hz  | 4.19 | -5.3 dB |
| Peaking | 397 Hz   | 2.22 | -0.4 dB |
| Peaking | 803 Hz   | 2.65 | 0.9 dB  |
| Peaking | 11128 Hz | 6.1  | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VS05/VSonic%20VS05.png)