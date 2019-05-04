# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.6; 25 -1.8; 28 -2.2; 31 -2.5; 34 -2.8; 37 -3.1; 41 -3.4; 45 -3.7; 49 -3.9; 54 -4.3; 60 -4.6; 66 -5.1; 72 -5.5; 79 -5.9; 87 -6.3; 96 -6.8; 106 -7.2; 116 -7.6; 128 -7.9; 141 -8.2; 155 -8.4; 170 -8.6; 187 -8.6; 206 -8.7; 227 -8.7; 249 -8.9; 274 -9.1; 302 -9.2; 332 -9.2; 365 -9.1; 402 -9.0; 442 -8.8; 486 -8.7; 535 -8.4; 588 -8.2; 647 -7.9; 712 -7.7; 783 -7.6; 861 -7.9; 947 -8.6; 1042 -9.9; 1146 -11.5; 1261 -12.6; 1387 -13.3; 1526 -13.4; 1678 -13.0; 1846 -11.8; 2031 -9.8; 2234 -7.0; 2457 -3.9; 2703 -1.6; 2973 -0.5; 3270 -0.8; 3597 -2.3; 3957 -4.3; 4353 -5.0; 4788 -3.3; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.31 | 5.4 dB  |
| Peaking | 226 Hz  | 0.53 | -2.8 dB |
| Peaking | 1560 Hz | 1.5  | -8.1 dB |
| Peaking | 2930 Hz | 2.27 | 7.9 dB  |
| Peaking | 5784 Hz | 3.19 | 6.5 dB  |
| Peaking | 441 Hz  | 2.38 | -0.5 dB |
| Peaking | 797 Hz  | 2.33 | 0.8 dB  |
| Peaking | 1157 Hz | 1.59 | 0.6 dB  |
| Peaking | 1162 Hz | 3.96 | -1.7 dB |
| Peaking | 8241 Hz | 4.59 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE315/Shure%20SE315.png)