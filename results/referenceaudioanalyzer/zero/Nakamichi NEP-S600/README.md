# Nakamichi NEP-S600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.9; 25 -14.2; 28 -14.7; 31 -15.0; 34 -15.2; 37 -15.3; 41 -15.4; 45 -15.5; 49 -15.5; 54 -15.5; 60 -15.4; 66 -15.3; 72 -15.1; 79 -15.0; 87 -14.7; 96 -14.4; 106 -14.1; 116 -13.7; 128 -13.3; 141 -12.9; 155 -12.4; 170 -11.9; 187 -11.4; 206 -10.7; 227 -10.0; 249 -9.4; 274 -9.3; 302 -9.2; 332 -8.7; 365 -7.9; 402 -7.1; 442 -6.4; 486 -5.7; 535 -5.0; 588 -4.4; 647 -3.9; 712 -3.3; 783 -3.0; 861 -2.8; 947 -2.5; 1042 -2.8; 1146 -3.0; 1261 -3.3; 1387 -3.7; 1526 -3.8; 1678 -3.7; 1846 -3.2; 2031 -2.9; 2234 -2.6; 2457 -2.1; 2703 -1.6; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -1.6; 4353 -2.5; 4788 -2.5; 5267 -3.2; 5793 -4.2; 6373 -3.1; 7010 -2.5; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nakamichi NEP-S600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nakamichi NEP-S600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.32 | -3.4 dB |
| Peaking | 71 Hz   | 0.26 | -8.6 dB |
| Peaking | 815 Hz  | 1.02 | 3.1 dB  |
| Peaking | 3287 Hz | 1.41 | 4.4 dB  |
| Peaking | 6749 Hz | 8.98 | 2.7 dB  |
| Peaking | 241 Hz  | 4.35 | 0.6 dB  |
| Peaking | 317 Hz  | 4.38 | -0.7 dB |
| Peaking | 8628 Hz | 2.8  | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Nakamichi%20NEP-S600/Nakamichi%20NEP-S600.png)