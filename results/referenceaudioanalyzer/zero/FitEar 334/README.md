# FitEar 334
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.3; 25 -11.5; 28 -11.8; 31 -12.0; 34 -12.2; 37 -12.3; 41 -12.4; 45 -12.4; 49 -12.4; 54 -12.4; 60 -12.4; 66 -12.4; 72 -12.4; 79 -12.4; 87 -12.2; 96 -12.0; 106 -12.0; 116 -11.8; 128 -11.7; 141 -11.4; 155 -11.2; 170 -10.9; 187 -10.7; 206 -10.4; 227 -10.1; 249 -9.8; 274 -9.4; 302 -9.0; 332 -8.6; 365 -8.2; 402 -7.8; 442 -7.3; 486 -6.8; 535 -6.3; 588 -5.9; 647 -5.4; 712 -4.8; 783 -4.3; 861 -3.8; 947 -3.3; 1042 -2.8; 1146 -2.4; 1261 -2.3; 1387 -2.3; 1526 -2.3; 1678 -2.4; 1846 -3.0; 2031 -3.9; 2234 -4.5; 2457 -4.5; 2703 -3.7; 2973 -2.7; 3270 -2.0; 3597 -1.2; 3957 -0.5; 4353 -0.8; 4788 -2.0; 5267 -3.4; 5793 -3.6; 6373 -2.7; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar 334 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar 334 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.45 | -4.5 dB |
| Peaking | 121 Hz   | 0.35 | -5.4 dB |
| Peaking | 1190 Hz  | 1.05 | 3.6 dB  |
| Peaking | 4115 Hz  | 1.65 | 4.7 dB  |
| Peaking | 22050 Hz | 2.28 | 0.7 dB  |
| Peaking | 1688 Hz  | 5.35 | 0.8 dB  |
| Peaking | 2308 Hz  | 5.37 | -1.2 dB |
| Peaking | 5324 Hz  | 5.9  | -0.8 dB |
| Peaking | 6730 Hz  | 5.12 | 3.0 dB  |
| Peaking | 7711 Hz  | 2.38 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/FitEar%20334/FitEar%20334.png)