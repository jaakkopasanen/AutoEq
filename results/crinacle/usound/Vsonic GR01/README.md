# Vsonic GR01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.3; 25 -2.7; 28 -3.1; 31 -3.5; 34 -3.8; 37 -4.0; 41 -4.4; 45 -4.6; 49 -4.9; 54 -5.2; 60 -5.6; 66 -5.9; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.5; 106 -7.9; 116 -8.4; 128 -8.7; 141 -9.1; 155 -9.3; 170 -9.5; 187 -9.7; 206 -9.9; 227 -9.9; 249 -9.8; 274 -9.8; 302 -9.7; 332 -9.6; 365 -9.4; 402 -9.3; 442 -9.1; 486 -8.9; 535 -8.6; 588 -8.3; 647 -7.8; 712 -7.3; 783 -6.7; 861 -6.1; 947 -5.8; 1042 -5.8; 1146 -6.2; 1261 -6.7; 1387 -6.7; 1526 -6.1; 1678 -5.2; 1846 -4.3; 2031 -3.6; 2234 -3.3; 2457 -3.3; 2703 -3.0; 2973 -2.3; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -2.7; 5267 -2.7; 5793 -3.1; 6373 -3.9; 7010 -4.8; 7711 -6.5; 8482 -9.2; 9330 -9.9; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic GR01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic GR01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.3  | 5.1 dB  |
| Peaking | 238 Hz  | 0.51 | -3.7 dB |
| Peaking | 3774 Hz | 0.84 | 5.7 dB  |
| Peaking | 8932 Hz | 3.84 | -5.1 dB |
| Peaking | 551 Hz  | 2.21 | -0.5 dB |
| Peaking | 962 Hz  | 2.11 | 1.4 dB  |
| Peaking | 1402 Hz | 2.06 | -1.8 dB |
| Peaking | 2086 Hz | 1.34 | 1.3 dB  |
| Peaking | 2635 Hz | 3.83 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vsonic%20GR01/Vsonic%20GR01.png)