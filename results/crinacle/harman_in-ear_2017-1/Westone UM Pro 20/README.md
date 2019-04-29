# Westone UM Pro 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.2; 25 -10.4; 28 -10.5; 31 -10.7; 34 -10.8; 37 -10.9; 41 -11.1; 45 -11.2; 49 -11.3; 54 -11.5; 60 -11.7; 66 -12.0; 72 -12.3; 79 -12.6; 87 -13.0; 96 -13.4; 106 -13.7; 116 -14.0; 128 -14.2; 141 -14.4; 155 -14.7; 170 -14.7; 187 -14.7; 206 -14.6; 227 -14.5; 249 -14.3; 274 -14.1; 302 -13.7; 332 -13.3; 365 -12.7; 402 -12.3; 442 -11.8; 486 -11.3; 535 -10.7; 588 -10.1; 647 -9.4; 712 -8.7; 783 -7.9; 861 -7.3; 947 -6.9; 1042 -6.8; 1146 -6.9; 1261 -7.1; 1387 -6.8; 1526 -6.0; 1678 -5.0; 1846 -3.9; 2031 -2.6; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -16.5; 16529 -9.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.37 | -3.4 dB  |
| Peaking | 116 Hz   | 0.71 | -2.2 dB  |
| Peaking | 248 Hz   | 0.47 | -6.7 dB  |
| Peaking | 3557 Hz  | 0.74 | 7.1 dB   |
| Peaking | 15213 Hz | 3.63 | -11.5 dB |
| Peaking | 1424 Hz  | 4.01 | -1.4 dB  |
| Peaking | 2311 Hz  | 4.33 | 1.8 dB   |
| Peaking | 3629 Hz  | 2.44 | -1.2 dB  |
| Peaking | 6111 Hz  | 2.55 | 3.0 dB   |
| Peaking | 8104 Hz  | 3.02 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20UM%20Pro%2020/Westone%20UM%20Pro%2020.png)