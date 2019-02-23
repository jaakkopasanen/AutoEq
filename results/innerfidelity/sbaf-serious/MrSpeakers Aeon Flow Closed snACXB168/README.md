# MrSpeakers Aeon Flow Closed snACXB168
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.3; 25 -3.3; 28 -3.4; 31 -3.4; 34 -3.5; 37 -3.6; 41 -3.6; 45 -3.7; 49 -3.8; 54 -3.6; 60 -3.2; 66 -3.0; 72 -3.2; 79 -3.8; 87 -4.3; 96 -4.4; 106 -4.0; 116 -3.6; 128 -3.6; 141 -3.4; 155 -2.9; 170 -3.8; 187 -4.1; 206 -4.2; 227 -4.3; 249 -4.5; 274 -4.6; 302 -4.7; 332 -4.8; 365 -4.6; 402 -4.6; 442 -4.5; 486 -4.9; 535 -5.2; 588 -5.2; 647 -5.5; 712 -5.6; 783 -5.3; 861 -5.0; 947 -4.4; 1042 -3.4; 1146 -4.4; 1261 -4.8; 1387 -5.2; 1526 -5.3; 1678 -5.2; 1846 -4.7; 2031 -3.4; 2234 -2.3; 2457 -1.6; 2703 -2.6; 2973 -0.5; 3270 -1.6; 3597 -2.4; 3957 -2.0; 4353 -3.8; 4788 -2.1; 5267 -0.7; 5793 -2.1; 6373 -3.1; 7010 -5.8; 7711 -7.3; 8482 -7.7; 9330 -6.0; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed snACXB168 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed snACXB168 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 635 Hz  |  1.58 | -1.5 dB |
| Peaking | 1630 Hz |  2.83 | -2.0 dB |
| Peaking | 2816 Hz |  1.44 | 2.9 dB  |
| Peaking | 5387 Hz |  4.14 | 3.1 dB  |
| Peaking | 8123 Hz |  3.28 | -4.3 dB |
| Peaking | 21 Hz   |  1.01 | 0.8 dB  |
| Peaking | 66 Hz   |  4.83 | 1.0 dB  |
| Peaking | 153 Hz  |  4.45 | 1.2 dB  |
| Peaking | 280 Hz  |  1.86 | -0.5 dB |
| Peaking | 1038 Hz | 10.82 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Closed%20snACXB168/MrSpeakers%20Aeon%20Flow%20Closed%20snACXB168.png)