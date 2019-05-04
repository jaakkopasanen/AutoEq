# Beats Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -4.0; 25 -4.6; 28 -5.5; 31 -6.2; 34 -6.8; 37 -7.2; 41 -7.6; 45 -7.9; 49 -8.1; 54 -8.1; 60 -8.1; 66 -8.1; 72 -8.1; 79 -8.2; 87 -8.5; 96 -9.0; 106 -9.3; 116 -9.3; 128 -9.5; 141 -9.7; 155 -9.9; 170 -9.8; 187 -9.7; 206 -9.4; 227 -8.8; 249 -8.1; 274 -7.1; 302 -5.7; 332 -4.9; 365 -3.9; 402 -3.0; 442 -2.7; 486 -2.8; 535 -3.0; 588 -3.0; 647 -2.9; 712 -2.5; 783 -2.5; 861 -2.2; 947 -1.2; 1042 -1.4; 1146 -1.1; 1261 -0.7; 1387 -0.5; 1526 -0.8; 1678 -1.5; 1846 -2.7; 2031 -4.3; 2234 -6.3; 2457 -8.3; 2703 -10.2; 2973 -10.7; 3270 -8.6; 3597 -4.8; 3957 -1.0; 4353 -1.8; 4788 -3.9; 5267 -2.5; 5793 -3.0; 6373 -5.8; 7010 -7.2; 7711 -8.0; 8482 -5.2; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 81 Hz   | 0.59 | -3.3 dB  |
| Peaking | 185 Hz  | 1.36 | -4.1 dB  |
| Peaking | 1931 Hz | 0.46 | 13.3 dB  |
| Peaking | 2924 Hz | 0.84 | -21.4 dB |
| Peaking | 4014 Hz | 1.71 | 10.1 dB  |
| Peaking | 19 Hz   | 2.88 | 2.6 dB   |
| Peaking | 410 Hz  | 5.08 | 1.5 dB   |
| Peaking | 5593 Hz | 8.29 | 2.8 dB   |
| Peaking | 7491 Hz | 3.03 | -4.1 dB  |
| Peaking | 8755 Hz | 2    | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beats%20Pro/Beats%20Pro.png)