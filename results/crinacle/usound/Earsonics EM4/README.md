# Earsonics EM4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.9; 28 -9.1; 31 -9.2; 34 -9.3; 37 -9.5; 41 -9.6; 45 -9.7; 49 -9.7; 54 -9.8; 60 -9.9; 66 -10.1; 72 -10.3; 79 -10.6; 87 -10.9; 96 -11.1; 106 -11.3; 116 -11.5; 128 -11.6; 141 -11.7; 155 -11.9; 170 -11.8; 187 -11.8; 206 -11.7; 227 -11.5; 249 -11.4; 274 -11.2; 302 -10.9; 332 -10.7; 365 -10.4; 402 -10.1; 442 -9.7; 486 -9.3; 535 -9.0; 588 -8.5; 647 -8.1; 712 -7.6; 783 -7.2; 861 -6.9; 947 -6.8; 1042 -7.1; 1146 -7.9; 1261 -8.8; 1387 -9.5; 1526 -9.6; 1678 -9.4; 1846 -8.9; 2031 -8.1; 2234 -7.1; 2457 -6.0; 2703 -4.1; 2973 -1.3; 3270 -0.5; 3597 -1.4; 3957 -3.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.0; 16529 -16.1; 18182 -16.8; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.98 | -1.5 dB  |
| Peaking | 169 Hz   | 0.31 | -5.1 dB  |
| Peaking | 3218 Hz  | 4.83 | 5.7 dB   |
| Peaking | 5312 Hz  | 1.95 | 6.9 dB   |
| Peaking | 17709 Hz | 1.56 | -12.6 dB |
| Peaking | 878 Hz   | 1.6  | 1.7 dB   |
| Peaking | 1540 Hz  | 1.99 | -3.4 dB  |
| Peaking | 8049 Hz  | 6.01 | -1.4 dB  |
| Peaking | 14645 Hz | 1.9  | 3.3 dB   |
| Peaking | 16047 Hz | 3.42 | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20EM4/Earsonics%20EM4.png)