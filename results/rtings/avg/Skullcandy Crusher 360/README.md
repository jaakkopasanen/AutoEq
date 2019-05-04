# Skullcandy Crusher 360
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.3; 25 -5.5; 28 -5.8; 31 -6.0; 34 -6.3; 37 -6.5; 41 -6.6; 45 -6.5; 49 -6.4; 54 -6.2; 60 -6.3; 66 -6.4; 72 -6.6; 79 -6.9; 87 -7.2; 96 -7.7; 106 -8.0; 116 -8.2; 128 -8.3; 141 -8.2; 155 -7.9; 170 -7.6; 187 -7.0; 206 -6.4; 227 -5.8; 249 -5.1; 274 -4.4; 302 -3.7; 332 -3.1; 365 -2.5; 402 -2.0; 442 -1.6; 486 -1.4; 535 -1.1; 588 -0.9; 647 -0.7; 712 -0.5; 783 -0.6; 861 -0.6; 947 -0.9; 1042 -1.2; 1146 -1.1; 1261 -1.1; 1387 -1.4; 1526 -2.0; 1678 -2.6; 1846 -3.3; 2031 -4.2; 2234 -4.7; 2457 -5.0; 2703 -5.8; 2973 -7.6; 3270 -9.1; 3597 -8.3; 3957 -6.4; 4353 -5.5; 4788 -5.3; 5267 -4.8; 5793 -7.1; 6373 -8.8; 7010 -9.2; 7711 -10.3; 8482 -10.0; 9330 -8.9; 10263 -9.7; 11289 -12.0; 12418 -12.9; 13660 -10.7; 15026 -7.3; 16529 -6.3; 18182 -5.7; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher 360 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 562 Hz   | 1.7  | 3.2 dB  |
| Peaking | 1113 Hz  | 1.06 | 3.8 dB  |
| Peaking | 3263 Hz  | 4.24 | -4.4 dB |
| Peaking | 11376 Hz | 0.79 | -7.0 dB |
| Peaking | 22050 Hz | 1.99 | -5.8 dB |
| Peaking | 44 Hz    | 0.76 | -1.4 dB |
| Peaking | 131 Hz   | 1.37 | -3.6 dB |
| Peaking | 5088 Hz  | 3.44 | 2.7 dB  |
| Peaking | 8167 Hz  | 1.03 | -2.9 dB |
| Peaking | 9636 Hz  | 3.24 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | -4.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher%20360/Skullcandy%20Crusher%20360.png)