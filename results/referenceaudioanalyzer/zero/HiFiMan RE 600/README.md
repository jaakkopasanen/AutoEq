# HiFiMan RE 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.8; 25 -2.8; 28 -2.8; 31 -2.8; 34 -2.8; 37 -2.8; 41 -2.9; 45 -3.0; 49 -3.1; 54 -3.1; 60 -3.1; 66 -3.1; 72 -3.1; 79 -3.0; 87 -2.8; 96 -2.8; 106 -2.8; 116 -2.8; 128 -2.8; 141 -2.8; 155 -2.8; 170 -2.8; 187 -2.8; 206 -2.8; 227 -2.5; 249 -2.4; 274 -2.4; 302 -2.4; 332 -2.4; 365 -2.4; 402 -2.4; 442 -2.5; 486 -2.3; 535 -2.1; 588 -1.9; 647 -1.8; 712 -1.6; 783 -1.5; 861 -1.5; 947 -1.5; 1042 -1.5; 1146 -1.6; 1261 -1.9; 1387 -2.2; 1526 -2.8; 1678 -3.5; 1846 -4.6; 2031 -5.9; 2234 -7.1; 2457 -7.8; 2703 -7.5; 2973 -6.4; 3270 -4.6; 3597 -2.8; 3957 -1.8; 4353 -1.9; 4788 -2.2; 5267 -2.6; 5793 -3.3; 6373 -2.8; 7010 -0.5; 7711 -2.0; 8482 -2.3; 9330 -2.3; 10263 -2.3; 11289 -2.3; 12418 -2.3; 13660 -2.3; 15026 -2.3; 16529 -2.3; 18182 -2.3; 20000 -2.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan RE 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan RE 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.22 | -0.6 dB |
| Peaking | 1349 Hz | 0.74 | 2.2 dB  |
| Peaking | 2537 Hz | 1.18 | -7.1 dB |
| Peaking | 3837 Hz | 2.49 | 3.4 dB  |
| Peaking | 7096 Hz | 9.01 | 2.1 dB  |
| Peaking | 1235 Hz | 5.07 | -0.1 dB |
| Peaking | 5953 Hz | 5.35 | -1.6 dB |
| Peaking | 5964 Hz | 2    | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20RE%20600/HiFiMan%20RE%20600.png)