# ARC Pollux
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.4; 25 -1.5; 28 -1.6; 31 -1.7; 34 -1.8; 37 -1.9; 41 -2.0; 45 -2.2; 49 -2.3; 54 -2.5; 60 -2.7; 66 -3.1; 72 -3.4; 79 -3.8; 87 -4.3; 96 -4.8; 106 -5.2; 116 -5.6; 128 -6.0; 141 -6.4; 155 -6.7; 170 -6.9; 187 -7.2; 206 -7.3; 227 -7.5; 249 -7.6; 274 -7.6; 302 -7.7; 332 -7.7; 365 -7.7; 402 -7.7; 442 -7.8; 486 -7.7; 535 -7.7; 588 -7.6; 647 -7.5; 712 -7.3; 783 -7.1; 861 -7.0; 947 -7.2; 1042 -7.7; 1146 -8.6; 1261 -9.6; 1387 -10.2; 1526 -10.3; 1678 -10.0; 1846 -9.5; 2031 -8.7; 2234 -7.7; 2457 -6.2; 2703 -4.6; 2973 -2.9; 3270 -1.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -3.3; 5267 -2.4; 5793 -1.4; 6373 -1.9; 7010 -5.9; 7711 -11.7; 8482 -11.4; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ARC Pollux GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ARC Pollux ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.61 | 5.4 dB  |
| Peaking | 1740 Hz | 0.88 | -4.7 dB |
| Peaking | 3517 Hz | 1.43 | 7.4 dB  |
| Peaking | 6218 Hz | 3.05 | 5.2 dB  |
| Peaking | 7937 Hz | 4.37 | -8.3 dB |
| Peaking | 34 Hz   | 1.1  | -3.1 dB |
| Peaking | 36 Hz   | 0.32 | 2.6 dB  |
| Peaking | 235 Hz  | 0.41 | -1.7 dB |
| Peaking | 976 Hz  | 1.49 | 1.7 dB  |
| Peaking | 1321 Hz | 3.14 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/ARC%20Pollux/ARC%20Pollux.png)