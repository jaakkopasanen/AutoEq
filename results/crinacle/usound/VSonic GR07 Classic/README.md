# VSonic GR07 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.0; 25 -2.3; 28 -2.7; 31 -3.0; 34 -3.2; 37 -3.4; 41 -3.6; 45 -3.8; 49 -4.1; 54 -4.4; 60 -4.7; 66 -5.0; 72 -5.4; 79 -5.8; 87 -6.3; 96 -6.7; 106 -7.2; 116 -7.5; 128 -7.9; 141 -8.2; 155 -8.5; 170 -8.7; 187 -8.9; 206 -9.0; 227 -9.0; 249 -9.0; 274 -9.0; 302 -9.0; 332 -8.9; 365 -8.8; 402 -8.6; 442 -8.5; 486 -8.2; 535 -8.0; 588 -7.6; 647 -7.2; 712 -6.7; 783 -6.1; 861 -5.6; 947 -5.3; 1042 -5.3; 1146 -5.6; 1261 -6.1; 1387 -6.2; 1526 -5.9; 1678 -5.6; 1846 -5.2; 2031 -5.1; 2234 -5.3; 2457 -5.6; 2703 -5.6; 2973 -4.6; 3270 -3.0; 3597 -1.6; 3957 -0.7; 4353 -0.5; 4788 -1.4; 5267 -3.7; 5793 -7.0; 6373 -7.3; 7010 -6.0; 7711 -8.8; 8482 -9.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.9; 15026 -9.3; 16529 -8.2; 18182 -10.8; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.69 | 4.8 dB   |
| Peaking | 51 Hz    | 1.19 | 1.4 dB   |
| Peaking | 232 Hz   | 0.68 | -3.0 dB  |
| Peaking | 4424 Hz  | 1.39 | 10.1 dB  |
| Peaking | 5815 Hz  | 0.92 | -5.4 dB  |
| Peaking | 497 Hz   | 2.13 | -0.7 dB  |
| Peaking | 850 Hz   | 2.61 | 0.5 dB   |
| Peaking | 988 Hz   | 2.68 | 1.2 dB   |
| Peaking | 11149 Hz | 2.56 | 1.4 dB   |
| Peaking | 20127 Hz | 0.84 | -11.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/VSonic%20GR07%20Classic/VSonic%20GR07%20Classic.png)