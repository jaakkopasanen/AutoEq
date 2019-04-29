# Unique Melody 3X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.7; 34 -2.0; 37 -2.4; 41 -2.8; 45 -3.2; 49 -3.5; 54 -3.9; 60 -4.4; 66 -4.8; 72 -5.2; 79 -5.6; 87 -6.2; 96 -6.7; 106 -7.2; 116 -7.7; 128 -8.0; 141 -8.4; 155 -8.7; 170 -8.9; 187 -9.2; 206 -9.4; 227 -9.5; 249 -9.5; 274 -9.6; 302 -9.7; 332 -9.7; 365 -9.7; 402 -9.7; 442 -9.7; 486 -9.7; 535 -9.6; 588 -9.6; 647 -9.5; 712 -9.3; 783 -9.1; 861 -9.0; 947 -9.1; 1042 -9.4; 1146 -10.0; 1261 -10.4; 1387 -10.1; 1526 -9.1; 1678 -7.6; 1846 -5.7; 2031 -3.8; 2234 -2.3; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.3; 6373 -9.4; 7010 -12.6; 7711 -8.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.24 | 6.4 dB   |
| Peaking | 333 Hz   | 0.28 | -3.6 dB  |
| Peaking | 1378 Hz  | 1.84 | -5.0 dB  |
| Peaking | 3485 Hz  | 0.62 | 7.8 dB   |
| Peaking | 6955 Hz  | 4.5  | -10.7 dB |
| Peaking | 2512 Hz  | 2.72 | 1.9 dB   |
| Peaking | 3057 Hz  | 1.31 | -1.4 dB  |
| Peaking | 5444 Hz  | 5.86 | 2.9 dB   |
| Peaking | 10873 Hz | 1.24 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%203X/Unique%20Melody%203X.png)