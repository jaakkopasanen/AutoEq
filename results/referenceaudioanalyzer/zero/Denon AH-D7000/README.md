# Denon AH-D7000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.6; 25 -5.2; 28 -5.8; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.7; 45 -6.7; 49 -6.7; 54 -6.7; 60 -6.6; 66 -6.4; 72 -6.3; 79 -6.1; 87 -5.8; 96 -5.7; 106 -5.6; 116 -5.4; 128 -5.2; 141 -4.8; 155 -4.4; 170 -4.1; 187 -3.9; 206 -3.7; 227 -3.6; 249 -3.4; 274 -3.3; 302 -3.1; 332 -2.9; 365 -2.8; 402 -2.8; 442 -2.6; 486 -2.4; 535 -2.4; 588 -2.7; 647 -3.2; 712 -4.1; 783 -5.0; 861 -4.9; 947 -4.1; 1042 -3.7; 1146 -3.7; 1261 -3.4; 1387 -3.1; 1526 -3.1; 1678 -3.0; 1846 -2.7; 2031 -2.5; 2234 -2.4; 2457 -2.0; 2703 -1.3; 2973 -0.5; 3270 -0.6; 3597 -2.3; 3957 -4.5; 4353 -5.4; 4788 -5.6; 5267 -5.5; 5793 -5.3; 6373 -6.7; 7010 -9.6; 7711 -11.3; 8482 -10.3; 9330 -8.3; 10263 -8.1; 11289 -8.9; 12418 -7.6; 13660 -5.2; 15026 -4.2; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 52 Hz    | 0.66 | -2.7 dB |
| Peaking | 390 Hz   | 1.07 | 1.7 dB  |
| Peaking | 2899 Hz  | 2.18 | 3.9 dB  |
| Peaking | 7826 Hz  | 2.15 | -7.0 dB |
| Peaking | 11531 Hz | 2.96 | -3.9 dB |
| Peaking | 572 Hz   | 4.03 | 0.8 dB  |
| Peaking | 805 Hz   | 4.2  | -1.7 dB |
| Peaking | 1566 Hz  | 1.71 | 0.8 dB  |
| Peaking | 4411 Hz  | 4.6  | -1.6 dB |
| Peaking | 5988 Hz  | 7.87 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-D7000/Denon%20AH-D7000.png)