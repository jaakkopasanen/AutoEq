# Focal Clear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.1; 25 -1.3; 28 -1.7; 31 -1.9; 34 -2.2; 37 -2.4; 41 -2.6; 45 -2.8; 49 -3.0; 54 -3.2; 60 -3.5; 66 -3.8; 72 -4.0; 79 -4.3; 87 -4.7; 96 -5.0; 106 -5.3; 116 -5.6; 128 -5.9; 141 -6.0; 155 -6.1; 170 -6.1; 187 -6.1; 206 -6.1; 227 -6.0; 249 -5.9; 274 -5.6; 302 -5.4; 332 -5.1; 365 -4.9; 402 -4.8; 442 -4.7; 486 -4.7; 535 -4.6; 588 -4.6; 647 -4.7; 712 -5.0; 783 -5.3; 861 -5.8; 947 -6.3; 1042 -6.9; 1146 -7.5; 1261 -7.9; 1387 -8.0; 1526 -7.3; 1678 -6.3; 1846 -5.4; 2031 -4.5; 2234 -3.7; 2457 -4.1; 2703 -4.7; 2973 -5.4; 3270 -5.2; 3597 -5.0; 3957 -2.0; 4353 -0.5; 4788 -1.7; 5267 -2.3; 5793 -4.3; 6373 -1.9; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -5.2; 12418 -7.9; 13660 -5.2; 15026 -4.8; 16529 -8.3; 18182 -11.6; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Clear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.09 | 3.7 dB  |
| Peaking | 1273 Hz  | 2.1  | -3.5 dB |
| Peaking | 4423 Hz  | 4.28 | 4.5 dB  |
| Peaking | 6701 Hz  | 7.46 | 4.0 dB  |
| Peaking | 19285 Hz | 0.8  | -8.5 dB |
| Peaking | 174 Hz   | 1.27 | -1.7 dB |
| Peaking | 2247 Hz  | 5.05 | 1.5 dB  |
| Peaking | 3251 Hz  | 4.54 | -1.3 dB |
| Peaking | 12411 Hz | 6.5  | -3.0 dB |
| Peaking | 14717 Hz | 3.41 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Clear/Focal%20Clear.png)