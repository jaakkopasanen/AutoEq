# TFZ 1S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.5; 25 -12.6; 28 -12.6; 31 -12.7; 34 -12.7; 37 -12.6; 41 -12.6; 45 -12.6; 49 -12.7; 54 -12.6; 60 -12.5; 66 -12.3; 72 -12.2; 79 -12.0; 87 -11.9; 96 -11.7; 106 -11.6; 116 -11.3; 128 -11.1; 141 -10.8; 155 -10.5; 170 -10.1; 187 -9.8; 206 -9.4; 227 -9.1; 249 -9.0; 274 -8.6; 302 -8.2; 332 -7.8; 365 -7.5; 402 -7.2; 442 -6.9; 486 -6.5; 535 -6.2; 588 -6.0; 647 -5.8; 712 -5.8; 783 -5.8; 861 -6.0; 947 -6.6; 1042 -7.2; 1146 -7.9; 1261 -8.6; 1387 -9.4; 1526 -10.2; 1678 -10.9; 1846 -11.2; 2031 -10.9; 2234 -9.9; 2457 -8.6; 2703 -7.3; 2973 -6.4; 3270 -6.1; 3597 -6.4; 3957 -6.4; 4353 -5.6; 4788 -3.7; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 1S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.18 | -6.2 dB |
| Peaking | 845 Hz  | 0.78 | 3.3 dB  |
| Peaking | 2008 Hz | 0.67 | -7.0 dB |
| Peaking | 2887 Hz | 1.83 | 4.5 dB  |
| Peaking | 5737 Hz | 2.57 | 7.8 dB  |
| Peaking | 1843 Hz | 7.38 | -0.3 dB |
| Peaking | 6582 Hz | 8.77 | 1.6 dB  |
| Peaking | 7686 Hz | 3.42 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/TFZ%201S/TFZ%201S.png)