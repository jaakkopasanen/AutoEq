# Shure SE846 Blue Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -10.9; 25 -10.9; 28 -10.9; 31 -10.9; 34 -10.9; 37 -10.9; 41 -10.9; 45 -10.8; 49 -10.8; 54 -10.8; 60 -10.9; 66 -10.9; 72 -10.9; 79 -10.9; 87 -10.9; 96 -10.8; 106 -10.7; 116 -10.6; 128 -10.5; 141 -10.4; 155 -10.2; 170 -10.0; 187 -9.8; 206 -9.6; 227 -9.3; 249 -9.1; 274 -8.9; 302 -8.5; 332 -8.2; 365 -8.0; 402 -7.7; 442 -7.6; 486 -7.4; 535 -7.1; 588 -6.9; 647 -6.4; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.1; 1387 -7.5; 1526 -8.0; 1678 -8.2; 1846 -7.9; 2031 -7.5; 2234 -6.6; 2457 -4.9; 2703 -2.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Blue Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.2  | -4.6 dB |
| Peaking | 1948 Hz | 1.82 | -3.2 dB |
| Peaking | 3111 Hz | 1.81 | 6.2 dB  |
| Peaking | 4720 Hz | 2.36 | 4.3 dB  |
| Peaking | 6158 Hz | 4.68 | 4.2 dB  |
| Peaking | 761 Hz  | 2.4  | 0.9 dB  |
| Peaking | 1463 Hz | 5.06 | -0.5 dB |
| Peaking | 6761 Hz | 2.16 | 1.2 dB  |
| Peaking | 7757 Hz | 2.21 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Blue%20Filter/Shure%20SE846%20Blue%20Filter.png)