# VSonic GR07 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.2; 25 -3.6; 28 -4.0; 31 -4.3; 34 -4.5; 37 -4.6; 41 -4.8; 45 -5.1; 49 -5.3; 54 -5.6; 60 -5.9; 66 -6.3; 72 -6.7; 79 -7.1; 87 -7.5; 96 -8.0; 106 -8.4; 116 -8.8; 128 -9.1; 141 -9.5; 155 -9.8; 170 -9.9; 187 -10.1; 206 -10.2; 227 -10.3; 249 -10.3; 274 -10.3; 302 -10.2; 332 -10.0; 365 -9.7; 402 -9.6; 442 -9.4; 486 -9.1; 535 -8.8; 588 -8.4; 647 -7.9; 712 -7.4; 783 -6.9; 861 -6.4; 947 -6.2; 1042 -6.2; 1146 -6.4; 1261 -6.6; 1387 -6.5; 1526 -6.0; 1678 -5.5; 1846 -5.1; 2031 -4.6; 2234 -4.3; 2457 -4.0; 2703 -3.6; 2973 -2.4; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -2.9; 5793 -6.0; 6373 -5.9; 7010 -4.2; 7711 -6.3; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.4; 15026 -25.7; 16529 -27.1; 18182 -27.4; 20000 -29.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.19 | 3.6 dB   |
| Peaking | 257 Hz   | 0.37 | -4.4 dB  |
| Peaking | 956 Hz   | 0.55 | 1.5 dB   |
| Peaking | 3442 Hz  | 2.14 | 5.5 dB   |
| Peaking | 4631 Hz  | 4.22 | 4.4 dB   |
| Peaking | 343 Hz   | 4.84 | 0.1 dB   |
| Peaking | 11292 Hz | 0.66 | 9.5 dB   |
| Peaking | 12743 Hz | 2.57 | 10.5 dB  |
| Peaking | 14872 Hz | 0.83 | -17.6 dB |
| Peaking | 19892 Hz | 0.3  | -20.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB   |
| Peaking | 62 Hz    | 1.41 | 0.4 dB   |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -26.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/VSonic%20GR07%20Classic/VSonic%20GR07%20Classic.png)