# Xiaomi Piston 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.2; 28 -11.4; 31 -11.5; 34 -11.5; 37 -11.6; 41 -11.6; 45 -11.7; 49 -11.7; 54 -11.7; 60 -11.8; 66 -11.8; 72 -11.9; 79 -12.0; 87 -12.0; 96 -12.0; 106 -11.9; 116 -11.6; 128 -11.5; 141 -11.3; 155 -11.0; 170 -10.5; 187 -10.1; 206 -9.7; 227 -9.1; 249 -8.5; 274 -7.9; 302 -7.3; 332 -6.6; 365 -6.0; 402 -5.3; 442 -4.5; 486 -4.0; 535 -3.4; 588 -2.5; 647 -2.0; 712 -1.6; 783 -1.1; 861 -1.1; 947 -1.2; 1042 -1.4; 1146 -1.6; 1261 -1.8; 1387 -2.4; 1526 -2.9; 1678 -3.2; 1846 -3.3; 2031 -3.2; 2234 -3.2; 2457 -2.9; 2703 -2.9; 2973 -2.3; 3270 -1.2; 3597 -0.5; 3957 -1.3; 4353 -3.7; 4788 -5.2; 5267 -6.4; 5793 -7.5; 6373 -6.5; 7010 -4.3; 7711 -3.5; 8482 -4.6; 9330 -5.9; 10263 -4.7; 11289 -1.4; 12418 -1.3; 13660 -1.3; 15026 -1.3; 16529 -1.3; 18182 -1.3; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Piston 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.23 | -10.0 dB |
| Peaking | 180 Hz   | 0.66 | -4.6 dB  |
| Peaking | 1908 Hz  | 3    | -1.8 dB  |
| Peaking | 6115 Hz  | 1.53 | -5.5 dB  |
| Peaking | 22050 Hz | 2.28 | -2.1 dB  |
| Peaking | 821 Hz   | 2.43 | 1.5 dB   |
| Peaking | 3739 Hz  | 2.94 | 5.0 dB   |
| Peaking | 3913 Hz  | 1.11 | -2.6 dB  |
| Peaking | 7157 Hz  | 4.1  | 2.4 dB   |
| Peaking | 9485 Hz  | 5.04 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.7 dB  |
| Peaking | 125 Hz   | 1.41 | -8.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%202/Xiaomi%20Piston%202.png)