# AKG K601
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.5; 79 -2.4; 87 -3.1; 96 -3.7; 106 -4.3; 116 -4.8; 128 -5.3; 141 -5.6; 155 -5.9; 170 -6.0; 187 -6.2; 206 -6.3; 227 -6.4; 249 -6.4; 274 -6.2; 302 -6.0; 332 -5.7; 365 -5.6; 402 -5.5; 442 -5.3; 486 -5.2; 535 -4.9; 588 -4.7; 647 -4.4; 712 -4.2; 783 -4.6; 861 -5.2; 947 -5.7; 1042 -6.1; 1146 -6.7; 1261 -7.1; 1387 -7.7; 1526 -8.5; 1678 -9.4; 1846 -10.1; 2031 -11.0; 2234 -11.6; 2457 -11.7; 2703 -11.3; 2973 -9.9; 3270 -7.5; 3597 -7.2; 3957 -7.8; 4353 -6.4; 4788 -5.2; 5267 -4.3; 5793 -5.7; 6373 -6.2; 7010 -5.6; 7711 -7.6; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -6.5; 16529 -6.8; 18182 -10.3; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.56 | 6.8 dB  |
| Peaking | 717 Hz   | 1.48 | 2.3 dB  |
| Peaking | 2325 Hz  | 1.38 | -6.7 dB |
| Peaking | 9304 Hz  | 0.25 | 4.1 dB  |
| Peaking | 20563 Hz | 0.05 | -4.7 dB |
| Peaking | 70 Hz    | 1.46 | 2.8 dB  |
| Peaking | 73 Hz    | 0.62 | -1.7 dB |
| Peaking | 5240 Hz  | 4.17 | 2.5 dB  |
| Peaking | 6576 Hz  | 0.8  | -1.5 dB |
| Peaking | 15579 Hz | 2.32 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601/AKG%20K601.png)