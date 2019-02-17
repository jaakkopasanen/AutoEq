# Xiaomi Piston 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.4; 25 -8.8; 28 -9.4; 31 -9.9; 34 -10.3; 37 -10.7; 41 -11.0; 45 -11.4; 49 -11.6; 54 -12.0; 60 -12.4; 66 -12.7; 72 -12.9; 79 -13.3; 87 -13.6; 96 -13.9; 106 -13.9; 116 -13.9; 128 -14.0; 141 -13.9; 155 -13.8; 170 -13.6; 187 -13.3; 206 -12.9; 227 -12.4; 249 -12.0; 274 -11.4; 302 -10.8; 332 -10.3; 365 -9.6; 402 -8.9; 442 -8.2; 486 -7.6; 535 -6.9; 588 -6.1; 647 -5.5; 712 -5.1; 783 -4.6; 861 -4.5; 947 -4.6; 1042 -5.2; 1146 -6.0; 1261 -6.9; 1387 -8.0; 1526 -8.8; 1678 -9.4; 1846 -9.7; 2031 -9.8; 2234 -10.0; 2457 -9.6; 2703 -9.2; 2973 -7.9; 3270 -6.4; 3597 -5.9; 3957 -7.6; 4353 -10.8; 4788 -11.4; 5267 -7.3; 5793 -3.0; 6373 -0.5; 7010 -2.5; 7711 -4.7; 8482 -5.0; 9330 -5.3; 10263 -6.2; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Piston 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 76 Hz   | 0.41 | -7.5 dB |
| Peaking | 207 Hz  | 0.84 | -4.3 dB |
| Peaking | 2085 Hz | 1.64 | -5.3 dB |
| Peaking | 4638 Hz | 4.68 | -7.3 dB |
| Peaking | 6321 Hz | 4.56 | 5.8 dB  |
| Peaking | 851 Hz  | 2.35 | 2.0 dB  |
| Peaking | 1471 Hz | 4.59 | -1.4 dB |
| Peaking | 2748 Hz | 7.02 | -1.2 dB |
| Peaking | 3475 Hz | 6.9  | 1.4 dB  |
| Peaking | 9975 Hz | 8.17 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%203/Xiaomi%20Piston%203.png)