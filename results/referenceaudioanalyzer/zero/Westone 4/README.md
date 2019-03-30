# Westone 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.9; 25 -4.7; 28 -5.6; 31 -6.3; 34 -6.9; 37 -7.4; 41 -7.9; 45 -8.4; 49 -8.7; 54 -9.1; 60 -9.4; 66 -9.7; 72 -9.9; 79 -10.1; 87 -10.2; 96 -10.4; 106 -10.5; 116 -10.6; 128 -10.9; 141 -10.9; 155 -10.9; 170 -10.9; 187 -10.9; 206 -10.9; 227 -10.9; 249 -10.9; 274 -10.7; 302 -10.5; 332 -10.3; 365 -10.2; 402 -9.9; 442 -9.6; 486 -9.2; 535 -8.9; 588 -8.5; 647 -8.0; 712 -7.6; 783 -7.3; 861 -7.3; 947 -7.3; 1042 -7.3; 1146 -7.0; 1261 -6.9; 1387 -6.5; 1526 -6.0; 1678 -5.4; 1846 -4.9; 2031 -4.4; 2234 -4.1; 2457 -4.2; 2703 -4.6; 2973 -5.2; 3270 -5.9; 3597 -5.6; 3957 -4.0; 4353 -2.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.23 | 4.6 dB  |
| Peaking | 88 Hz   | 0.44 | -3.3 dB |
| Peaking | 292 Hz  | 0.6  | -3.0 dB |
| Peaking | 2163 Hz | 2.4  | 2.4 dB  |
| Peaking | 5335 Hz | 2.16 | 6.9 dB  |
| Peaking | 3571 Hz | 3.49 | -2.7 dB |
| Peaking | 4250 Hz | 1.55 | 3.4 dB  |
| Peaking | 6089 Hz | 1.37 | -4.2 dB |
| Peaking | 6405 Hz | 4.42 | 4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%204/Westone%204.png)