# Fischer Audio FA-005
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -2.4; 25 -4.0; 28 -6.2; 31 -8.0; 34 -9.5; 37 -10.7; 41 -12.0; 45 -12.8; 49 -13.3; 54 -13.4; 60 -13.1; 66 -12.9; 72 -12.8; 79 -12.8; 87 -12.8; 96 -12.8; 106 -12.5; 116 -12.4; 128 -12.1; 141 -11.9; 155 -11.9; 170 -11.9; 187 -11.7; 206 -11.4; 227 -10.9; 249 -10.4; 274 -9.8; 302 -9.1; 332 -8.7; 365 -8.3; 402 -7.9; 442 -7.6; 486 -7.1; 535 -6.5; 588 -5.5; 647 -4.2; 712 -3.1; 783 -2.7; 861 -2.4; 947 -3.0; 1042 -4.7; 1146 -6.4; 1261 -7.6; 1387 -8.2; 1526 -8.3; 1678 -8.3; 1846 -8.3; 2031 -8.0; 2234 -7.7; 2457 -7.4; 2703 -6.7; 2973 -5.9; 3270 -5.0; 3597 -4.3; 3957 -3.6; 4353 -2.5; 4788 -0.8; 5267 -0.7; 5793 -0.7; 6373 -1.4; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-005 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-005 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.28 | 9.1 dB  |
| Peaking | 46 Hz   | 0.85 | -6.0 dB |
| Peaking | 141 Hz  | 0.54 | -4.7 dB |
| Peaking | 783 Hz  | 2.57 | 5.3 dB  |
| Peaking | 5288 Hz | 2.15 | 6.9 dB  |
| Peaking | 965 Hz  | 4.99 | 2.2 dB  |
| Peaking | 1693 Hz | 1.18 | -2.3 dB |
| Peaking | 3982 Hz | 1.56 | 2.0 dB  |
| Peaking | 6290 Hz | 1.35 | -3.0 dB |
| Peaking | 6385 Hz | 4.34 | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20FA-005/Fischer%20Audio%20FA-005.png)