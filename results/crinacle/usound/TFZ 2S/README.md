# TFZ 2S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.2; 25 -10.2; 28 -10.1; 31 -9.9; 34 -9.7; 37 -9.5; 41 -9.3; 45 -9.1; 49 -8.9; 54 -8.7; 60 -8.5; 66 -8.4; 72 -8.2; 79 -8.1; 87 -8.0; 96 -7.9; 106 -7.9; 116 -7.7; 128 -7.6; 141 -7.5; 155 -7.3; 170 -7.1; 187 -6.8; 206 -6.5; 227 -6.2; 249 -5.9; 274 -5.6; 302 -5.4; 332 -5.1; 365 -4.8; 402 -4.6; 442 -4.4; 486 -4.3; 535 -4.1; 588 -3.9; 647 -3.8; 712 -3.7; 783 -3.4; 861 -3.6; 947 -3.8; 1042 -4.4; 1146 -5.4; 1261 -6.5; 1387 -7.4; 1526 -8.0; 1678 -8.5; 1846 -8.8; 2031 -8.4; 2234 -8.6; 2457 -7.7; 2703 -6.3; 2973 -5.2; 3270 -4.7; 3597 -5.2; 3957 -6.7; 4353 -8.1; 4788 -6.8; 5267 -3.5; 5793 -1.0; 6373 -0.5; 7010 -3.8; 7711 -9.2; 8482 -8.5; 9330 -5.9; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -7.0; 18182 -7.9; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 2S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 2S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.5  | -4.4 dB |
| Peaking | 113 Hz   | 1.65 | -1.3 dB |
| Peaking | 1917 Hz  | 2.72 | -3.4 dB |
| Peaking | 6251 Hz  | 4.17 | 6.8 dB  |
| Peaking | 7923 Hz  | 5.12 | -5.2 dB |
| Peaking | 869 Hz   | 0.82 | 3.4 dB  |
| Peaking | 1395 Hz  | 1.32 | -2.7 dB |
| Peaking | 4241 Hz  | 1.6  | 2.7 dB  |
| Peaking | 4380 Hz  | 4.05 | -5.7 dB |
| Peaking | 18535 Hz | 1.22 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%202S/TFZ%202S.png)