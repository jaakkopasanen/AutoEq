# AKG N5005 Bass Boost
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -9.9; 31 -9.9; 34 -9.8; 37 -9.7; 41 -9.6; 45 -9.5; 49 -9.4; 54 -9.2; 60 -9.0; 66 -8.8; 72 -8.6; 79 -8.5; 87 -8.4; 96 -8.1; 106 -8.0; 116 -7.8; 128 -7.7; 141 -7.7; 155 -7.7; 170 -7.7; 187 -7.8; 206 -7.7; 227 -7.7; 249 -7.8; 274 -7.8; 302 -7.8; 332 -7.8; 365 -7.8; 402 -7.8; 442 -7.7; 486 -7.6; 535 -7.5; 588 -7.3; 647 -7.1; 712 -6.8; 783 -6.5; 861 -6.2; 947 -6.0; 1042 -6.1; 1146 -6.8; 1261 -7.7; 1387 -8.4; 1526 -8.8; 1678 -8.8; 1846 -8.6; 2031 -8.3; 2234 -7.4; 2457 -5.8; 2703 -4.1; 2973 -3.1; 3270 -3.3; 3597 -3.6; 3957 -4.1; 4353 -6.0; 4788 -6.4; 5267 -3.2; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -7.1; 8482 -7.7; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -7.7; 18182 -8.6; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 Bass Boost GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 Bass Boost ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.05 | -2.6 dB |
| Peaking | 1784 Hz  | 1.84 | -3.0 dB |
| Peaking | 3062 Hz  | 2.59 | 4.1 dB  |
| Peaking | 6122 Hz  | 3.77 | 6.6 dB  |
| Peaking | 8106 Hz  | 5.55 | -2.8 dB |
| Peaking | 30 Hz    | 1.01 | -1.0 dB |
| Peaking | 120 Hz   | 1.68 | 0.9 dB  |
| Peaking | 4645 Hz  | 6.08 | -3.8 dB |
| Peaking | 4656 Hz  | 2.38 | 1.7 dB  |
| Peaking | 17543 Hz | 2.77 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AKG%20N5005%20Bass%20Boost/AKG%20N5005%20Bass%20Boost.png)