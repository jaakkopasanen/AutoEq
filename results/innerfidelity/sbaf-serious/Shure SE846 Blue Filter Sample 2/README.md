# Shure SE846 Blue Filter Sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.1; 25 -10.2; 28 -10.2; 31 -10.1; 34 -10.1; 37 -10.1; 41 -10.0; 45 -10.0; 49 -10.0; 54 -10.0; 60 -10.0; 66 -10.0; 72 -10.0; 79 -10.1; 87 -10.1; 96 -10.2; 106 -10.1; 116 -9.9; 128 -9.8; 141 -9.7; 155 -9.5; 170 -9.3; 187 -9.0; 206 -8.8; 227 -8.5; 249 -8.3; 274 -8.0; 302 -7.8; 332 -7.6; 365 -7.3; 402 -7.2; 442 -6.9; 486 -6.9; 535 -6.8; 588 -6.3; 647 -6.2; 712 -6.1; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.1; 1387 -7.6; 1526 -7.8; 1678 -8.0; 1846 -7.8; 2031 -7.2; 2234 -6.4; 2457 -4.7; 2703 -2.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Blue Filter Sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.18 | -3.7 dB |
| Peaking | 702 Hz  | 0.78 | 1.1 dB  |
| Peaking | 1933 Hz | 1.14 | -3.8 dB |
| Peaking | 3215 Hz | 1.38 | 7.5 dB  |
| Peaking | 5621 Hz | 2.65 | 5.0 dB  |
| Peaking | 6593 Hz | 7.15 | 2.2 dB  |
| Peaking | 7865 Hz | 2.21 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Blue%20Filter%20Sample%202/Shure%20SE846%20Blue%20Filter%20Sample%202.png)