# Unique Melody 3DD-Ti
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.0; 25 -8.8; 28 -8.5; 31 -8.2; 34 -8.0; 37 -7.8; 41 -7.5; 45 -7.3; 49 -7.2; 54 -7.0; 60 -6.9; 66 -6.8; 72 -6.7; 79 -6.8; 87 -6.9; 96 -7.0; 106 -7.2; 116 -7.3; 128 -7.4; 141 -7.5; 155 -7.6; 170 -7.6; 187 -7.6; 206 -7.6; 227 -7.5; 249 -7.4; 274 -7.3; 302 -7.1; 332 -6.8; 365 -6.5; 402 -6.2; 442 -6.0; 486 -5.8; 535 -5.5; 588 -5.3; 647 -5.3; 712 -5.7; 783 -6.4; 861 -7.0; 947 -8.2; 1042 -9.7; 1146 -11.5; 1261 -12.6; 1387 -12.6; 1526 -11.2; 1678 -9.1; 1846 -6.7; 2031 -4.4; 2234 -2.6; 2457 -2.0; 2703 -3.1; 2973 -8.1; 3270 -12.5; 3597 -6.4; 3957 -1.7; 4353 -0.5; 4788 -0.9; 5267 -2.4; 5793 -7.8; 6373 -9.1; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -8.0; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -15.7; 16529 -22.6; 18182 -21.6; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3DD-Ti GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3DD-Ti ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 1352 Hz  |  2.42 | -7.7 dB  |
| Peaking | 2488 Hz  |  2.05 | 6.3 dB   |
| Peaking | 3219 Hz  |  5.26 | -10.6 dB |
| Peaking | 4353 Hz  |  2.85 | 7.2 dB   |
| Peaking | 17571 Hz |  1.33 | -18.8 dB |
| Peaking | 26 Hz    |  0.02 | -0.9 dB  |
| Peaking | 591 Hz   |  1.51 | 2.4 dB   |
| Peaking | 6098 Hz  | 12.27 | -5.4 dB  |
| Peaking | 13573 Hz |  1.53 | 5.7 dB   |
| Peaking | 15536 Hz |  2.46 | -7.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB   |
| Peaking | 125 Hz   | 1.41 | -0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -15.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%203DD-Ti/Unique%20Melody%203DD-Ti.png)