# MyST Izophones-30s
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -4.8; 28 -5.1; 31 -5.2; 34 -5.3; 37 -5.4; 41 -5.5; 45 -5.6; 49 -5.7; 54 -5.7; 60 -5.5; 66 -5.3; 72 -5.1; 79 -5.0; 87 -4.8; 96 -4.5; 106 -4.4; 116 -4.3; 128 -4.1; 141 -4.0; 155 -3.7; 170 -3.5; 187 -3.4; 206 -3.4; 227 -3.3; 249 -3.0; 274 -2.8; 302 -2.6; 332 -2.4; 365 -2.4; 402 -2.4; 442 -2.3; 486 -2.1; 535 -2.1; 588 -2.1; 647 -2.1; 712 -2.1; 783 -2.3; 861 -2.5; 947 -2.7; 1042 -3.0; 1146 -3.4; 1261 -3.7; 1387 -4.1; 1526 -4.4; 1678 -4.1; 1846 -2.9; 2031 -1.9; 2234 -1.3; 2457 -0.7; 2703 -0.5; 2973 -1.2; 3270 -2.4; 3597 -5.1; 3957 -7.7; 4353 -8.7; 4788 -7.3; 5267 -5.2; 5793 -6.1; 6373 -8.4; 7010 -8.9; 7711 -6.2; 8482 -3.5; 9330 -3.5; 10263 -3.5; 11289 -3.5; 12418 -4.2; 13660 -3.6; 15026 -3.5; 16529 -3.5; 18182 -3.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MyST Izophones-30s GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST Izophones-30s ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.67 | -2.2 dB |
| Peaking | 489 Hz  | 0.95 | 1.5 dB  |
| Peaking | 2727 Hz | 2.52 | 3.9 dB  |
| Peaking | 4236 Hz | 3.29 | -5.8 dB |
| Peaking | 6786 Hz | 4.4  | -5.9 dB |
| Peaking | 831 Hz  | 2.36 | 0.5 dB  |
| Peaking | 1598 Hz | 2.08 | -1.7 dB |
| Peaking | 2029 Hz | 3.43 | 1.4 dB  |
| Peaking | 8593 Hz | 7.3  | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MyST%20Izophones-30s/MyST%20Izophones-30s.png)