# RHA T20 Bass Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.4; 25 -11.6; 28 -11.8; 31 -11.9; 34 -12.1; 37 -12.2; 41 -12.2; 45 -12.2; 49 -12.2; 54 -12.3; 60 -12.3; 66 -12.3; 72 -12.3; 79 -12.3; 87 -12.3; 96 -12.4; 106 -12.2; 116 -12.0; 128 -11.8; 141 -11.5; 155 -11.3; 170 -11.0; 187 -10.6; 206 -10.2; 227 -9.7; 249 -9.2; 274 -8.8; 302 -8.3; 332 -7.8; 365 -7.4; 402 -6.9; 442 -6.4; 486 -6.1; 535 -5.8; 588 -5.2; 647 -5.0; 712 -4.9; 783 -4.8; 861 -5.1; 947 -5.5; 1042 -6.1; 1146 -6.8; 1261 -7.7; 1387 -9.1; 1526 -10.0; 1678 -9.0; 1846 -5.9; 2031 -8.0; 2234 -8.4; 2457 -8.5; 2703 -8.3; 2973 -7.0; 3270 -6.0; 3597 -6.5; 3957 -9.0; 4353 -13.0; 4788 -12.2; 5267 -6.6; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.9; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Bass Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.36 | -6.1 dB |
| Peaking | 148 Hz  | 0.89 | -3.2 dB |
| Peaking | 1532 Hz | 3.65 | -4.1 dB |
| Peaking | 4548 Hz | 4.14 | -8.8 dB |
| Peaking | 6120 Hz | 4.01 | 7.1 dB  |
| Peaking | 275 Hz  | 2.27 | -0.7 dB |
| Peaking | 715 Hz  | 1.49 | 1.8 dB  |
| Peaking | 1849 Hz | 7.51 | 3.0 dB  |
| Peaking | 2415 Hz | 1.38 | -2.6 dB |
| Peaking | 3381 Hz | 3.68 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Bass%20Filter/RHA%20T20%20Bass%20Filter.png)