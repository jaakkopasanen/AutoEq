# Brainwavz B400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.4; 41 -2.1; 45 -2.8; 49 -3.4; 54 -3.9; 60 -4.5; 66 -5.2; 72 -5.9; 79 -6.5; 87 -7.2; 96 -7.9; 106 -8.5; 116 -9.1; 128 -9.6; 141 -10.0; 155 -10.4; 170 -10.7; 187 -11.0; 206 -11.0; 227 -11.1; 249 -11.0; 274 -10.9; 302 -10.7; 332 -10.5; 365 -10.3; 402 -10.0; 442 -9.7; 486 -9.3; 535 -8.8; 588 -8.2; 647 -7.7; 712 -6.9; 783 -6.3; 861 -5.6; 947 -5.3; 1042 -5.3; 1146 -5.8; 1261 -6.4; 1387 -6.4; 1526 -5.9; 1678 -4.8; 1846 -3.5; 2031 -2.4; 2234 -1.6; 2457 -1.4; 2703 -1.9; 2973 -3.5; 3270 -5.4; 3597 -6.1; 3957 -5.0; 4353 -2.4; 4788 -2.0; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.8; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz B400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz B400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.62 | 6.5 dB  |
| Peaking | 209 Hz  | 0.59 | -5.1 dB |
| Peaking | 2298 Hz | 2.15 | 5.2 dB  |
| Peaking | 5780 Hz | 2.06 | 6.3 dB  |
| Peaking | 8709 Hz | 4.02 | -4.1 dB |
| Peaking | 510 Hz  | 1.51 | -1.2 dB |
| Peaking | 1052 Hz | 1.07 | 2.7 dB  |
| Peaking | 1338 Hz | 2.14 | -2.5 dB |
| Peaking | 3580 Hz | 5.39 | -2.1 dB |
| Peaking | 4418 Hz | 8.7  | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Brainwavz%20B400/Brainwavz%20B400.png)