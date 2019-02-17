# Shure SE846 White Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.0; 25 -10.0; 28 -10.0; 31 -10.0; 34 -10.0; 37 -9.9; 41 -9.9; 45 -9.9; 49 -9.9; 54 -9.9; 60 -9.9; 66 -10.0; 72 -10.0; 79 -10.0; 87 -10.0; 96 -9.9; 106 -9.8; 116 -9.7; 128 -9.6; 141 -9.5; 155 -9.3; 170 -9.2; 187 -8.9; 206 -8.7; 227 -8.4; 249 -8.2; 274 -8.0; 302 -7.9; 332 -7.6; 365 -7.3; 402 -7.1; 442 -6.9; 486 -6.8; 535 -6.6; 588 -6.4; 647 -6.2; 712 -6.0; 783 -5.9; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -8.0; 1526 -8.6; 1678 -9.1; 1846 -9.2; 2031 -9.0; 2234 -8.2; 2457 -6.5; 2703 -3.7; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -2.6; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.6; 8482 -7.4; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.25 | -3.7 dB |
| Peaking | 2031 Hz | 1.73 | -4.8 dB |
| Peaking | 3238 Hz | 1.72 | 7.0 dB  |
| Peaking | 6019 Hz | 2.01 | 6.3 dB  |
| Peaking | 8054 Hz | 2.21 | -3.2 dB |
| Peaking | 28 Hz   | 0.17 | -1.0 dB |
| Peaking | 47 Hz   | 0.63 | 1.3 dB  |
| Peaking | 746 Hz  | 1.45 | 1.0 dB  |
| Peaking | 1451 Hz | 3.58 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20White%20Filter/Shure%20SE846%20White%20Filter.png)