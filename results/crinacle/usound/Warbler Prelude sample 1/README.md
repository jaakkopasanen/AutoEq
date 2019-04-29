# Warbler Prelude sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.5; 31 -2.2; 34 -2.8; 37 -3.3; 41 -3.8; 45 -4.2; 49 -4.6; 54 -5.0; 60 -5.5; 66 -6.0; 72 -6.6; 79 -7.0; 87 -7.4; 96 -8.1; 106 -8.7; 116 -9.0; 128 -9.5; 141 -9.9; 155 -10.2; 170 -10.5; 187 -10.6; 206 -10.8; 227 -10.9; 249 -10.9; 274 -10.9; 302 -10.9; 332 -10.8; 365 -10.7; 402 -10.6; 442 -10.5; 486 -10.3; 535 -10.0; 588 -9.7; 647 -9.4; 712 -9.0; 783 -8.5; 861 -8.0; 947 -7.8; 1042 -7.9; 1146 -8.5; 1261 -9.2; 1387 -9.6; 1526 -9.4; 1678 -8.7; 1846 -7.9; 2031 -7.2; 2234 -6.7; 2457 -6.6; 2703 -6.7; 2973 -7.0; 3270 -6.9; 3597 -5.6; 3957 -3.2; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Warbler Prelude sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Warbler Prelude sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.39 | 6.7 dB  |
| Peaking | 249 Hz  | 0.4  | -4.7 dB |
| Peaking | 1482 Hz | 2.51 | -2.5 dB |
| Peaking | 5218 Hz | 2.05 | 7.1 dB  |
| Peaking | 3243 Hz | 3.67 | -1.7 dB |
| Peaking | 4295 Hz | 4.8  | 3.0 dB  |
| Peaking | 4617 Hz | 0.38 | 0.6 dB  |
| Peaking | 6209 Hz | 1.13 | -3.7 dB |
| Peaking | 6374 Hz | 3.98 | 4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Warbler%20Prelude%20sample%201/Warbler%20Prelude%20sample%201.png)