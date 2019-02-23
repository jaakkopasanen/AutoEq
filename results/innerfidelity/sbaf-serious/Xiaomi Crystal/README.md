# Xiaomi Crystal
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.2; 28 -8.5; 31 -8.7; 34 -8.9; 37 -9.0; 41 -9.1; 45 -9.2; 49 -9.4; 54 -9.6; 60 -9.7; 66 -9.9; 72 -10.0; 79 -10.2; 87 -10.3; 96 -10.5; 106 -10.4; 116 -10.3; 128 -10.3; 141 -10.1; 155 -9.9; 170 -9.6; 187 -9.3; 206 -8.8; 227 -8.3; 249 -7.8; 274 -7.3; 302 -6.7; 332 -6.1; 365 -5.4; 402 -4.8; 442 -4.0; 486 -3.5; 535 -2.9; 588 -2.0; 647 -1.4; 712 -1.1; 783 -0.5; 861 -0.5; 947 -0.6; 1042 -0.6; 1146 -0.8; 1261 -0.9; 1387 -1.1; 1526 -1.3; 1678 -1.6; 1846 -2.8; 2031 -3.3; 2234 -3.3; 2457 -2.8; 2703 -2.7; 2973 -2.1; 3270 -1.5; 3597 -1.0; 3957 -1.7; 4353 -4.0; 4788 -5.4; 5267 -6.4; 5793 -8.1; 6373 -7.4; 7010 -5.0; 7711 -4.3; 8482 -5.0; 9330 -6.5; 10263 -5.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Crystal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.35 | -3.2 dB |
| Peaking | 143 Hz  | 0.5  | -4.6 dB |
| Peaking | 883 Hz  | 0.71 | 4.8 dB  |
| Peaking | 3488 Hz | 4.79 | 3.6 dB  |
| Peaking | 265 Hz  | 2.4  | -0.1 dB |
| Peaking | 3959 Hz | 2.1  | 1.0 dB  |
| Peaking | 6030 Hz | 2.54 | -5.1 dB |
| Peaking | 7161 Hz | 2.31 | 2.2 dB  |
| Peaking | 9396 Hz | 4.88 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Crystal/Xiaomi%20Crystal.png)