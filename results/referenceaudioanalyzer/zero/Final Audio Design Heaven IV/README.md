# Final Audio Design Heaven IV
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.5; 25 -8.7; 28 -8.8; 31 -8.9; 34 -9.0; 37 -9.0; 41 -8.9; 45 -8.9; 49 -8.9; 54 -9.0; 60 -8.9; 66 -8.7; 72 -8.6; 79 -8.4; 87 -8.3; 96 -8.0; 106 -7.8; 116 -7.6; 128 -7.4; 141 -7.1; 155 -6.8; 170 -6.5; 187 -6.3; 206 -6.0; 227 -6.0; 249 -5.9; 274 -5.5; 302 -5.0; 332 -4.6; 365 -4.2; 402 -3.9; 442 -3.5; 486 -3.1; 535 -2.8; 588 -2.5; 647 -2.1; 712 -1.8; 783 -1.5; 861 -1.2; 947 -1.0; 1042 -0.8; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.7; 1846 -1.1; 2031 -1.6; 2234 -2.1; 2457 -2.9; 2703 -5.1; 2973 -7.2; 3270 -6.7; 3597 -4.4; 3957 -2.3; 4353 -1.1; 4788 -0.9; 5267 -1.9; 5793 -3.2; 6373 -3.6; 7010 -2.7; 7711 -3.1; 8482 -3.4; 9330 -3.4; 10263 -3.4; 11289 -3.4; 12418 -3.4; 13660 -3.4; 15026 -3.4; 16529 -3.4; 18182 -3.4; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design Heaven IV GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design Heaven IV ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.2  | -5.4 dB |
| Peaking | 1310 Hz | 0.59 | 3.3 dB  |
| Peaking | 3067 Hz | 3.28 | -5.8 dB |
| Peaking | 4506 Hz | 3.6  | 2.8 dB  |
| Peaking | 47 Hz   | 0.71 | -0.3 dB |
| Peaking | 204 Hz  | 0.8  | 0.5 dB  |
| Peaking | 258 Hz  | 2.07 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20Heaven%20IV/Final%20Audio%20Design%20Heaven%20IV.png)