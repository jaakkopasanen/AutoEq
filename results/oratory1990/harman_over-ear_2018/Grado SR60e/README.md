# Grado SR60e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.2; 54 -2.1; 60 -2.9; 66 -3.5; 72 -4.1; 79 -4.5; 87 -4.9; 96 -5.2; 106 -5.4; 116 -5.5; 128 -5.6; 141 -5.5; 155 -5.5; 170 -5.4; 187 -5.5; 206 -5.4; 227 -5.2; 249 -4.9; 274 -4.6; 302 -4.2; 332 -4.2; 365 -5.4; 402 -5.2; 442 -4.9; 486 -4.7; 535 -4.6; 588 -4.5; 647 -4.4; 712 -4.5; 783 -4.7; 861 -5.0; 947 -5.2; 1042 -5.2; 1146 -5.2; 1261 -5.3; 1387 -5.9; 1526 -7.1; 1678 -8.8; 1846 -13.0; 2031 -15.3; 2234 -12.8; 2457 -10.8; 2703 -9.2; 2973 -7.8; 3270 -6.3; 3597 -7.1; 3957 -8.2; 4353 -8.4; 4788 -7.5; 5267 -8.1; 5793 -7.7; 6373 -7.1; 7010 -5.4; 7711 -6.4; 8482 -7.7; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -10.5; 16529 -8.6; 18182 -6.8; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.7  | 6.6 dB   |
| Peaking | 544 Hz   | 0.51 | 2.0 dB   |
| Peaking | 1547 Hz  | 1.74 | 2.8 dB   |
| Peaking | 2001 Hz  | 2.48 | -10.7 dB |
| Peaking | 15364 Hz | 2.38 | -4.3 dB  |
| Peaking | 322 Hz   | 4.06 | 1.4 dB   |
| Peaking | 371 Hz   | 4.32 | -1.4 dB  |
| Peaking | 3310 Hz  | 5.65 | 2.3 dB   |
| Peaking | 4507 Hz  | 1.4  | -1.5 dB  |
| Peaking | 7127 Hz  | 8.72 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Grado%20SR60e/Grado%20SR60e.png)