# AKG N5005 Reference
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.2; 25 -7.3; 28 -7.4; 31 -7.3; 34 -7.2; 37 -7.1; 41 -7.0; 45 -6.9; 49 -6.8; 54 -6.6; 60 -6.4; 66 -6.2; 72 -6.0; 79 -5.9; 87 -5.8; 96 -5.5; 106 -5.3; 116 -5.2; 128 -5.1; 141 -4.9; 155 -4.9; 170 -4.8; 187 -4.9; 206 -4.8; 227 -4.8; 249 -4.9; 274 -4.9; 302 -5.0; 332 -4.9; 365 -4.9; 402 -4.9; 442 -4.9; 486 -4.8; 535 -4.7; 588 -4.6; 647 -4.4; 712 -4.1; 783 -3.9; 861 -3.5; 947 -3.3; 1042 -3.4; 1146 -4.2; 1261 -5.1; 1387 -5.8; 1526 -6.1; 1678 -6.1; 1846 -5.9; 2031 -5.5; 2234 -4.7; 2457 -3.4; 2703 -2.0; 2973 -1.3; 3270 -1.7; 3597 -2.1; 3957 -2.8; 4353 -4.5; 4788 -4.9; 5267 -2.1; 5793 -0.5; 6373 -0.7; 7010 -3.7; 7711 -8.5; 8482 -6.3; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.4; 16529 -8.5; 18182 -9.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N5005 Reference GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N5005 Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.28 | -3.1 dB |
| Peaking | 3224 Hz  | 1.61 | 8.0 dB  |
| Peaking | 3785 Hz  | 0.59 | -5.3 dB |
| Peaking | 5913 Hz  | 3.71 | 7.1 dB  |
| Peaking | 17618 Hz | 2.29 | -6.4 dB |
| Peaking | 956 Hz   | 1.33 | 4.0 dB  |
| Peaking | 1238 Hz  | 0.52 | -2.7 dB |
| Peaking | 2559 Hz  | 2.81 | 1.7 dB  |
| Peaking | 7890 Hz  | 5.98 | -5.8 dB |
| Peaking | 8508 Hz  | 0.98 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AKG%20N5005%20Reference/AKG%20N5005%20Reference.png)