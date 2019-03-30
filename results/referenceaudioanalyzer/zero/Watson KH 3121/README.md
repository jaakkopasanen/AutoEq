# Watson KH 3121
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -8.1; 25 -8.7; 28 -9.4; 31 -10.0; 34 -10.5; 37 -10.9; 41 -11.4; 45 -11.8; 49 -12.2; 54 -12.5; 60 -12.9; 66 -13.2; 72 -13.5; 79 -13.8; 87 -14.0; 96 -14.2; 106 -14.4; 116 -14.6; 128 -14.8; 141 -15.0; 155 -15.2; 170 -15.4; 187 -15.6; 206 -15.8; 227 -16.0; 249 -16.1; 274 -16.4; 302 -16.5; 332 -16.2; 365 -15.8; 402 -15.0; 442 -13.7; 486 -12.1; 535 -10.1; 588 -7.8; 647 -5.4; 712 -3.1; 783 -1.6; 861 -0.9; 947 -1.1; 1042 -2.2; 1146 -3.6; 1261 -5.4; 1387 -7.4; 1526 -9.6; 1678 -11.1; 1846 -11.1; 2031 -9.6; 2234 -6.8; 2457 -3.8; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Watson KH 3121 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Watson KH 3121 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 106 Hz  | 0.33 | -6.9 dB |
| Peaking | 380 Hz  | 0.73 | -8.2 dB |
| Peaking | 832 Hz  | 1.12 | 10.2 dB |
| Peaking | 1776 Hz | 1.84 | -9.9 dB |
| Peaking | 3513 Hz | 0.79 | 7.8 dB  |
| Peaking | 20 Hz   | 2.12 | 1.3 dB  |
| Peaking | 2784 Hz | 4.78 | 2.2 dB  |
| Peaking | 3416 Hz | 1.41 | -1.3 dB |
| Peaking | 6251 Hz | 2.17 | 5.3 dB  |
| Peaking | 7463 Hz | 1.49 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -9.6 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 9.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Watson%20KH%203121/Watson%20KH%203121.png)