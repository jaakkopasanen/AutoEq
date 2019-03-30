# Sony MDR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -11.0; 25 -11.5; 28 -12.2; 31 -12.6; 34 -12.8; 37 -12.9; 41 -12.9; 45 -12.9; 49 -12.8; 54 -12.6; 60 -12.4; 66 -12.2; 72 -12.0; 79 -11.7; 87 -11.4; 96 -11.2; 106 -11.2; 116 -11.2; 128 -11.5; 141 -11.6; 155 -11.6; 170 -11.4; 187 -11.2; 206 -11.0; 227 -10.5; 249 -10.0; 274 -9.3; 302 -8.3; 332 -7.3; 365 -6.4; 402 -6.0; 442 -6.1; 486 -5.8; 535 -5.7; 588 -5.7; 647 -6.0; 712 -6.5; 783 -6.8; 861 -6.7; 947 -5.9; 1042 -4.2; 1146 -1.6; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -2.0; 1846 -4.3; 2031 -6.2; 2234 -7.6; 2457 -8.3; 2703 -8.1; 2973 -7.3; 3270 -6.0; 3597 -4.6; 3957 -4.5; 4353 -5.5; 4788 -6.2; 5267 -6.9; 5793 -8.3; 6373 -9.8; 7010 -8.8; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.46 | -6.3 dB |
| Peaking | 177 Hz  | 1.36 | -3.7 dB |
| Peaking | 1368 Hz | 2.61 | 7.1 dB  |
| Peaking | 6514 Hz | 5.71 | -3.8 dB |
| Peaking | 475 Hz  | 2.05 | 1.3 dB  |
| Peaking | 835 Hz  | 4.92 | -1.4 dB |
| Peaking | 1664 Hz | 6.07 | 2.0 dB  |
| Peaking | 2504 Hz | 2.39 | -2.8 dB |
| Peaking | 3770 Hz | 3.81 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-Z7/Sony%20MDR-Z7.png)