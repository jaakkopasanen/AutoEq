# Shure SE846 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -13.0; 25 -13.0; 28 -12.9; 31 -12.9; 34 -12.8; 37 -12.8; 41 -12.7; 45 -12.7; 49 -12.7; 54 -12.6; 60 -12.6; 66 -12.6; 72 -12.6; 79 -12.6; 87 -12.5; 96 -12.4; 106 -12.2; 116 -12.0; 128 -11.9; 141 -11.8; 155 -11.5; 170 -11.3; 187 -11.0; 206 -10.7; 227 -10.4; 249 -10.1; 274 -9.7; 302 -9.4; 332 -9.0; 365 -8.6; 402 -8.3; 442 -8.0; 486 -7.7; 535 -7.4; 588 -7.1; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.8; 1261 -7.0; 1387 -7.3; 1526 -7.6; 1678 -7.6; 1846 -7.2; 2031 -6.7; 2234 -5.9; 2457 -4.5; 2703 -2.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.32 | -5.9 dB |
| Peaking | 135 Hz  | 0.49 | -4.2 dB |
| Peaking | 1834 Hz | 1.82 | -3.2 dB |
| Peaking | 3893 Hz | 0.9  | 7.2 dB  |
| Peaking | 769 Hz  | 3.05 | 0.8 dB  |
| Peaking | 2945 Hz | 4.82 | 2.3 dB  |
| Peaking | 3526 Hz | 1.21 | -1.2 dB |
| Peaking | 6294 Hz | 2.41 | 5.0 dB  |
| Peaking | 7401 Hz | 1.53 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Black%20Filter/Shure%20SE846%20Black%20Filter.png)