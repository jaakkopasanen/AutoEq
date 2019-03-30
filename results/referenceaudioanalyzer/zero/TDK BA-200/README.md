# TDK BA-200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.2; 28 -11.2; 31 -11.2; 34 -11.2; 37 -11.2; 41 -11.2; 45 -11.2; 49 -11.2; 54 -11.2; 60 -11.2; 66 -11.2; 72 -11.2; 79 -11.2; 87 -11.2; 96 -11.2; 106 -11.1; 116 -10.9; 128 -10.9; 141 -10.9; 155 -10.7; 170 -10.5; 187 -10.5; 206 -10.2; 227 -10.2; 249 -10.0; 274 -9.8; 302 -9.5; 332 -9.2; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.1; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.5; 783 -6.1; 861 -5.8; 947 -5.4; 1042 -5.2; 1146 -5.0; 1261 -5.0; 1387 -5.2; 1526 -5.5; 1678 -6.1; 1846 -6.7; 2031 -7.2; 2234 -7.3; 2457 -7.2; 2703 -6.6; 2973 -5.6; 3270 -4.1; 3597 -2.8; 3957 -3.0; 4353 -4.6; 4788 -5.0; 5267 -3.5; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TDK BA-200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK BA-200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.11 | -5.3 dB |
| Peaking | 1019 Hz | 1.92 | 1.8 dB  |
| Peaking | 3716 Hz | 5.53 | 3.6 dB  |
| Peaking | 6177 Hz | 3.49 | 7.0 dB  |
| Peaking | 7131 Hz | 1.4  | -1.2 dB |
| Peaking | 1431 Hz | 3.02 | 0.9 dB  |
| Peaking | 2254 Hz | 1.98 | -1.7 dB |
| Peaking | 3239 Hz | 5.35 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/TDK%20BA-200/TDK%20BA-200.png)