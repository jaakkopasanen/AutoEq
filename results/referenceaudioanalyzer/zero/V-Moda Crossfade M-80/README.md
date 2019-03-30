# V-Moda Crossfade M-80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.8; 25 -4.9; 28 -5.1; 31 -5.3; 34 -5.5; 37 -5.6; 41 -5.7; 45 -5.7; 49 -5.7; 54 -5.7; 60 -5.8; 66 -6.0; 72 -5.8; 79 -5.7; 87 -5.7; 96 -5.7; 106 -5.7; 116 -5.7; 128 -5.7; 141 -5.3; 155 -4.4; 170 -3.1; 187 -2.4; 206 -2.8; 227 -3.1; 249 -3.4; 274 -3.7; 302 -3.7; 332 -3.3; 365 -2.9; 402 -2.3; 442 -1.6; 486 -0.8; 535 -0.5; 588 -0.5; 647 -0.9; 712 -1.5; 783 -2.3; 861 -3.2; 947 -4.1; 1042 -5.2; 1146 -6.1; 1261 -6.8; 1387 -7.0; 1526 -6.8; 1678 -6.2; 1846 -5.3; 2031 -4.2; 2234 -3.2; 2457 -2.8; 2703 -2.9; 2973 -3.7; 3270 -5.0; 3597 -6.6; 3957 -8.1; 4353 -9.9; 4788 -11.5; 5267 -11.1; 5793 -9.2; 6373 -6.5; 7010 -3.2; 7711 -3.7; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 94 Hz   | 0.31 | -2.1 dB |
| Peaking | 191 Hz  | 2.56 | 3.0 dB  |
| Peaking | 558 Hz  | 1.23 | 4.2 dB  |
| Peaking | 1313 Hz | 2.4  | -3.9 dB |
| Peaking | 4906 Hz | 2.89 | -8.4 dB |
| Peaking | 1730 Hz | 3.32 | -1.5 dB |
| Peaking | 2522 Hz | 1.82 | 2.2 dB  |
| Peaking | 3790 Hz | 4.08 | -1.7 dB |
| Peaking | 5944 Hz | 5.47 | -1.9 dB |
| Peaking | 7127 Hz | 4.1  | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/V-Moda%20Crossfade%20M-80/V-Moda%20Crossfade%20M-80.png)