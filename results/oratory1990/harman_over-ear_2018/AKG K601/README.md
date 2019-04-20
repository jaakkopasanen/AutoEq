# AKG K601
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.4; 79 -2.4; 87 -3.0; 96 -3.6; 106 -4.2; 116 -4.8; 128 -5.2; 141 -5.6; 155 -5.8; 170 -6.0; 187 -6.1; 206 -6.3; 227 -6.4; 249 -6.4; 274 -6.2; 302 -5.9; 332 -5.8; 365 -5.7; 402 -5.5; 442 -5.3; 486 -5.2; 535 -5.0; 588 -4.8; 647 -4.4; 712 -4.3; 783 -4.6; 861 -5.3; 947 -5.7; 1042 -6.2; 1146 -6.8; 1261 -7.2; 1387 -7.7; 1526 -8.5; 1678 -9.4; 1846 -10.1; 2031 -11.0; 2234 -11.6; 2457 -11.7; 2703 -11.2; 2973 -9.7; 3270 -7.6; 3597 -7.1; 3957 -7.7; 4353 -6.3; 4788 -5.0; 5267 -4.4; 5793 -5.5; 6373 -6.3; 7010 -6.1; 7711 -8.2; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -10.6; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.55 | 6.8 dB  |
| Peaking | 690 Hz  | 1.53 | 2.4 dB  |
| Peaking | 2282 Hz | 1.53 | -5.6 dB |
| Peaking | 5124 Hz | 2.95 | 2.7 dB  |
| Peaking | 7912 Hz | 7.94 | -2.2 dB |
| Peaking | 39 Hz   | 2.66 | -0.9 dB |
| Peaking | 66 Hz   | 2.96 | 1.4 dB  |
| Peaking | 163 Hz  | 1.41 | -0.7 dB |
| Peaking | 3317 Hz | 2.64 | -1.4 dB |
| Peaking | 3349 Hz | 5.82 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601/AKG%20K601.png)