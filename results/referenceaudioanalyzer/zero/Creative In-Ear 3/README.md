# Creative In-Ear 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.8; 25 -3.3; 28 -4.0; 31 -4.5; 34 -4.9; 37 -5.2; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.3; 60 -6.5; 66 -6.7; 72 -6.7; 79 -6.9; 87 -7.0; 96 -7.0; 106 -7.0; 116 -7.0; 128 -7.0; 141 -6.7; 155 -6.6; 170 -6.4; 187 -6.4; 206 -6.7; 227 -7.2; 249 -7.3; 274 -7.0; 302 -6.6; 332 -6.2; 365 -5.7; 402 -5.2; 442 -4.9; 486 -4.6; 535 -4.2; 588 -3.7; 647 -3.3; 712 -2.8; 783 -2.4; 861 -2.1; 947 -1.8; 1042 -1.5; 1146 -1.5; 1261 -1.5; 1387 -1.8; 1526 -2.1; 1678 -2.7; 1846 -3.3; 2031 -3.8; 2234 -3.9; 2457 -3.4; 2703 -2.5; 2973 -1.4; 3270 -0.6; 3597 -0.5; 3957 -0.8; 4353 -1.4; 4788 -1.8; 5267 -2.0; 5793 -2.6; 6373 -3.2; 7010 -2.4; 7711 -2.8; 8482 -3.1; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -3.1; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative In-Ear 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative In-Ear 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 1.3  | -1.9 dB |
| Peaking | 99 Hz   | 0.9  | -3.1 dB |
| Peaking | 268 Hz  | 1.03 | -3.4 dB |
| Peaking | 1054 Hz | 1.87 | 2.0 dB  |
| Peaking | 3713 Hz | 2.51 | 2.8 dB  |
| Peaking | 1494 Hz | 2.79 | 0.9 dB  |
| Peaking | 2199 Hz | 1.75 | -1.5 dB |
| Peaking | 2983 Hz | 4.48 | 1.2 dB  |
| Peaking | 5175 Hz | 6    | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20In-Ear%203/Creative%20In-Ear%203.png)