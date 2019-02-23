# Koss ESP950
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.9; 31 -1.0; 34 -1.0; 37 -0.9; 41 -1.3; 45 -1.9; 49 -2.0; 54 -1.7; 60 -2.2; 66 -2.9; 72 -4.0; 79 -6.3; 87 -6.7; 96 -6.7; 106 -6.8; 116 -6.6; 128 -6.6; 141 -7.0; 155 -7.5; 170 -7.7; 187 -7.8; 206 -7.8; 227 -7.9; 249 -7.9; 274 -7.8; 302 -7.6; 332 -7.4; 365 -7.2; 402 -7.1; 442 -7.4; 486 -7.7; 535 -7.8; 588 -7.9; 647 -7.8; 712 -7.8; 783 -8.6; 861 -9.6; 947 -10.0; 1042 -10.2; 1146 -10.5; 1261 -10.9; 1387 -10.3; 1526 -8.7; 1678 -7.2; 1846 -3.8; 2031 -0.7; 2234 -0.9; 2457 -4.2; 2703 -6.4; 2973 -7.4; 3270 -6.7; 3597 -5.0; 3957 -4.1; 4353 -4.2; 4788 -2.9; 5267 -4.0; 5793 -6.2; 6373 -6.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.5; 13660 -8.0; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss ESP950 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.15 | 6.3 dB  |
| Peaking | 55 Hz    | 2.94 | 3.7 dB  |
| Peaking | 2093 Hz  | 2.42 | 13.6 dB |
| Peaking | 2114 Hz  | 0.51 | -8.3 dB |
| Peaking | 4430 Hz  | 1.26 | 6.7 dB  |
| Peaking | 70 Hz    | 4.19 | 2.1 dB  |
| Peaking | 81 Hz    | 3.04 | -1.8 dB |
| Peaking | 193 Hz   | 1.59 | -1.3 dB |
| Peaking | 680 Hz   | 4.09 | 1.2 dB  |
| Peaking | 12756 Hz | 5.97 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
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