# MrSpeakers Aeon Flow Closed snACXB168
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.3; 25 -3.3; 28 -3.4; 31 -3.4; 34 -3.5; 37 -3.6; 41 -3.6; 45 -3.7; 49 -3.8; 54 -3.6; 60 -3.2; 66 -3.0; 72 -3.2; 79 -3.8; 87 -4.3; 96 -4.4; 106 -4.0; 116 -3.6; 128 -3.6; 141 -3.4; 155 -2.9; 170 -3.8; 187 -4.1; 206 -4.2; 227 -4.3; 249 -4.5; 274 -4.6; 302 -4.7; 332 -4.8; 365 -4.6; 402 -4.6; 442 -4.5; 486 -4.9; 535 -5.2; 588 -5.2; 647 -5.5; 712 -5.6; 783 -5.3; 861 -5.0; 947 -4.4; 1042 -3.4; 1146 -4.4; 1261 -4.8; 1387 -5.2; 1526 -5.3; 1678 -5.2; 1846 -4.7; 2031 -3.4; 2234 -2.3; 2457 -1.6; 2703 -2.6; 2973 -0.5; 3270 -1.6; 3597 -2.4; 3957 -2.0; 4353 -3.8; 4788 -2.1; 5267 -0.7; 5793 -2.1; 6373 -3.1; 7010 -5.8; 7711 -7.3; 8482 -7.7; 9330 -6.0; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed snACXB168 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed snACXB168 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 595 Hz  | 0.97 | -1.5 dB |
| Peaking | 1625 Hz | 2.88 | -2.0 dB |
| Peaking | 2827 Hz | 1.56 | 2.7 dB  |
| Peaking | 5371 Hz | 4.41 | 3.0 dB  |
| Peaking | 8128 Hz | 3.24 | -4.6 dB |
| Peaking | 24 Hz   | 0.51 | 0.7 dB  |
| Peaking | 66 Hz   | 3.19 | 1.6 dB  |
| Peaking | 119 Hz  | 0.51 | -1.6 dB |
| Peaking | 147 Hz  | 1.61 | 2.1 dB  |
| Peaking | 436 Hz  | 3.15 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Closed%20snACXB168/MrSpeakers%20Aeon%20Flow%20Closed%20snACXB168.png)