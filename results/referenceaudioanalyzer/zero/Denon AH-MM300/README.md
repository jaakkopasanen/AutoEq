# Denon AH-MM300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.2; 25 -11.2; 28 -11.2; 31 -11.2; 34 -11.1; 37 -11.0; 41 -11.1; 45 -11.3; 49 -11.4; 54 -11.4; 60 -11.3; 66 -11.4; 72 -11.6; 79 -11.7; 87 -11.7; 96 -11.6; 106 -11.4; 116 -11.0; 128 -10.6; 141 -10.0; 155 -9.2; 170 -8.0; 187 -6.7; 206 -5.2; 227 -4.0; 249 -3.6; 274 -3.5; 302 -3.2; 332 -2.8; 365 -2.5; 402 -2.2; 442 -2.4; 486 -2.6; 535 -2.7; 588 -2.9; 647 -3.2; 712 -3.5; 783 -3.7; 861 -4.0; 947 -4.2; 1042 -4.4; 1146 -4.5; 1261 -4.4; 1387 -4.2; 1526 -4.2; 1678 -4.2; 1846 -4.5; 2031 -4.4; 2234 -3.8; 2457 -3.4; 2703 -3.8; 2973 -3.7; 3270 -3.0; 3597 -2.1; 3957 -0.8; 4353 -0.5; 4788 -2.2; 5267 -3.3; 5793 -2.9; 6373 -2.2; 7010 -1.1; 7711 -3.0; 8482 -3.3; 9330 -3.3; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-MM300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-MM300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 67 Hz   | 0.21 | -9.1 dB |
| Peaking | 309 Hz  | 0.77 | 5.6 dB  |
| Peaking | 1422 Hz | 0.8  | -1.2 dB |
| Peaking | 4132 Hz | 3.23 | 3.0 dB  |
| Peaking | 4772 Hz | 1.94 | 0.5 dB  |
| Peaking | 20 Hz   | 1.08 | -1.7 dB |
| Peaking | 51 Hz   | 0.7  | 1.4 dB  |
| Peaking | 130 Hz  | 0.67 | -1.2 dB |
| Peaking | 214 Hz  | 3.34 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-MM300/Denon%20AH-MM300.png)