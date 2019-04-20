# Koss ESP950
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.8; 31 -0.9; 34 -1.0; 37 -1.1; 41 -1.4; 45 -1.8; 49 -1.9; 54 -1.8; 60 -2.2; 66 -2.9; 72 -4.2; 79 -6.2; 87 -6.7; 96 -6.7; 106 -6.8; 116 -6.6; 128 -6.6; 141 -7.0; 155 -7.5; 170 -7.7; 187 -7.8; 206 -7.8; 227 -7.9; 249 -7.9; 274 -7.8; 302 -7.6; 332 -7.4; 365 -7.2; 402 -7.2; 442 -7.4; 486 -7.7; 535 -7.8; 588 -7.9; 647 -7.8; 712 -7.8; 783 -8.6; 861 -9.6; 947 -10.0; 1042 -10.2; 1146 -10.5; 1261 -10.9; 1387 -10.3; 1526 -8.8; 1678 -7.1; 1846 -3.8; 2031 -0.7; 2234 -0.9; 2457 -4.2; 2703 -6.4; 2973 -7.4; 3270 -6.8; 3597 -5.0; 3957 -4.1; 4353 -4.2; 4788 -2.9; 5267 -4.0; 5793 -6.3; 6373 -5.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.5; 13660 -8.0; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.15 | 6.3 dB  |
| Peaking | 54 Hz    | 2.79 | 3.7 dB  |
| Peaking | 2105 Hz  | 2.42 | 13.7 dB |
| Peaking | 2122 Hz  | 0.51 | -8.4 dB |
| Peaking | 4400 Hz  | 1.24 | 6.8 dB  |
| Peaking | 90 Hz    | 3    | -1.8 dB |
| Peaking | 145 Hz   | 0.41 | 1.5 dB  |
| Peaking | 191 Hz   | 0.97 | -2.7 dB |
| Peaking | 693 Hz   | 5.27 | 1.1 dB  |
| Peaking | 12790 Hz | 5.97 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Koss%20ESP950/Koss%20ESP950.png)