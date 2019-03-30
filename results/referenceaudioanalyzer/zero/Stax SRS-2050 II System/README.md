# Stax SRS-2050 II System
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -1.3; 37 -2.9; 41 -5.5; 45 -7.5; 49 -9.1; 54 -10.6; 60 -11.7; 66 -12.0; 72 -11.7; 79 -10.8; 87 -9.7; 96 -8.8; 106 -8.0; 116 -7.3; 128 -6.8; 141 -6.4; 155 -6.1; 170 -5.8; 187 -5.6; 206 -5.5; 227 -5.4; 249 -5.1; 274 -5.4; 302 -5.4; 332 -5.2; 365 -5.2; 402 -5.2; 442 -5.2; 486 -5.1; 535 -4.8; 588 -4.8; 647 -5.1; 712 -5.3; 783 -5.6; 861 -6.1; 947 -6.5; 1042 -7.0; 1146 -7.4; 1261 -8.1; 1387 -8.8; 1526 -9.2; 1678 -9.4; 1846 -9.4; 2031 -8.9; 2234 -7.4; 2457 -5.5; 2703 -3.9; 2973 -3.0; 3270 -2.8; 3597 -3.1; 3957 -4.7; 4353 -6.6; 4788 -7.4; 5267 -6.5; 5793 -8.1; 6373 -11.7; 7010 -13.1; 7711 -11.2; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SRS-2050 II System GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SRS-2050 II System ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.17 | 20.2 dB  |
| Peaking | 63 Hz   | 0.46 | -24.9 dB |
| Peaking | 1744 Hz | 1.53 | -4.1 dB  |
| Peaking | 3099 Hz | 2.06 | 5.0 dB   |
| Peaking | 6943 Hz | 3.63 | -7.4 dB  |
| Peaking | 34 Hz   | 4.23 | 1.4 dB   |
| Peaking | 497 Hz  | 0.46 | -0.6 dB  |
| Peaking | 619 Hz  | 1.65 | 1.2 dB   |
| Peaking | 7802 Hz | 7.43 | -1.7 dB  |
| Peaking | 8792 Hz | 3.07 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -7.8 dB |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Stax%20SRS-2050%20II%20System/Stax%20SRS-2050%20II%20System.png)