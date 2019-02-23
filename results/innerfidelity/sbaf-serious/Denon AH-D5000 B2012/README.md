# Denon AH-D5000 B2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.5; 25 -3.1; 28 -3.7; 31 -4.0; 34 -4.2; 37 -4.4; 41 -4.4; 45 -4.5; 49 -4.4; 54 -4.4; 60 -4.6; 66 -4.6; 72 -4.4; 79 -4.4; 87 -4.9; 96 -5.3; 106 -5.5; 116 -5.6; 128 -5.7; 141 -5.9; 155 -6.0; 170 -5.8; 187 -5.9; 206 -5.8; 227 -5.6; 249 -5.5; 274 -5.2; 302 -5.0; 332 -4.7; 365 -4.5; 402 -4.2; 442 -3.8; 486 -3.6; 535 -3.1; 588 -2.2; 647 -1.6; 712 -1.7; 783 -2.8; 861 -3.4; 947 -1.6; 1042 -2.5; 1146 -2.9; 1261 -3.4; 1387 -4.2; 1526 -5.3; 1678 -6.0; 1846 -6.3; 2031 -6.2; 2234 -5.2; 2457 -1.0; 2703 -1.7; 2973 -0.6; 3270 -1.9; 3597 -1.5; 3957 -0.5; 4353 -0.9; 4788 -2.6; 5267 -3.1; 5793 -3.9; 6373 -4.3; 7010 -5.1; 7711 -3.6; 8482 -3.8; 9330 -4.6; 10263 -6.3; 11289 -4.4; 12418 -4.6; 13660 -5.3; 15026 -3.8; 16529 -3.8; 18182 -4.3; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 B2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.72 | 2.6 dB  |
| Peaking | 196 Hz  | 0.5  | -2.3 dB |
| Peaking | 724 Hz  | 0.81 | 2.4 dB  |
| Peaking | 1937 Hz | 1.83 | -5.6 dB |
| Peaking | 2784 Hz | 1.3  | 4.7 dB  |
| Peaking | 18 Hz   | 2.35 | 1.4 dB  |
| Peaking | 4190 Hz | 6.83 | 2.3 dB  |
| Peaking | 6896 Hz | 6.44 | -1.1 dB |
| Peaking | 8542 Hz | 2.71 | 3.5 dB  |
| Peaking | 9101 Hz | 1.41 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000%20B2012/Denon%20AH-D5000%20B2012.png)