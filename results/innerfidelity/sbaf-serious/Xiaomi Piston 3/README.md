# Xiaomi Piston 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.1; 25 -6.5; 28 -7.1; 31 -7.6; 34 -8.0; 37 -8.4; 41 -8.7; 45 -9.0; 49 -9.3; 54 -9.7; 60 -10.0; 66 -10.4; 72 -10.6; 79 -10.9; 87 -11.3; 96 -11.6; 106 -11.6; 116 -11.6; 128 -11.7; 141 -11.6; 155 -11.5; 170 -11.3; 187 -10.9; 206 -10.6; 227 -10.1; 249 -9.7; 274 -9.1; 302 -8.5; 332 -7.9; 365 -7.3; 402 -6.6; 442 -5.8; 486 -5.3; 535 -4.6; 588 -3.8; 647 -3.2; 712 -2.8; 783 -2.3; 861 -2.2; 947 -2.3; 1042 -2.9; 1146 -3.7; 1261 -4.6; 1387 -5.7; 1526 -6.5; 1678 -7.1; 1846 -7.4; 2031 -7.5; 2234 -7.7; 2457 -7.3; 2703 -6.9; 2973 -5.6; 3270 -4.1; 3597 -3.6; 3957 -5.2; 4353 -8.5; 4788 -9.1; 5267 -5.0; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Piston 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 68 Hz   | 0.7  | -2.2 dB |
| Peaking | 158 Hz  | 0.53 | -5.0 dB |
| Peaking | 830 Hz  | 0.87 | 4.8 dB  |
| Peaking | 1806 Hz | 1.52 | -3.0 dB |
| Peaking | 6192 Hz | 5.75 | 6.7 dB  |
| Peaking | 2614 Hz | 3.31 | -1.2 dB |
| Peaking | 3581 Hz | 2.77 | 3.8 dB  |
| Peaking | 4585 Hz | 3.77 | -5.4 dB |
| Peaking | 5569 Hz | 6.88 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%203/Xiaomi%20Piston%203.png)