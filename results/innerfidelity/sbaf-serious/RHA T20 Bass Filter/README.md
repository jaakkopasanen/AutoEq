# RHA T20 Bass Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.2; 25 -10.4; 28 -10.6; 31 -10.8; 34 -10.9; 37 -11.0; 41 -11.1; 45 -11.1; 49 -11.1; 54 -11.1; 60 -11.1; 66 -11.1; 72 -11.1; 79 -11.2; 87 -11.2; 96 -11.2; 106 -11.0; 116 -10.8; 128 -10.6; 141 -10.4; 155 -10.1; 170 -9.8; 187 -9.4; 206 -9.0; 227 -8.5; 249 -8.1; 274 -7.6; 302 -7.1; 332 -6.6; 365 -6.2; 402 -5.7; 442 -5.2; 486 -5.0; 535 -4.6; 588 -4.0; 647 -3.8; 712 -3.7; 783 -3.6; 861 -3.9; 947 -4.4; 1042 -5.0; 1146 -5.6; 1261 -6.5; 1387 -8.0; 1526 -8.8; 1678 -7.8; 1846 -4.7; 2031 -6.8; 2234 -7.2; 2457 -7.3; 2703 -7.1; 2973 -5.9; 3270 -4.9; 3597 -5.3; 3957 -7.8; 4353 -11.8; 4788 -11.0; 5267 -5.4; 5793 -0.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Bass Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.46 | -5.1 dB |
| Peaking | 132 Hz  | 1.09 | -3.1 dB |
| Peaking | 4522 Hz | 5.68 | -6.8 dB |
| Peaking | 4872 Hz | 4.08 | -1.7 dB |
| Peaking | 6050 Hz | 3.85 | 7.2 dB  |
| Peaking | 237 Hz  | 1.97 | -0.9 dB |
| Peaking | 706 Hz  | 1.11 | 2.6 dB  |
| Peaking | 1462 Hz | 4.5  | -3.6 dB |
| Peaking | 2500 Hz | 4.06 | -1.6 dB |
| Peaking | 3407 Hz | 6.13 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Bass%20Filter/RHA%20T20%20Bass%20Filter.png)