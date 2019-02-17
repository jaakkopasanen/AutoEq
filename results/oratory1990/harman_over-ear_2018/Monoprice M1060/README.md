# Monoprice M1060
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.7; 28 -1.0; 31 -1.2; 34 -1.3; 37 -1.4; 41 -1.6; 45 -1.8; 49 -2.0; 54 -2.4; 60 -2.7; 66 -2.9; 72 -3.1; 79 -3.4; 87 -3.8; 96 -4.1; 106 -4.5; 116 -4.8; 128 -5.1; 141 -5.5; 155 -5.7; 170 -5.9; 187 -6.1; 206 -6.2; 227 -6.2; 249 -6.0; 274 -5.5; 302 -4.8; 332 -4.2; 365 -3.8; 402 -3.7; 442 -3.8; 486 -4.3; 535 -4.7; 588 -5.0; 647 -5.4; 712 -5.6; 783 -5.4; 861 -4.8; 947 -4.2; 1042 -4.4; 1146 -4.9; 1261 -5.4; 1387 -5.5; 1526 -5.6; 1678 -6.2; 1846 -6.7; 2031 -6.4; 2234 -6.2; 2457 -6.1; 2703 -5.9; 2973 -5.9; 3270 -5.5; 3597 -4.8; 3957 -5.3; 4353 -6.5; 4788 -5.0; 5267 -3.4; 5793 -3.3; 6373 -1.1; 7010 -1.8; 7711 -4.0; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.6; 12418 -4.3; 13660 -4.3; 15026 -5.6; 16529 -11.7; 18182 -18.3; 20000 -24.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice M1060 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice M1060 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.67 | 3.1 dB  |
| Peaking | 53 Hz    | 1.15 | 1.2 dB  |
| Peaking | 196 Hz   | 1.39 | -2.2 dB |
| Peaking | 6407 Hz  | 2.24 | 5.2 dB  |
| Peaking | 17462 Hz | 0    | -2.8 dB |
| Peaking | 182 Hz   | 0.43 | 2.0 dB  |
| Peaking | 405 Hz   | 1.73 | 2.3 dB  |
| Peaking | 1043 Hz  | 1.7  | 2.2 dB  |
| Peaking | 3449 Hz  | 3.25 | 1.4 dB  |
| Peaking | 11308 Hz | 1.76 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Monoprice%20M1060/Monoprice%20M1060.png)