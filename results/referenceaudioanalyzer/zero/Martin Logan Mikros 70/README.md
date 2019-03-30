# Martin Logan Mikros 70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.4; 25 -8.9; 28 -9.4; 31 -9.8; 34 -10.0; 37 -10.2; 41 -10.4; 45 -10.6; 49 -10.8; 54 -10.9; 60 -11.0; 66 -10.9; 72 -10.9; 79 -10.9; 87 -10.9; 96 -10.9; 106 -10.9; 116 -10.6; 128 -10.6; 141 -10.4; 155 -10.2; 170 -9.9; 187 -9.7; 206 -9.5; 227 -9.1; 249 -8.9; 274 -9.0; 302 -8.7; 332 -8.6; 365 -8.2; 402 -7.8; 442 -7.3; 486 -6.9; 535 -6.4; 588 -6.0; 647 -5.5; 712 -5.2; 783 -4.8; 861 -4.4; 947 -4.1; 1042 -3.8; 1146 -3.4; 1261 -2.9; 1387 -2.5; 1526 -2.2; 1678 -2.6; 1846 -3.2; 2031 -3.8; 2234 -4.2; 2457 -4.3; 2703 -4.0; 2973 -3.4; 3270 -2.5; 3597 -1.9; 3957 -1.4; 4353 -0.7; 4788 -0.5; 5267 -1.1; 5793 -2.3; 6373 -3.1; 7010 -3.1; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Martin Logan Mikros 70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Martin Logan Mikros 70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 3 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 80 Hz   | 0.24 | -5.6 dB |
| Peaking | 1343 Hz | 1.18 | 3.0 dB  |
| Peaking | 4601 Hz | 1.68 | 4.9 dB  |
| Peaking | 14 Hz   | 1.53 | 1.0 dB  |
| Peaking | 712 Hz  | 4.5  | 0.4 dB  |
| Peaking | 2418 Hz | 2.78 | -1.6 dB |
| Peaking | 2549 Hz | 1.44 | 1.0 dB  |
| Peaking | 8737 Hz | 3.5  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Martin%20Logan%20Mikros%2070/Martin%20Logan%20Mikros%2070.png)