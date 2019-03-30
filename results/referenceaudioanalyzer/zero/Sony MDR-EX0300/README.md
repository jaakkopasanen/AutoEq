# Sony MDR-EX0300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.5; 28 -4.6; 31 -4.8; 34 -4.8; 37 -4.9; 41 -4.9; 45 -4.8; 49 -4.8; 54 -4.8; 60 -4.8; 66 -4.8; 72 -4.8; 79 -4.8; 87 -4.8; 96 -4.9; 106 -4.8; 116 -4.5; 128 -4.5; 141 -4.3; 155 -4.1; 170 -3.7; 187 -3.6; 206 -3.9; 227 -3.9; 249 -3.9; 274 -3.6; 302 -3.4; 332 -3.2; 365 -2.9; 402 -2.8; 442 -2.6; 486 -2.3; 535 -2.1; 588 -1.9; 647 -1.8; 712 -1.6; 783 -1.6; 861 -1.6; 947 -1.8; 1042 -1.9; 1146 -2.1; 1261 -2.4; 1387 -2.8; 1526 -3.3; 1678 -4.0; 1846 -4.9; 2031 -5.8; 2234 -6.3; 2457 -6.6; 2703 -6.5; 2973 -5.4; 3270 -3.5; 3597 -2.2; 3957 -2.8; 4353 -5.1; 4788 -7.5; 5267 -8.6; 5793 -7.5; 6373 -3.7; 7010 -0.5; 7711 -2.5; 8482 -2.8; 9330 -2.8; 10263 -2.8; 11289 -2.8; 12418 -2.8; 13660 -2.8; 15026 -2.8; 16529 -2.8; 18182 -2.8; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX0300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX0300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.36 | -1.6 dB |
| Peaking | 123 Hz  | 0.41 | -1.0 dB |
| Peaking | 2299 Hz | 1.3  | -7.0 dB |
| Peaking | 2389 Hz | 0.33 | 3.3 dB  |
| Peaking | 5240 Hz | 3.51 | -7.9 dB |
| Peaking | 2861 Hz | 6.97 | -1.0 dB |
| Peaking | 3620 Hz | 6.37 | 1.8 dB  |
| Peaking | 6037 Hz | 8.71 | -1.5 dB |
| Peaking | 6860 Hz | 7.11 | 3.5 dB  |
| Peaking | 8552 Hz | 0.81 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-EX0300/Sony%20MDR-EX0300.png)