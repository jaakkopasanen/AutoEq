# Shure SE846 White Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.3; 25 -10.4; 28 -10.4; 31 -10.4; 34 -10.3; 37 -10.3; 41 -10.3; 45 -10.2; 49 -10.2; 54 -10.3; 60 -10.3; 66 -10.3; 72 -10.3; 79 -10.3; 87 -10.4; 96 -10.3; 106 -10.2; 116 -10.0; 128 -9.9; 141 -9.8; 155 -9.7; 170 -9.5; 187 -9.3; 206 -9.0; 227 -8.8; 249 -8.5; 274 -8.4; 302 -8.2; 332 -8.0; 365 -7.7; 402 -7.5; 442 -7.3; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.6; 712 -6.4; 783 -6.3; 861 -6.4; 947 -6.7; 1042 -7.1; 1146 -7.4; 1261 -7.7; 1387 -8.3; 1526 -9.0; 1678 -9.4; 1846 -9.5; 2031 -9.4; 2234 -8.6; 2457 -6.8; 2703 -4.0; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -3.0; 4788 -2.5; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -7.8; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.22 | -4.1 dB |
| Peaking | 2006 Hz | 1.6  | -4.8 dB |
| Peaking | 3257 Hz | 1.92 | 7.1 dB  |
| Peaking | 6021 Hz | 2.09 | 6.5 dB  |
| Peaking | 8143 Hz | 2.35 | -3.5 dB |
| Peaking | 767 Hz  | 2.26 | 0.9 dB  |
| Peaking | 1440 Hz | 4.19 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20White%20Filter/Shure%20SE846%20White%20Filter.png)