# Sony XBA-Z5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.0; 31 -10.1; 34 -10.2; 37 -10.3; 41 -10.4; 45 -10.4; 49 -10.4; 54 -10.4; 60 -10.4; 66 -10.2; 72 -10.1; 79 -10.1; 87 -10.0; 96 -9.7; 106 -9.8; 116 -9.7; 128 -9.5; 141 -9.2; 155 -9.0; 170 -8.8; 187 -8.6; 206 -8.2; 227 -8.0; 249 -7.7; 274 -7.4; 302 -7.0; 332 -6.7; 365 -6.5; 402 -6.5; 442 -6.5; 486 -6.2; 535 -5.9; 588 -5.7; 647 -5.5; 712 -5.5; 783 -5.5; 861 -5.5; 947 -5.5; 1042 -5.5; 1146 -5.5; 1261 -5.4; 1387 -5.2; 1526 -5.0; 1678 -4.4; 1846 -3.9; 2031 -5.2; 2234 -6.8; 2457 -7.4; 2703 -7.6; 2973 -7.8; 3270 -7.3; 3597 -7.1; 3957 -7.9; 4353 -8.8; 4788 -8.7; 5267 -7.1; 5793 -4.0; 6373 -0.5; 7010 -3.2; 7711 -5.5; 8482 -5.7; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-Z5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.35 | -4.6 dB |
| Peaking | 152 Hz  | 0.92 | -1.6 dB |
| Peaking | 2798 Hz | 4.54 | -2.0 dB |
| Peaking | 4607 Hz | 2.68 | -3.7 dB |
| Peaking | 6370 Hz | 5.11 | 6.3 dB  |
| Peaking | 251 Hz  | 3.12 | -0.2 dB |
| Peaking | 728 Hz  | 1.79 | 0.5 dB  |
| Peaking | 1855 Hz | 2.79 | 2.4 dB  |
| Peaking | 2251 Hz | 4.45 | -1.8 dB |
| Peaking | 3309 Hz | 3.73 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-Z5/Sony%20XBA-Z5.png)