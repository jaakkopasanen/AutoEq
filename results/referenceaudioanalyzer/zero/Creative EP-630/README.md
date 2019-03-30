# Creative EP-630
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.2; 25 -13.4; 28 -13.6; 31 -13.8; 34 -14.0; 37 -14.1; 41 -14.1; 45 -14.1; 49 -14.1; 54 -14.1; 60 -14.1; 66 -14.1; 72 -14.1; 79 -14.1; 87 -14.1; 96 -14.0; 106 -13.8; 116 -13.8; 128 -13.5; 141 -13.4; 155 -13.1; 170 -12.8; 187 -12.5; 206 -12.2; 227 -11.8; 249 -11.4; 274 -11.0; 302 -10.5; 332 -10.0; 365 -9.4; 402 -8.8; 442 -8.2; 486 -7.6; 535 -7.2; 588 -6.9; 647 -6.3; 712 -5.6; 783 -4.9; 861 -4.3; 947 -3.6; 1042 -3.1; 1146 -2.5; 1261 -1.8; 1387 -1.3; 1526 -0.9; 1678 -0.7; 1846 -0.5; 2031 -0.5; 2234 -0.9; 2457 -1.5; 2703 -2.2; 2973 -2.7; 3270 -3.2; 3597 -3.5; 3957 -3.9; 4353 -4.3; 4788 -4.4; 5267 -4.2; 5793 -5.2; 6373 -9.4; 7010 -11.7; 7711 -9.2; 8482 -6.3; 9330 -6.3; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative EP-630 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative EP-630 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.42 | -5.5 dB |
| Peaking | 130 Hz  | 0.36 | -6.3 dB |
| Peaking | 1740 Hz | 0.66 | 6.1 dB  |
| Peaking | 5543 Hz | 2.98 | 1.9 dB  |
| Peaking | 6906 Hz | 4.12 | -7.2 dB |
| Peaking | 479 Hz  | 7.31 | 0.3 dB  |
| Peaking | 3060 Hz | 3.93 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20EP-630/Creative%20EP-630.png)