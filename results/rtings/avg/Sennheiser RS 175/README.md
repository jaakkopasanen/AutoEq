# Sennheiser RS 175
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -14.6; 25 -14.5; 28 -14.3; 31 -13.9; 34 -13.5; 37 -13.0; 41 -12.4; 45 -11.9; 49 -11.3; 54 -10.8; 60 -10.5; 66 -10.5; 72 -10.7; 79 -11.0; 87 -11.3; 96 -11.4; 106 -11.3; 116 -11.0; 128 -10.4; 141 -9.4; 155 -8.2; 170 -6.7; 187 -5.1; 206 -3.7; 227 -2.6; 249 -2.1; 274 -2.1; 302 -2.4; 332 -2.8; 365 -2.3; 402 -1.1; 442 -0.5; 486 -1.0; 535 -1.7; 588 -2.4; 647 -3.0; 712 -3.6; 783 -4.2; 861 -4.6; 947 -5.0; 1042 -5.3; 1146 -5.6; 1261 -6.0; 1387 -6.1; 1526 -5.7; 1678 -5.0; 1846 -4.5; 2031 -5.9; 2234 -9.7; 2457 -12.4; 2703 -13.1; 2973 -12.4; 3270 -10.3; 3597 -7.8; 3957 -7.0; 4353 -7.1; 4788 -6.9; 5267 -6.9; 5793 -6.8; 6373 -1.7; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.7; 12418 -5.5; 13660 -5.5; 15026 -7.2; 16529 -5.9; 18182 -5.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 175 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 175 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.48 | -8.0 dB |
| Peaking | 30 Hz   | 0.73 | -4.7 dB |
| Peaking | 114 Hz  | 1    | -6.7 dB |
| Peaking | 306 Hz  | 0.58 | 5.2 dB  |
| Peaking | 2746 Hz | 2.76 | -8.6 dB |
| Peaking | 498 Hz  | 2.72 | 1.9 dB  |
| Peaking | 998 Hz  | 0.38 | -0.9 dB |
| Peaking | 1856 Hz | 5.22 | 3.1 dB  |
| Peaking | 5729 Hz | 3.88 | -2.7 dB |
| Peaking | 6494 Hz | 5.66 | 6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | 4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20175/Sennheiser%20RS%20175.png)