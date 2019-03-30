# AKG N20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.6; 25 -8.0; 28 -8.5; 31 -8.8; 34 -9.1; 37 -9.3; 41 -9.6; 45 -9.8; 49 -9.9; 54 -9.9; 60 -9.9; 66 -9.9; 72 -9.9; 79 -9.8; 87 -9.6; 96 -9.6; 106 -9.4; 116 -9.2; 128 -9.0; 141 -8.7; 155 -8.4; 170 -8.1; 187 -7.6; 206 -7.1; 227 -6.4; 249 -6.0; 274 -5.8; 302 -5.6; 332 -5.3; 365 -4.8; 402 -4.2; 442 -3.7; 486 -3.2; 535 -2.7; 588 -2.3; 647 -1.9; 712 -1.6; 783 -1.4; 861 -1.0; 947 -0.6; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.9; 1526 -1.5; 1678 -2.4; 1846 -3.5; 2031 -4.9; 2234 -6.7; 2457 -8.1; 2703 -8.5; 2973 -7.4; 3270 -5.7; 3597 -4.5; 3957 -3.8; 4353 -3.8; 4788 -4.7; 5267 -7.0; 5793 -8.9; 6373 -8.1; 7010 -3.4; 7711 -3.9; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 59 Hz   |  0.4  | -2.7 dB |
| Peaking | 130 Hz  |  0.16 | -3.5 dB |
| Peaking | 1333 Hz |  0.29 | 6.0 dB  |
| Peaking | 2551 Hz |  1.6  | -9.1 dB |
| Peaking | 5859 Hz |  3.8  | -6.6 dB |
| Peaking | 350 Hz  |  6.17 | -0.2 dB |
| Peaking | 7154 Hz | 11.86 | 2.2 dB  |
| Peaking | 9224 Hz |  0.89 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20N20/AKG%20N20.png)