# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.6; 28 -3.7; 31 -3.8; 34 -3.9; 37 -4.1; 41 -4.3; 45 -4.4; 49 -4.5; 54 -4.7; 60 -5.0; 66 -5.3; 72 -5.6; 79 -6.0; 87 -6.4; 96 -6.9; 106 -7.3; 116 -7.7; 128 -8.1; 141 -8.4; 155 -8.7; 170 -8.9; 187 -9.0; 206 -9.1; 227 -9.2; 249 -9.2; 274 -9.2; 302 -9.1; 332 -9.0; 365 -8.9; 402 -8.8; 442 -8.7; 486 -8.6; 535 -8.5; 588 -8.3; 647 -8.2; 712 -8.1; 783 -7.9; 861 -7.9; 947 -8.2; 1042 -8.8; 1146 -10.0; 1261 -11.3; 1387 -12.3; 1526 -12.9; 1678 -12.8; 1846 -11.9; 2031 -9.9; 2234 -7.2; 2457 -4.5; 2703 -2.2; 2973 -0.8; 3270 -0.5; 3597 -0.7; 3957 -2.3; 4353 -4.2; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.25 | 3.1 dB  |
| Peaking | 198 Hz  | 0.46 | -3.3 dB |
| Peaking | 1645 Hz | 1.56 | -7.9 dB |
| Peaking | 3071 Hz | 1.76 | 7.6 dB  |
| Peaking | 5774 Hz | 3.17 | 6.0 dB  |
| Peaking | 944 Hz  | 3.33 | 0.9 dB  |
| Peaking | 1290 Hz | 2.04 | -0.7 dB |
| Peaking | 1571 Hz | 7.23 | 0.8 dB  |
| Peaking | 8254 Hz | 4.54 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE315/Shure%20SE315.png)