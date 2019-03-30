# AKG K520
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -2.9; 31 -3.5; 34 -4.0; 37 -4.5; 41 -4.9; 45 -5.2; 49 -5.5; 54 -5.7; 60 -5.9; 66 -6.1; 72 -6.2; 79 -6.3; 87 -6.5; 96 -6.7; 106 -6.6; 116 -6.6; 128 -6.7; 141 -6.4; 155 -6.3; 170 -6.0; 187 -5.7; 206 -5.3; 227 -4.9; 249 -4.5; 274 -4.3; 302 -4.0; 332 -3.7; 365 -3.7; 402 -3.5; 442 -3.2; 486 -3.0; 535 -2.8; 588 -2.7; 647 -2.7; 712 -2.8; 783 -2.7; 861 -2.7; 947 -2.7; 1042 -2.8; 1146 -3.1; 1261 -3.4; 1387 -3.8; 1526 -4.2; 1678 -4.7; 1846 -5.5; 2031 -6.2; 2234 -6.6; 2457 -6.5; 2703 -5.6; 2973 -4.3; 3270 -3.1; 3597 -2.1; 3957 -1.0; 4353 -0.5; 4788 -2.0; 5267 -5.0; 5793 -6.3; 6373 -6.2; 7010 -6.6; 7711 -7.0; 8482 -6.5; 9330 -6.3; 10263 -7.0; 11289 -7.6; 12418 -7.6; 13660 -6.4; 15026 -4.5; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.18 | 4.2 dB  |
| Peaking | 97 Hz    | 1.03 | -2.5 dB |
| Peaking | 4272 Hz  | 2.15 | 8.8 dB  |
| Peaking | 5006 Hz  | 0.82 | -4.8 dB |
| Peaking | 11866 Hz | 2.19 | -2.9 dB |
| Peaking | 21 Hz    | 1.77 | 0.5 dB  |
| Peaking | 171 Hz   | 2.05 | -0.9 dB |
| Peaking | 886 Hz   | 0.47 | 2.2 dB  |
| Peaking | 2300 Hz  | 1.47 | -3.0 dB |
| Peaking | 3099 Hz  | 3.73 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K520/AKG%20K520.png)