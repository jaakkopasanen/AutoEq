# Lime Ears LE2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.1; 25 -4.2; 28 -4.3; 31 -4.5; 34 -4.6; 37 -4.7; 41 -5.0; 45 -5.3; 49 -5.5; 54 -5.6; 60 -5.8; 66 -6.1; 72 -6.5; 79 -6.8; 87 -7.2; 96 -7.8; 106 -8.2; 116 -8.5; 128 -8.9; 141 -9.2; 155 -9.5; 170 -9.7; 187 -9.9; 206 -9.9; 227 -9.9; 249 -9.9; 274 -9.9; 302 -9.8; 332 -9.7; 365 -9.5; 402 -9.3; 442 -9.2; 486 -8.9; 535 -8.5; 588 -8.2; 647 -7.8; 712 -7.3; 783 -6.8; 861 -6.4; 947 -6.2; 1042 -6.5; 1146 -7.1; 1261 -7.9; 1387 -8.5; 1526 -8.7; 1678 -8.8; 1846 -9.1; 2031 -9.4; 2234 -8.7; 2457 -6.2; 2703 -3.2; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -5.6; 5793 -4.0; 6373 -1.6; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -10.0; 18182 -11.8; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears LE2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears LE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 246 Hz   |  0.7  | -3.8 dB |
| Peaking | 2087 Hz  |  1.6  | -5.2 dB |
| Peaking | 2906 Hz  |  3.2  | 3.4 dB  |
| Peaking | 3844 Hz  |  1.18 | 6.5 dB  |
| Peaking | 18552 Hz |  1.07 | -5.9 dB |
| Peaking | 23 Hz    |  1.18 | 2.5 dB  |
| Peaking | 44 Hz    |  1.77 | 1.1 dB  |
| Peaking | 921 Hz   |  5.05 | 1.3 dB  |
| Peaking | 5365 Hz  | 11.33 | -3.6 dB |
| Peaking | 6327 Hz  |  9.34 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20LE2/Lime%20Ears%20LE2.png)