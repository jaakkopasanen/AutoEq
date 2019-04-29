# Unique Melody 3DD-Ti Open
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.0; 25 -6.0; 28 -6.0; 31 -5.9; 34 -5.8; 37 -5.7; 41 -5.6; 45 -5.5; 49 -5.4; 54 -5.3; 60 -5.2; 66 -5.2; 72 -5.2; 79 -5.2; 87 -5.3; 96 -5.4; 106 -5.5; 116 -5.5; 128 -5.6; 141 -5.6; 155 -5.6; 170 -5.6; 187 -5.5; 206 -5.4; 227 -5.3; 249 -5.2; 274 -5.0; 302 -4.9; 332 -4.7; 365 -4.5; 402 -4.3; 442 -4.1; 486 -3.8; 535 -3.6; 588 -3.6; 647 -3.6; 712 -4.0; 783 -4.6; 861 -5.2; 947 -6.3; 1042 -7.9; 1146 -9.7; 1261 -11.1; 1387 -11.4; 1526 -10.2; 1678 -8.1; 1846 -5.8; 2031 -3.9; 2234 -2.7; 2457 -2.6; 2703 -4.1; 2973 -9.3; 3270 -13.6; 3597 -7.3; 3957 -2.2; 4353 -0.5; 4788 -0.7; 5267 -2.2; 5793 -7.9; 6373 -9.4; 7010 -4.1; 7711 -5.2; 8482 -5.4; 9330 -5.9; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3DD-Ti Open GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3DD-Ti Open ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 1381 Hz | 2.78 | -7.5 dB  |
| Peaking | 2530 Hz | 1.7  | 5.3 dB   |
| Peaking | 3230 Hz | 4.01 | -14.4 dB |
| Peaking | 4415 Hz | 1.71 | 7.0 dB   |
| Peaking | 6087 Hz | 6.42 | -7.9 dB  |
| Peaking | 26 Hz   | 1.62 | -0.6 dB  |
| Peaking | 596 Hz  | 1.13 | 2.2 dB   |
| Peaking | 1098 Hz | 4.82 | -1.9 dB  |
| Peaking | 1699 Hz | 7.73 | -1.0 dB  |
| Peaking | 9238 Hz | 5.62 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%203DD-Ti%20Open/Unique%20Melody%203DD-Ti%20Open.png)