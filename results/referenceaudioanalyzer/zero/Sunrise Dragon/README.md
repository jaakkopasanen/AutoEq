# Sunrise Dragon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.8; 106 -1.5; 116 -2.0; 128 -2.6; 141 -3.2; 155 -3.8; 170 -4.3; 187 -4.8; 206 -5.3; 227 -5.8; 249 -6.3; 274 -6.7; 302 -7.1; 332 -7.5; 365 -7.9; 402 -8.0; 442 -8.1; 486 -8.2; 535 -7.9; 588 -7.5; 647 -7.2; 712 -7.3; 783 -8.1; 861 -9.0; 947 -10.0; 1042 -10.9; 1146 -11.7; 1261 -11.9; 1387 -11.9; 1526 -11.7; 1678 -11.3; 1846 -11.1; 2031 -10.8; 2234 -10.4; 2457 -9.8; 2703 -8.8; 2973 -7.5; 3270 -6.1; 3597 -5.0; 3957 -4.4; 4353 -4.6; 4788 -5.6; 5267 -7.0; 5793 -7.0; 6373 -4.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sunrise Dragon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sunrise Dragon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 120 Hz  | 0.09 | 7.0 dB  |
| Peaking | 315 Hz  | 0.59 | -6.9 dB |
| Peaking | 1414 Hz | 0.69 | -8.0 dB |
| Peaking | 3847 Hz | 2.59 | 3.8 dB  |
| Peaking | 6756 Hz | 8.65 | 3.7 dB  |
| Peaking | 165 Hz  | 2.62 | -0.6 dB |
| Peaking | 479 Hz  | 1.46 | -2.6 dB |
| Peaking | 674 Hz  | 0.6  | 2.5 dB  |
| Peaking | 1034 Hz | 1.76 | -2.2 dB |
| Peaking | 2360 Hz | 3.88 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sunrise%20Dragon/Sunrise%20Dragon.png)