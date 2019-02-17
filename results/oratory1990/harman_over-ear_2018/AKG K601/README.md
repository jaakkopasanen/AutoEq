# AKG K601
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.0; 72 -2.1; 79 -3.0; 87 -3.7; 96 -4.3; 106 -4.9; 116 -5.4; 128 -5.9; 141 -6.2; 155 -6.5; 170 -6.6; 187 -6.8; 206 -6.9; 227 -7.0; 249 -7.0; 274 -6.8; 302 -6.5; 332 -6.3; 365 -6.2; 402 -6.1; 442 -5.9; 486 -5.8; 535 -5.5; 588 -5.3; 647 -5.0; 712 -4.8; 783 -5.2; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -7.3; 1261 -7.7; 1387 -8.3; 1526 -9.1; 1678 -10.0; 1846 -10.7; 2031 -11.6; 2234 -12.2; 2457 -12.3; 2703 -11.9; 2973 -10.5; 3270 -8.1; 3597 -7.8; 3957 -8.4; 4353 -6.9; 4788 -5.8; 5267 -4.9; 5793 -6.3; 6373 -6.7; 7010 -6.2; 7711 -8.2; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -7.3; 15026 -6.5; 16529 -7.2; 18182 -10.9; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.66 | 6.9 dB  |
| Peaking | 705 Hz   | 2.13 | 2.1 dB  |
| Peaking | 2280 Hz  | 1.42 | -6.1 dB |
| Peaking | 5122 Hz  | 4.75 | 2.5 dB  |
| Peaking | 19686 Hz | 1.11 | -8.1 dB |
| Peaking | 37 Hz    | 3.07 | -1.1 dB |
| Peaking | 65 Hz    | 2.84 | 1.6 dB  |
| Peaking | 179 Hz   | 1.27 | -1.1 dB |
| Peaking | 8057 Hz  | 6.7  | -2.7 dB |
| Peaking | 8850 Hz  | 1.19 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601/AKG%20K601.png)