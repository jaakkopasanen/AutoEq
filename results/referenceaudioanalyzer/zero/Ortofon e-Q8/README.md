# Ortofon e-Q8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.5; 25 -8.4; 28 -8.3; 31 -8.2; 34 -8.2; 37 -8.2; 41 -8.1; 45 -8.0; 49 -7.9; 54 -7.9; 60 -7.9; 66 -7.9; 72 -7.9; 79 -7.9; 87 -8.1; 96 -8.2; 106 -8.3; 116 -8.3; 128 -8.3; 141 -8.2; 155 -8.1; 170 -8.0; 187 -7.9; 206 -7.9; 227 -7.9; 249 -7.9; 274 -7.9; 302 -7.6; 332 -7.6; 365 -7.5; 402 -7.3; 442 -7.1; 486 -6.9; 535 -6.6; 588 -6.3; 647 -6.0; 712 -5.7; 783 -5.3; 861 -5.0; 947 -4.6; 1042 -4.3; 1146 -4.0; 1261 -3.7; 1387 -3.4; 1526 -3.4; 1678 -3.4; 1846 -3.6; 2031 -4.0; 2234 -4.6; 2457 -6.2; 2703 -9.6; 2973 -9.7; 3270 -5.0; 3597 -1.1; 3957 -2.3; 4353 -5.7; 4788 -5.1; 5267 -2.1; 5793 -0.5; 6373 -1.5; 7010 -3.7; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon e-Q8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon e-Q8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.52 | -2.8 dB |
| Peaking | 176 Hz  | 0.26 | -2.8 dB |
| Peaking | 2104 Hz | 0.48 | 2.8 dB  |
| Peaking | 2799 Hz | 5.01 | -8.2 dB |
| Peaking | 5922 Hz | 5.29 | 4.4 dB  |
| Peaking | 3137 Hz | 5.65 | -2.1 dB |
| Peaking | 3677 Hz | 4.33 | 4.5 dB  |
| Peaking | 4538 Hz | 4.57 | -3.7 dB |
| Peaking | 5319 Hz | 5.32 | 1.5 dB  |
| Peaking | 8836 Hz | 2.37 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ortofon%20e-Q8/Ortofon%20e-Q8.png)