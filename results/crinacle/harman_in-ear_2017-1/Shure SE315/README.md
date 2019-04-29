# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.7; 25 -4.8; 28 -4.8; 31 -4.9; 34 -5.1; 37 -5.2; 41 -5.4; 45 -5.5; 49 -5.7; 54 -5.8; 60 -6.1; 66 -6.4; 72 -6.8; 79 -7.1; 87 -7.5; 96 -8.1; 106 -8.5; 116 -8.8; 128 -9.2; 141 -9.5; 155 -9.9; 170 -10.0; 187 -10.2; 206 -10.3; 227 -10.3; 249 -10.3; 274 -10.3; 302 -10.2; 332 -10.0; 365 -9.7; 402 -9.6; 442 -9.5; 486 -9.3; 535 -9.2; 588 -9.0; 647 -8.9; 712 -8.7; 783 -8.6; 861 -8.6; 947 -8.9; 1042 -9.6; 1146 -10.7; 1261 -11.8; 1387 -12.5; 1526 -12.8; 1678 -12.7; 1846 -11.7; 2031 -9.3; 2234 -6.1; 2457 -2.7; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -3.0; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.4; 16529 -9.4; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 243 Hz   | 0.63 | -4.0 dB  |
| Peaking | 1699 Hz  | 1.21 | -10.0 dB |
| Peaking | 2842 Hz  | 1.2  | 10.0 dB  |
| Peaking | 5740 Hz  | 3.09 | 5.1 dB   |
| Peaking | 15685 Hz | 3.81 | -5.9 dB  |
| Peaking | 25 Hz    | 1.23 | 1.9 dB   |
| Peaking | 50 Hz    | 2.38 | 0.9 dB   |
| Peaking | 513 Hz   | 4.14 | -0.4 dB  |
| Peaking | 6633 Hz  | 8.44 | 1.9 dB   |
| Peaking | 7869 Hz  | 2.83 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE315/Shure%20SE315.png)