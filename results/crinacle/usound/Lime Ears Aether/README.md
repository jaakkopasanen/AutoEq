# Lime Ears Aether
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.6; 25 -4.8; 28 -5.0; 31 -5.2; 34 -5.4; 37 -5.5; 41 -5.7; 45 -5.8; 49 -5.9; 54 -6.0; 60 -6.2; 66 -6.4; 72 -6.7; 79 -7.0; 87 -7.2; 96 -7.7; 106 -7.9; 116 -8.1; 128 -8.4; 141 -8.6; 155 -8.8; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.8; 249 -8.8; 274 -8.6; 302 -8.5; 332 -8.3; 365 -8.0; 402 -7.9; 442 -7.6; 486 -7.4; 535 -7.2; 588 -7.1; 647 -7.0; 712 -7.0; 783 -6.9; 861 -6.9; 947 -7.0; 1042 -7.4; 1146 -8.1; 1261 -8.7; 1387 -8.9; 1526 -8.5; 1678 -7.6; 1846 -6.7; 2031 -6.1; 2234 -5.7; 2457 -5.7; 2703 -5.5; 2973 -4.7; 3270 -3.2; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -4.7; 5793 -2.7; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -9.1; 9330 -8.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Aether GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Aether ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 207 Hz  |  0.77 | -2.6 dB |
| Peaking | 1366 Hz |  2.72 | -2.7 dB |
| Peaking | 4021 Hz |  2.3  | 6.5 dB  |
| Peaking | 6353 Hz |  5.27 | 5.2 dB  |
| Peaking | 8746 Hz |  4.63 | -3.8 dB |
| Peaking | 17 Hz   |  1.11 | 0.9 dB  |
| Peaking | 26 Hz   |  0.88 | 1.4 dB  |
| Peaking | 2118 Hz |  7.99 | 0.5 dB  |
| Peaking | 5334 Hz | 15.22 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20Aether/Lime%20Ears%20Aether.png)