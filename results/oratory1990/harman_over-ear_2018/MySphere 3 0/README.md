# MySphere 3 0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.5; 37 -1.9; 41 -2.0; 45 -2.0; 49 -1.9; 54 -2.0; 60 -2.3; 66 -2.6; 72 -2.9; 79 -3.2; 87 -3.6; 96 -4.1; 106 -4.8; 116 -5.7; 128 -6.5; 141 -7.0; 155 -7.0; 170 -7.2; 187 -7.5; 206 -7.8; 227 -8.1; 249 -7.9; 274 -7.6; 302 -7.5; 332 -7.4; 365 -7.1; 402 -6.5; 442 -6.5; 486 -7.1; 535 -7.7; 588 -7.8; 647 -7.8; 712 -8.4; 783 -9.2; 861 -8.9; 947 -7.8; 1042 -7.4; 1146 -7.8; 1261 -8.3; 1387 -8.6; 1526 -8.9; 1678 -9.3; 1846 -9.7; 2031 -9.4; 2234 -8.6; 2457 -8.9; 2703 -8.9; 2973 -6.9; 3270 -4.4; 3597 -3.2; 3957 -4.0; 4353 -5.0; 4788 -4.1; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -11.4; 11289 -14.4; 12418 -14.6; 13660 -14.2; 15026 -13.9; 16529 -14.1; 18182 -15.3; 20000 -18.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MySphere 3 0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MySphere 3 0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.88 | 6.1 dB  |
| Peaking | 64 Hz    | 1.59 | 3.2 dB  |
| Peaking | 1524 Hz  | 0.36 | -2.5 dB |
| Peaking | 5898 Hz  | 0.97 | 11.6 dB |
| Peaking | 19383 Hz | 0.08 | -9.7 dB |
| Peaking | 3381 Hz  | 1.49 | -4.0 dB |
| Peaking | 3496 Hz  | 3.52 | 6.9 dB  |
| Peaking | 9283 Hz  | 5.31 | 3.4 dB  |
| Peaking | 11338 Hz | 2.47 | -3.0 dB |
| Peaking | 16119 Hz | 1.67 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 3.7 dB   |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -13.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MySphere%203%200/MySphere%203%200.png)