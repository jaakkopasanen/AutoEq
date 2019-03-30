# Ortofon e-Q7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.4; 25 -8.6; 28 -8.8; 31 -8.9; 34 -9.0; 37 -9.1; 41 -9.1; 45 -9.1; 49 -9.1; 54 -9.1; 60 -9.1; 66 -9.1; 72 -9.1; 79 -9.1; 87 -9.1; 96 -9.1; 106 -9.1; 116 -9.1; 128 -9.1; 141 -9.0; 155 -8.7; 170 -8.7; 187 -8.5; 206 -8.4; 227 -8.4; 249 -8.4; 274 -8.3; 302 -8.1; 332 -7.9; 365 -7.7; 402 -7.4; 442 -7.1; 486 -6.8; 535 -6.4; 588 -6.1; 647 -5.8; 712 -5.4; 783 -5.0; 861 -4.7; 947 -4.2; 1042 -3.7; 1146 -3.2; 1261 -2.7; 1387 -2.1; 1526 -1.4; 1678 -0.7; 1846 -2.2; 2031 -5.2; 2234 -7.2; 2457 -9.0; 2703 -10.3; 2973 -9.3; 3270 -5.5; 3597 -1.8; 3957 -2.2; 4353 -4.2; 4788 -3.7; 5267 -1.6; 5793 -0.5; 6373 -1.6; 7010 -5.0; 7711 -7.2; 8482 -6.6; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon e-Q7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon e-Q7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 73 Hz    | 0.17 | -3.3 dB  |
| Peaking | 1738 Hz  | 0.96 | 11.9 dB  |
| Peaking | 2752 Hz  | 0.86 | -14.3 dB |
| Peaking | 3647 Hz  | 2.62 | 10.8 dB  |
| Peaking | 5749 Hz  | 2.99 | 7.9 dB   |
| Peaking | 6477 Hz  | 8.84 | 1.5 dB   |
| Peaking | 7802 Hz  | 3.19 | -2.3 dB  |
| Peaking | 8940 Hz  | 3.75 | 1.0 dB   |
| Peaking | 10292 Hz | 0.86 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ortofon%20e-Q7/Ortofon%20e-Q7.png)