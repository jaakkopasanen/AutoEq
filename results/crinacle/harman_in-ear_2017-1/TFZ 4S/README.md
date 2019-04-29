# TFZ 4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.1; 25 -8.2; 28 -8.2; 31 -8.2; 34 -8.2; 37 -8.1; 41 -8.0; 45 -8.0; 49 -7.9; 54 -7.8; 60 -7.8; 66 -7.8; 72 -7.9; 79 -7.9; 87 -8.0; 96 -8.1; 106 -8.1; 116 -8.1; 128 -8.1; 141 -8.1; 155 -8.1; 170 -8.0; 187 -7.9; 206 -7.7; 227 -7.6; 249 -7.4; 274 -7.2; 302 -7.0; 332 -6.7; 365 -6.4; 402 -6.3; 442 -6.2; 486 -6.1; 535 -5.9; 588 -5.8; 647 -5.7; 712 -5.7; 783 -5.6; 861 -5.6; 947 -6.0; 1042 -6.7; 1146 -7.7; 1261 -8.7; 1387 -9.5; 1526 -10.1; 1678 -10.6; 1846 -11.1; 2031 -11.0; 2234 -9.5; 2457 -7.1; 2703 -4.9; 2973 -3.3; 3270 -2.9; 3597 -3.6; 3957 -5.2; 4353 -5.9; 4788 -5.0; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.4; 8482 -8.0; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -12.4; 16529 -19.0; 18182 -17.7; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 54 Hz    | 0.29 | -1.8 dB  |
| Peaking | 1867 Hz  | 1.98 | -5.6 dB  |
| Peaking | 3095 Hz  | 2.89 | 4.7 dB   |
| Peaking | 5948 Hz  | 3.26 | 6.9 dB   |
| Peaking | 18214 Hz | 0.9  | -13.5 dB |
| Peaking | 785 Hz   | 1.22 | 1.5 dB   |
| Peaking | 1307 Hz  | 3.46 | -1.5 dB  |
| Peaking | 8505 Hz  | 4.82 | -2.3 dB  |
| Peaking | 14249 Hz | 1.34 | 5.5 dB   |
| Peaking | 15849 Hz | 2.61 | -8.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -11.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%204S/TFZ%204S.png)