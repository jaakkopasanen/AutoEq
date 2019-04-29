# Jomo Quatre Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.5; 25 -9.5; 28 -9.4; 31 -9.3; 34 -9.2; 37 -9.1; 41 -9.0; 45 -8.9; 49 -8.9; 54 -8.8; 60 -8.8; 66 -8.8; 72 -8.9; 79 -9.0; 87 -9.2; 96 -9.5; 106 -9.7; 116 -9.8; 128 -9.9; 141 -10.1; 155 -10.2; 170 -10.2; 187 -10.2; 206 -10.2; 227 -10.1; 249 -9.9; 274 -9.8; 302 -9.6; 332 -9.4; 365 -9.1; 402 -8.9; 442 -8.5; 486 -8.2; 535 -7.8; 588 -7.3; 647 -6.8; 712 -6.3; 783 -5.6; 861 -5.1; 947 -4.8; 1042 -4.9; 1146 -5.4; 1261 -6.0; 1387 -6.3; 1526 -6.3; 1678 -5.9; 1846 -5.6; 2031 -5.3; 2234 -4.9; 2457 -3.7; 2703 -1.6; 2973 -0.5; 3270 -0.5; 3597 -0.9; 3957 -2.6; 4353 -4.7; 4788 -7.7; 5267 -6.8; 5793 -2.9; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Quatre Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Quatre Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.17 | -2.9 dB |
| Peaking | 168 Hz  | 0.89 | -3.2 dB |
| Peaking | 335 Hz  | 1.72 | -1.8 dB |
| Peaking | 3135 Hz | 2.33 | 6.7 dB  |
| Peaking | 6372 Hz | 6.45 | 5.1 dB  |
| Peaking | 498 Hz  | 3.13 | -0.6 dB |
| Peaking | 931 Hz  | 2.76 | 2.0 dB  |
| Peaking | 4065 Hz | 3.83 | 2.7 dB  |
| Peaking | 4979 Hz | 2.67 | -4.4 dB |
| Peaking | 5730 Hz | 5.51 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Quatre%20Black/Jomo%20Quatre%20Black.png)