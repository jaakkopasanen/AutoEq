# Xiaomi Piston 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.2; 28 -11.4; 31 -11.5; 34 -11.5; 37 -11.6; 41 -11.6; 45 -11.7; 49 -11.7; 54 -11.7; 60 -11.8; 66 -11.8; 72 -11.9; 79 -12.0; 87 -12.0; 96 -12.0; 106 -11.9; 116 -11.6; 128 -11.5; 141 -11.3; 155 -11.0; 170 -10.5; 187 -10.1; 206 -9.7; 227 -9.1; 249 -8.5; 274 -7.9; 302 -7.3; 332 -6.6; 365 -6.0; 402 -5.3; 442 -4.5; 486 -4.0; 535 -3.4; 588 -2.5; 647 -2.0; 712 -1.6; 783 -1.1; 861 -1.1; 947 -1.2; 1042 -1.4; 1146 -1.6; 1261 -1.8; 1387 -2.4; 1526 -2.9; 1678 -3.2; 1846 -3.3; 2031 -3.2; 2234 -3.2; 2457 -2.9; 2703 -2.9; 2973 -2.3; 3270 -1.2; 3597 -0.5; 3957 -1.3; 4353 -3.7; 4788 -5.2; 5267 -6.4; 5793 -7.5; 6373 -6.5; 7010 -4.3; 7711 -4.7; 8482 -5.0; 9330 -5.9; 10263 -5.1; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Piston 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.46 | -4.7 dB |
| Peaking | 118 Hz  | 0.4  | -6.1 dB |
| Peaking | 814 Hz  | 0.69 | 4.6 dB  |
| Peaking | 3568 Hz | 2.6  | 4.4 dB  |
| Peaking | 5615 Hz | 3.59 | -3.2 dB |
| Peaking | 1652 Hz | 6.02 | -0.3 dB |
| Peaking | 2420 Hz | 5.02 | 0.4 dB  |
| Peaking | 6287 Hz | 7.58 | -0.9 dB |
| Peaking | 7129 Hz | 5.8  | 1.4 dB  |
| Peaking | 9486 Hz | 7.27 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%202/Xiaomi%20Piston%202.png)