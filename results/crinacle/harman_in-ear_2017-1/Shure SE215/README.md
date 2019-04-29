# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.3; 25 -9.4; 28 -9.5; 31 -9.5; 34 -9.6; 37 -9.6; 41 -9.7; 45 -9.8; 49 -9.9; 54 -10.0; 60 -10.2; 66 -10.4; 72 -10.6; 79 -10.8; 87 -11.1; 96 -11.4; 106 -11.6; 116 -11.7; 128 -11.8; 141 -11.9; 155 -11.9; 170 -11.8; 187 -11.6; 206 -11.4; 227 -11.0; 249 -10.7; 274 -10.3; 302 -9.7; 332 -9.2; 365 -8.5; 402 -8.0; 442 -7.5; 486 -7.0; 535 -6.4; 588 -5.9; 647 -5.3; 712 -4.8; 783 -4.2; 861 -3.9; 947 -3.9; 1042 -4.3; 1146 -5.1; 1261 -5.8; 1387 -6.1; 1526 -6.2; 1678 -6.0; 1846 -6.0; 2031 -6.2; 2234 -6.4; 2457 -5.9; 2703 -4.2; 2973 -2.1; 3270 -0.8; 3597 -0.5; 3957 -1.4; 4353 -3.8; 4788 -7.8; 5267 -7.7; 5793 -2.6; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -10.7; 15026 -13.9; 16529 -17.3; 18182 -19.7; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.36 | -3.6 dB  |
| Peaking | 176 Hz   | 0.93 | -4.2 dB  |
| Peaking | 3445 Hz  | 3.1  | 6.6 dB   |
| Peaking | 6397 Hz  | 5.76 | 6.3 dB   |
| Peaking | 18051 Hz | 0.96 | -14.8 dB |
| Peaking | 309 Hz   | 2.66 | -1.0 dB  |
| Peaking | 849 Hz   | 1.98 | 2.9 dB   |
| Peaking | 5046 Hz  | 9.86 | -4.4 dB  |
| Peaking | 12376 Hz | 1.63 | 4.1 dB   |
| Peaking | 14615 Hz | 1.66 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -12.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE215/Shure%20SE215.png)