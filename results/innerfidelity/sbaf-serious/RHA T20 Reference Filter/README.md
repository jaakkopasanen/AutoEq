# RHA T20 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.5; 25 -9.8; 28 -10.0; 31 -10.1; 34 -10.2; 37 -10.3; 41 -10.3; 45 -10.4; 49 -10.4; 54 -10.4; 60 -10.4; 66 -10.5; 72 -10.5; 79 -10.5; 87 -10.5; 96 -10.5; 106 -10.4; 116 -10.2; 128 -10.0; 141 -9.7; 155 -9.5; 170 -9.2; 187 -8.8; 206 -8.4; 227 -7.9; 249 -7.5; 274 -7.0; 302 -6.5; 332 -6.0; 365 -5.5; 402 -5.1; 442 -4.6; 486 -4.4; 535 -4.0; 588 -3.4; 647 -3.2; 712 -3.2; 783 -3.0; 861 -3.3; 947 -3.8; 1042 -4.4; 1146 -5.0; 1261 -5.9; 1387 -7.4; 1526 -8.5; 1678 -7.5; 1846 -4.4; 2031 -6.7; 2234 -7.6; 2457 -8.6; 2703 -9.0; 2973 -7.8; 3270 -6.4; 3597 -6.2; 3957 -8.1; 4353 -12.5; 4788 -13.0; 5267 -7.0; 5793 -1.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.52 | -4.4 dB |
| Peaking | 124 Hz  | 1.22 | -3.0 dB |
| Peaking | 2582 Hz | 4.56 | -3.2 dB |
| Peaking | 4637 Hz | 4.95 | -9.4 dB |
| Peaking | 6141 Hz | 4.12 | 7.2 dB  |
| Peaking | 227 Hz  | 1.67 | -1.1 dB |
| Peaking | 763 Hz  | 0.75 | 3.4 dB  |
| Peaking | 1573 Hz | 2.21 | -4.1 dB |
| Peaking | 1843 Hz | 8.19 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Reference%20Filter/RHA%20T20%20Reference%20Filter.png)