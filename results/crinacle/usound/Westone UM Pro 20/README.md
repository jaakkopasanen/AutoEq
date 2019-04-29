# Westone UM Pro 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.1; 25 -9.2; 28 -9.4; 31 -9.5; 34 -9.7; 37 -9.8; 41 -9.9; 45 -10.0; 49 -10.2; 54 -10.4; 60 -10.6; 66 -10.9; 72 -11.2; 79 -11.4; 87 -11.8; 96 -12.2; 106 -12.6; 116 -12.8; 128 -13.1; 141 -13.3; 155 -13.5; 170 -13.5; 187 -13.6; 206 -13.5; 227 -13.3; 249 -13.1; 274 -12.9; 302 -12.6; 332 -12.3; 365 -11.9; 402 -11.5; 442 -11.0; 486 -10.5; 535 -10.0; 588 -9.4; 647 -8.7; 712 -8.0; 783 -7.2; 861 -6.6; 947 -6.1; 1042 -6.0; 1146 -6.2; 1261 -6.6; 1387 -6.6; 1526 -6.1; 1678 -5.1; 1846 -4.1; 2031 -3.1; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.0; 8482 -9.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.28 | -2.7 dB |
| Peaking | 132 Hz  | 0.79 | -2.6 dB |
| Peaking | 288 Hz  | 0.59 | -4.9 dB |
| Peaking | 4055 Hz | 0.62 | 7.0 dB  |
| Peaking | 8258 Hz | 4.05 | -6.7 dB |
| Peaking | 947 Hz  | 2.14 | 1.6 dB  |
| Peaking | 1400 Hz | 2.91 | -1.2 dB |
| Peaking | 2452 Hz | 2.9  | 2.5 dB  |
| Peaking | 4236 Hz | 0.2  | -1.0 dB |
| Peaking | 6234 Hz | 2.98 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20UM%20Pro%2020/Westone%20UM%20Pro%2020.png)