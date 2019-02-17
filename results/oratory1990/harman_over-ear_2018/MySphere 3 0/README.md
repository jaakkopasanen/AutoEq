# MySphere 3 0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.2; 45 -1.1; 49 -1.0; 54 -1.1; 60 -1.4; 66 -1.6; 72 -2.0; 79 -2.3; 87 -2.7; 96 -3.2; 106 -4.0; 116 -4.8; 128 -5.6; 141 -6.2; 155 -6.1; 170 -6.3; 187 -6.5; 206 -6.9; 227 -7.2; 249 -7.0; 274 -6.7; 302 -6.6; 332 -6.5; 365 -6.2; 402 -5.6; 442 -5.6; 486 -6.2; 535 -6.8; 588 -6.9; 647 -6.9; 712 -7.5; 783 -8.3; 861 -8.0; 947 -6.9; 1042 -6.5; 1146 -6.9; 1261 -7.5; 1387 -7.7; 1526 -8.0; 1678 -8.4; 1846 -8.8; 2031 -8.5; 2234 -7.7; 2457 -7.9; 2703 -8.0; 2973 -6.0; 3270 -3.5; 3597 -2.3; 3957 -3.1; 4353 -4.2; 4788 -3.2; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -10.5; 11289 -13.5; 12418 -13.7; 13660 -13.3; 15026 -13.0; 16529 -13.2; 18182 -14.4; 20000 -17.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MySphere 3 0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MySphere 3 0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.7  | 6.0 dB  |
| Peaking | 68 Hz    | 1.37 | 3.3 dB  |
| Peaking | 3509 Hz  | 3.77 | 5.0 dB  |
| Peaking | 5955 Hz  | 1.06 | 13.0 dB |
| Peaking | 18544 Hz | 0.05 | -8.4 dB |
| Peaking | 427 Hz   | 4.17 | 1.5 dB  |
| Peaking | 3650 Hz  | 0.01 | -0.3 dB |
| Peaking | 9555 Hz  | 4.41 | 3.6 dB  |
| Peaking | 11284 Hz | 2.63 | -2.5 dB |
| Peaking | 15939 Hz | 1.67 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.5 dB   |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | -0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -12.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MySphere%203%200/MySphere%203%200.png)