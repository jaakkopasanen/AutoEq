# VSonic GR07 Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.3; 25 -2.7; 28 -3.1; 31 -3.6; 34 -3.9; 37 -4.2; 41 -4.6; 45 -4.9; 49 -5.2; 54 -5.5; 60 -5.9; 66 -6.3; 72 -6.7; 79 -7.2; 87 -7.6; 96 -8.1; 106 -8.5; 116 -8.9; 128 -9.2; 141 -9.5; 155 -9.7; 170 -9.9; 187 -10.1; 206 -10.1; 227 -10.2; 249 -10.2; 274 -10.2; 302 -10.1; 332 -9.9; 365 -9.7; 402 -9.6; 442 -9.5; 486 -9.4; 535 -9.1; 588 -8.9; 647 -8.7; 712 -8.3; 783 -7.9; 861 -7.6; 947 -7.4; 1042 -7.5; 1146 -7.7; 1261 -7.8; 1387 -7.6; 1526 -7.0; 1678 -6.2; 1846 -4.7; 2031 -3.5; 2234 -3.3; 2457 -2.4; 2703 -1.5; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.6; 5793 -4.5; 6373 -5.6; 7010 -4.4; 7711 -6.4; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.1; 15026 -22.0; 16529 -23.0; 18182 -23.6; 20000 -24.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 313 Hz   | 0.26 | -4.3 dB  |
| Peaking | 1454 Hz  | 1.3  | -4.8 dB  |
| Peaking | 6753 Hz  | 0.17 | 10.7 dB  |
| Peaking | 17691 Hz | 0.31 | -23.9 dB |
| Peaking | 16 Hz    | 0.61 | 5.1 dB   |
| Peaking | 61 Hz    | 0.93 | 1.1 dB   |
| Peaking | 8083 Hz  | 1.76 | -3.6 dB  |
| Peaking | 12493 Hz | 1.41 | 8.1 dB   |
| Peaking | 14646 Hz | 2.3  | -8.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB   |
| Peaking | 62 Hz    | 1.41 | 0.2 dB   |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -21.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/VSonic%20GR07%20Mk2/VSonic%20GR07%20Mk2.png)