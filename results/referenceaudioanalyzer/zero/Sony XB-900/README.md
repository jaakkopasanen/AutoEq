# Sony XB-900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -8.4; 25 -9.2; 28 -10.3; 31 -11.0; 34 -11.6; 37 -12.0; 41 -12.4; 45 -12.8; 49 -13.0; 54 -13.2; 60 -13.4; 66 -13.5; 72 -13.7; 79 -13.9; 87 -14.1; 96 -14.4; 106 -14.5; 116 -14.8; 128 -14.6; 141 -14.6; 155 -14.8; 170 -14.7; 187 -14.2; 206 -13.1; 227 -11.8; 249 -10.7; 274 -9.5; 302 -7.9; 332 -6.4; 365 -5.5; 402 -5.4; 442 -5.7; 486 -6.1; 535 -6.3; 588 -6.0; 647 -5.6; 712 -5.0; 783 -4.4; 861 -3.5; 947 -2.5; 1042 -1.6; 1146 -1.2; 1261 -0.8; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.9; 2234 -2.2; 2457 -3.9; 2703 -4.7; 2973 -3.5; 3270 -0.7; 3597 -0.7; 3957 -4.3; 4353 -5.7; 4788 -5.5; 5267 -6.1; 5793 -7.3; 6373 -6.9; 7010 -6.7; 7711 -7.0; 8482 -6.3; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XB-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XB-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.92 | -3.5 dB |
| Peaking | 160 Hz  | 0.41 | -9.1 dB |
| Peaking | 352 Hz  | 1.39 | 5.9 dB  |
| Peaking | 1290 Hz | 0.94 | 5.4 dB  |
| Peaking | 2419 Hz | 0.84 | 2.1 dB  |
| Peaking | 74 Hz   | 2.66 | -0.1 dB |
| Peaking | 1989 Hz | 3.92 | 1.4 dB  |
| Peaking | 2633 Hz | 3.16 | -2.7 dB |
| Peaking | 3397 Hz | 5.19 | 5.0 dB  |
| Peaking | 5824 Hz | 1.3  | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XB-900/Sony%20XB-900.png)