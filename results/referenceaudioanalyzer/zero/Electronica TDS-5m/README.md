# Electronica TDS-5m
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.4; 60 -2.2; 66 -2.9; 72 -3.4; 79 -3.9; 87 -4.3; 96 -4.5; 106 -4.8; 116 -4.9; 128 -4.9; 141 -5.0; 155 -5.2; 170 -5.2; 187 -5.2; 206 -5.5; 227 -5.6; 249 -5.9; 274 -5.9; 302 -5.9; 332 -6.1; 365 -6.2; 402 -6.2; 442 -5.9; 486 -5.9; 535 -5.9; 588 -5.9; 647 -6.0; 712 -6.2; 783 -6.3; 861 -6.6; 947 -6.8; 1042 -6.8; 1146 -6.3; 1261 -5.6; 1387 -5.2; 1526 -5.5; 1678 -6.2; 1846 -7.4; 2031 -8.8; 2234 -10.4; 2457 -12.1; 2703 -13.7; 2973 -14.4; 3270 -14.0; 3597 -12.7; 3957 -10.7; 4353 -8.8; 4788 -7.3; 5267 -6.1; 5793 -4.6; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Electronica TDS-5m GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Electronica TDS-5m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.54 | 6.5 dB  |
| Peaking | 307 Hz  | 0.47 | 0.4 dB  |
| Peaking | 1513 Hz | 2.54 | 2.6 dB  |
| Peaking | 3000 Hz | 1.59 | -8.6 dB |
| Peaking | 6307 Hz | 3.03 | 4.7 dB  |
| Peaking | 575 Hz  | 5.26 | 0.4 dB  |
| Peaking | 4816 Hz | 7.37 | 0.7 dB  |
| Peaking | 7898 Hz | 6.66 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Electronica%20TDS-5m/Electronica%20TDS-5m.png)