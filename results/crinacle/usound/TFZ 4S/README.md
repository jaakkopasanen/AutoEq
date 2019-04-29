# TFZ 4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.9; 25 -6.9; 28 -7.0; 31 -6.9; 34 -6.9; 37 -6.8; 41 -6.8; 45 -6.7; 49 -6.6; 54 -6.6; 60 -6.5; 66 -6.5; 72 -6.6; 79 -6.6; 87 -6.7; 96 -6.8; 106 -6.9; 116 -6.9; 128 -6.9; 141 -6.9; 155 -6.9; 170 -6.8; 187 -6.6; 206 -6.5; 227 -6.3; 249 -6.1; 274 -6.0; 302 -5.8; 332 -5.6; 365 -5.5; 402 -5.3; 442 -5.3; 486 -5.2; 535 -5.0; 588 -5.0; 647 -5.0; 712 -4.9; 783 -4.8; 861 -4.8; 947 -5.1; 1042 -5.8; 1146 -6.8; 1261 -8.1; 1387 -9.2; 1526 -10.0; 1678 -10.7; 1846 -11.2; 2031 -11.4; 2234 -10.6; 2457 -8.7; 2703 -6.8; 2973 -5.5; 3270 -5.0; 3597 -5.4; 3957 -6.7; 4353 -6.9; 4788 -5.7; 5267 -2.6; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -8.9; 8482 -9.6; 9330 -6.6; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 951 Hz   | 0.77 | 5.5 dB  |
| Peaking | 1989 Hz  | 0.57 | -8.8 dB |
| Peaking | 2986 Hz  | 2.07 | 6.7 dB  |
| Peaking | 6087 Hz  | 2.44 | 8.4 dB  |
| Peaking | 8102 Hz  | 4.96 | -5.3 dB |
| Peaking | 77 Hz    | 0.15 | -0.5 dB |
| Peaking | 374 Hz   | 1.38 | 0.8 dB  |
| Peaking | 9967 Hz  | 4.03 | 0.4 dB  |
| Peaking | 13188 Hz | 1.93 | 0.1 dB  |
| Peaking | 22050 Hz | 1.84 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%204S/TFZ%204S.png)