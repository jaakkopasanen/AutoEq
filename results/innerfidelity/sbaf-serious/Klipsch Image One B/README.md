# Klipsch Image One B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.2; 25 -12.3; 28 -12.5; 31 -12.6; 34 -12.7; 37 -12.7; 41 -12.8; 45 -12.8; 49 -12.8; 54 -12.8; 60 -12.9; 66 -12.9; 72 -12.9; 79 -13.0; 87 -13.1; 96 -13.1; 106 -12.8; 116 -12.5; 128 -12.5; 141 -12.7; 155 -12.7; 170 -12.2; 187 -12.2; 206 -11.8; 227 -11.4; 249 -11.0; 274 -10.6; 302 -9.8; 332 -8.9; 365 -7.5; 402 -6.1; 442 -4.4; 486 -3.4; 535 -2.6; 588 -1.7; 647 -1.1; 712 -0.6; 783 -0.5; 861 -1.5; 947 -2.5; 1042 -2.4; 1146 -3.7; 1261 -4.6; 1387 -5.4; 1526 -6.1; 1678 -7.0; 1846 -7.7; 2031 -8.3; 2234 -8.7; 2457 -9.2; 2703 -10.1; 2973 -9.9; 3270 -8.6; 3597 -6.6; 3957 -4.2; 4353 -2.9; 4788 -1.2; 5267 -2.6; 5793 -2.8; 6373 -1.2; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.21 | -6.7 dB |
| Peaking | 289 Hz  | 0.6  | -5.1 dB |
| Peaking | 642 Hz  | 0.67 | 8.6 dB  |
| Peaking | 3064 Hz | 0.76 | -8.1 dB |
| Peaking | 4679 Hz | 1.22 | 9.3 dB  |
| Peaking | 5516 Hz | 9.5  | -1.7 dB |
| Peaking | 6573 Hz | 5.55 | 3.3 dB  |
| Peaking | 7514 Hz | 3.74 | -1.4 dB |
| Peaking | 9178 Hz | 1.95 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One%20B/Klipsch%20Image%20One%20B.png)