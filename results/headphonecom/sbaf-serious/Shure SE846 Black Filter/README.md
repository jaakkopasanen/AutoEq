# Shure SE846 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -13.9; 28 -13.9; 31 -13.9; 34 -13.8; 37 -13.8; 41 -13.7; 45 -13.6; 49 -13.6; 54 -13.6; 60 -13.6; 66 -13.6; 72 -13.6; 79 -13.6; 87 -13.5; 96 -13.4; 106 -13.2; 116 -13.0; 128 -12.9; 141 -12.7; 155 -12.5; 170 -12.3; 187 -12.0; 206 -11.7; 227 -11.3; 249 -11.0; 274 -10.7; 302 -10.3; 332 -10.0; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.7; 535 -8.4; 588 -8.1; 647 -7.6; 712 -7.4; 783 -7.3; 861 -7.2; 947 -7.4; 1042 -7.6; 1146 -7.8; 1261 -8.0; 1387 -8.3; 1526 -8.6; 1678 -8.6; 1846 -8.2; 2031 -7.7; 2234 -6.9; 2457 -5.4; 2703 -3.2; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.47 | -5.8 dB |
| Peaking | 109 Hz  | 0.33 | -6.0 dB |
| Peaking | 1833 Hz | 1.41 | -4.1 dB |
| Peaking | 3907 Hz | 0.93 | 7.5 dB  |
| Peaking | 3029 Hz | 6.93 | 1.9 dB  |
| Peaking | 4047 Hz | 3.57 | -0.8 dB |
| Peaking | 6270 Hz | 2.19 | 4.9 dB  |
| Peaking | 7123 Hz | 0.67 | -1.5 dB |
| Peaking | 7578 Hz | 2.74 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Black%20Filter/Shure%20SE846%20Black%20Filter.png)