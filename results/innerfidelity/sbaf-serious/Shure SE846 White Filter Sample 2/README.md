# Shure SE846 White Filter Sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.6; 25 -9.6; 28 -9.6; 31 -9.6; 34 -9.6; 37 -9.6; 41 -9.5; 45 -9.5; 49 -9.5; 54 -9.4; 60 -9.4; 66 -9.5; 72 -9.5; 79 -9.6; 87 -9.6; 96 -9.7; 106 -9.5; 116 -9.4; 128 -9.3; 141 -9.2; 155 -9.0; 170 -8.8; 187 -8.6; 206 -8.4; 227 -8.2; 249 -8.0; 274 -7.7; 302 -7.6; 332 -7.4; 365 -7.2; 402 -7.2; 442 -6.9; 486 -7.0; 535 -6.9; 588 -6.4; 647 -6.4; 712 -6.4; 783 -6.3; 861 -6.6; 947 -6.9; 1042 -7.3; 1146 -7.6; 1261 -8.0; 1387 -8.5; 1526 -9.1; 1678 -9.5; 1846 -9.6; 2031 -9.3; 2234 -8.5; 2457 -6.4; 2703 -3.8; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -1.9; 4353 -4.0; 4788 -3.5; 5267 -1.3; 5793 -0.5; 6373 -1.1; 7010 -4.6; 7711 -7.8; 8482 -8.0; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White Filter Sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 50 Hz   |  0.24 | -3.3 dB |
| Peaking | 1951 Hz |  1.54 | -4.6 dB |
| Peaking | 3220 Hz |  2.14 | 7.4 dB  |
| Peaking | 6030 Hz |  2.63 | 6.5 dB  |
| Peaking | 7914 Hz |  3.24 | -3.6 dB |
| Peaking | 21 Hz   |  0.64 | -0.4 dB |
| Peaking | 48 Hz   |  2.03 | 0.5 dB  |
| Peaking | 692 Hz  |  2.49 | 0.7 dB  |
| Peaking | 4441 Hz | 12.62 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20White%20Filter%20Sample%202/Shure%20SE846%20White%20Filter%20Sample%202.png)