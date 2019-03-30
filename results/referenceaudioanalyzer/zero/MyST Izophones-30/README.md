# MyST Izophones-30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.9; 25 -5.6; 28 -6.4; 31 -6.9; 34 -7.3; 37 -7.5; 41 -7.5; 45 -7.5; 49 -7.3; 54 -7.0; 60 -6.8; 66 -7.0; 72 -7.3; 79 -7.5; 87 -7.5; 96 -7.2; 106 -6.9; 116 -6.6; 128 -6.4; 141 -6.0; 155 -5.9; 170 -5.6; 187 -5.4; 206 -5.2; 227 -5.0; 249 -4.9; 274 -4.7; 302 -4.3; 332 -4.2; 365 -4.3; 402 -4.2; 442 -3.9; 486 -4.1; 535 -4.3; 588 -4.2; 647 -3.9; 712 -4.1; 783 -4.2; 861 -4.4; 947 -4.6; 1042 -4.9; 1146 -4.9; 1261 -4.8; 1387 -4.6; 1526 -4.6; 1678 -4.4; 1846 -3.4; 2031 -2.4; 2234 -1.9; 2457 -1.2; 2703 -0.5; 2973 -0.8; 3270 -2.5; 3597 -6.2; 3957 -9.8; 4353 -10.7; 4788 -8.9; 5267 -7.6; 5793 -9.7; 6373 -12.0; 7010 -11.5; 7711 -8.0; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -7.0; 12418 -8.4; 13660 -7.6; 15026 -5.9; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MyST Izophones-30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST Izophones-30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.76 | -2.4 dB |
| Peaking | 2933 Hz  | 1.43 | 6.6 dB  |
| Peaking | 3737 Hz  | 2.04 | -1.0 dB |
| Peaking | 4114 Hz  | 2.86 | -7.3 dB |
| Peaking | 6608 Hz  | 3.5  | -7.4 dB |
| Peaking | 60 Hz    | 2.27 | 2.6 dB  |
| Peaking | 62 Hz    | 0.98 | -1.7 dB |
| Peaking | 420 Hz   | 0.9  | 1.3 dB  |
| Peaking | 9256 Hz  | 2.9  | 1.6 dB  |
| Peaking | 12637 Hz | 2.43 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MyST%20Izophones-30/MyST%20Izophones-30.png)