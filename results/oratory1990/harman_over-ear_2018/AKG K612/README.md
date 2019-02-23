# AKG K612
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.3; 45 -1.5; 49 -1.4; 54 -1.0; 60 -0.9; 66 -1.7; 72 -2.5; 79 -3.0; 87 -3.7; 96 -4.3; 106 -4.8; 116 -5.3; 128 -5.7; 141 -6.1; 155 -6.3; 170 -6.5; 187 -6.7; 206 -6.8; 227 -6.9; 249 -6.9; 274 -6.7; 302 -6.4; 332 -6.1; 365 -6.0; 402 -5.9; 442 -5.7; 486 -5.5; 535 -5.3; 588 -5.1; 647 -4.7; 712 -4.5; 783 -5.1; 861 -5.7; 947 -5.8; 1042 -5.8; 1146 -5.6; 1261 -5.7; 1387 -6.4; 1526 -7.5; 1678 -8.5; 1846 -9.2; 2031 -9.3; 2234 -8.9; 2457 -9.6; 2703 -8.9; 2973 -8.9; 3270 -7.3; 3597 -7.3; 3957 -6.2; 4353 -5.4; 4788 -6.4; 5267 -6.9; 5793 -8.7; 6373 -8.6; 7010 -8.5; 7711 -8.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.3; 13660 -6.9; 15026 -6.5; 16529 -8.7; 18182 -12.9; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K612 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.75 | 6.0 dB  |
| Peaking | 61 Hz    | 1.54 | 3.6 dB  |
| Peaking | 2274 Hz  | 2.25 | -3.3 dB |
| Peaking | 6617 Hz  | 3.31 | -2.3 dB |
| Peaking | 18844 Hz | 1.22 | -7.4 dB |
| Peaking | 668 Hz   | 2.11 | 2.0 dB  |
| Peaking | 1249 Hz  | 2.94 | 1.2 dB  |
| Peaking | 1706 Hz  | 3.83 | -1.4 dB |
| Peaking | 4387 Hz  | 6.89 | 1.8 dB  |
| Peaking | 15336 Hz | 4.91 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K612/AKG%20K612.png)