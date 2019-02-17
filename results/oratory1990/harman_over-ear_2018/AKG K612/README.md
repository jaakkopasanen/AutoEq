# AKG K612
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.8; 34 -1.2; 37 -1.6; 41 -2.0; 45 -2.2; 49 -2.1; 54 -1.7; 60 -1.6; 66 -2.4; 72 -3.2; 79 -3.7; 87 -4.4; 96 -5.0; 106 -5.5; 116 -6.0; 128 -6.4; 141 -6.8; 155 -6.9; 170 -7.2; 187 -7.4; 206 -7.5; 227 -7.6; 249 -7.5; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.7; 402 -6.6; 442 -6.4; 486 -6.2; 535 -6.0; 588 -5.8; 647 -5.4; 712 -5.2; 783 -5.8; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.3; 1261 -6.4; 1387 -7.1; 1526 -8.2; 1678 -9.2; 1846 -9.9; 2031 -10.0; 2234 -9.6; 2457 -10.3; 2703 -9.6; 2973 -9.5; 3270 -7.9; 3597 -7.9; 3957 -6.9; 4353 -6.1; 4788 -7.1; 5267 -7.6; 5793 -9.4; 6373 -9.3; 7010 -9.2; 7711 -9.3; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.0; 13660 -7.4; 15026 -6.5; 16529 -9.4; 18182 -13.6; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K612 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.98 | 6.2 dB  |
| Peaking | 60 Hz    | 2.04 | 3.6 dB  |
| Peaking | 2256 Hz  | 1.74 | -3.9 dB |
| Peaking | 6590 Hz  | 2.88 | -3.0 dB |
| Peaking | 18850 Hz | 1.13 | -8.1 dB |
| Peaking | 218 Hz   | 1.41 | -1.4 dB |
| Peaking | 680 Hz   | 2.05 | 1.4 dB  |
| Peaking | 2924 Hz  | 6.68 | -0.8 dB |
| Peaking | 9486 Hz  | 4.82 | 0.9 dB  |
| Peaking | 17475 Hz | 6.81 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K612/AKG%20K612.png)