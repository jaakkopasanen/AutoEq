# Focal Sphear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.4; 34 -2.8; 37 -3.1; 41 -3.5; 45 -3.9; 49 -4.2; 54 -4.5; 60 -4.9; 66 -5.3; 72 -5.7; 79 -6.1; 87 -6.5; 96 -6.9; 106 -7.3; 116 -7.5; 128 -7.8; 141 -7.9; 155 -8.1; 170 -8.0; 187 -8.0; 206 -7.8; 227 -7.5; 249 -7.3; 274 -7.0; 302 -6.6; 332 -6.2; 365 -5.8; 402 -5.3; 442 -4.9; 486 -4.5; 535 -4.0; 588 -3.5; 647 -3.0; 712 -2.4; 783 -1.8; 861 -1.4; 947 -1.1; 1042 -1.3; 1146 -1.9; 1261 -2.6; 1387 -3.2; 1526 -3.3; 1678 -3.2; 1846 -2.8; 2031 -2.8; 2234 -2.9; 2457 -3.3; 2703 -3.3; 2973 -2.9; 3270 -2.1; 3597 -1.4; 3957 -1.0; 4353 -1.4; 4788 -2.9; 5267 -6.5; 5793 -8.5; 6373 -4.8; 7010 -3.0; 7711 -6.1; 8482 -8.0; 9330 -4.6; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Sphear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Sphear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.55 | 5.0 dB  |
| Peaking | 162 Hz  | 0.54 | -3.8 dB |
| Peaking | 902 Hz  | 1.06 | 3.5 dB  |
| Peaking | 4001 Hz | 2.03 | 3.8 dB  |
| Peaking | 5619 Hz | 5.63 | -5.6 dB |
| Peaking | 20 Hz   | 0.3  | 0.3 dB  |
| Peaking | 1416 Hz | 4.89 | -0.7 dB |
| Peaking | 2006 Hz | 4.31 | 0.8 dB  |
| Peaking | 6950 Hz | 6.99 | 2.3 dB  |
| Peaking | 8246 Hz | 6.22 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Focal%20Sphear/Focal%20Sphear.png)