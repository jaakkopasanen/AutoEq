# Sony MDR-EX450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.6; 25 -8.9; 28 -9.4; 31 -9.8; 34 -10.1; 37 -10.3; 41 -10.5; 45 -10.7; 49 -10.8; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.2; 79 -11.2; 87 -11.2; 96 -11.1; 106 -10.9; 116 -10.9; 128 -10.7; 141 -10.5; 155 -10.3; 170 -10.0; 187 -9.7; 206 -9.5; 227 -9.1; 249 -8.8; 274 -8.3; 302 -7.9; 332 -7.4; 365 -6.8; 402 -6.3; 442 -5.7; 486 -5.2; 535 -4.5; 588 -4.0; 647 -3.4; 712 -2.8; 783 -2.2; 861 -1.8; 947 -1.3; 1042 -0.9; 1146 -0.6; 1261 -0.5; 1387 -0.5; 1526 -0.6; 1678 -0.7; 1846 -0.6; 2031 -1.1; 2234 -3.7; 2457 -6.9; 2703 -8.4; 2973 -7.7; 3270 -5.7; 3597 -4.2; 3957 -4.5; 4353 -6.8; 4788 -9.5; 5267 -10.0; 5793 -8.0; 6373 -3.8; 7010 -2.3; 7711 -4.5; 8482 -4.7; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.46 | -2.7 dB |
| Peaking | 127 Hz  | 0.3  | -5.3 dB |
| Peaking | 1867 Hz | 0.38 | 6.1 dB  |
| Peaking | 2725 Hz | 2.52 | -9.1 dB |
| Peaking | 5053 Hz | 3.28 | -8.5 dB |
| Peaking | 1948 Hz | 2.22 | -0.8 dB |
| Peaking | 1987 Hz | 5.64 | 1.7 dB  |
| Peaking | 5826 Hz | 9.08 | -1.6 dB |
| Peaking | 6769 Hz | 7.21 | 3.8 dB  |
| Peaking | 8835 Hz | 1.43 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-EX450/Sony%20MDR-EX450.png)