# MrSpeakers Aeon Flow Closed PreProduction
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.1; 28 -3.3; 31 -3.4; 34 -3.4; 37 -3.4; 41 -3.5; 45 -3.5; 49 -3.5; 54 -3.7; 60 -3.7; 66 -3.6; 72 -3.7; 79 -3.9; 87 -4.6; 96 -5.6; 106 -6.3; 116 -6.4; 128 -6.2; 141 -5.3; 155 -4.1; 170 -4.0; 187 -4.1; 206 -3.8; 227 -3.7; 249 -3.8; 274 -3.9; 302 -4.0; 332 -4.2; 365 -4.3; 402 -4.3; 442 -4.0; 486 -4.0; 535 -3.9; 588 -3.8; 647 -3.7; 712 -3.7; 783 -3.5; 861 -3.3; 947 -4.1; 1042 -4.5; 1146 -4.8; 1261 -5.0; 1387 -5.4; 1526 -5.9; 1678 -6.2; 1846 -5.8; 2031 -4.6; 2234 -4.0; 2457 -3.4; 2703 -1.9; 2973 -1.0; 3270 -1.3; 3597 -2.8; 3957 -3.3; 4353 -3.2; 4788 -2.7; 5267 -0.5; 5793 -0.7; 6373 -0.6; 7010 -1.4; 7711 -3.7; 8482 -6.5; 9330 -7.3; 10263 -4.2; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed PreProduction GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed PreProduction ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 115 Hz  | 3.2  | -2.8 dB |
| Peaking | 1651 Hz | 2.34 | -2.5 dB |
| Peaking | 2961 Hz | 3.56 | 3.1 dB  |
| Peaking | 6099 Hz | 2.45 | 4.2 dB  |
| Peaking | 8937 Hz | 4.36 | -4.5 dB |
| Peaking | 21 Hz   | 0.8  | 1.0 dB  |
| Peaking | 67 Hz   | 4.25 | 0.3 dB  |
| Peaking | 825 Hz  | 4.33 | 0.9 dB  |
| Peaking | 1092 Hz | 3.92 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Closed%20PreProduction/MrSpeakers%20Aeon%20Flow%20Closed%20PreProduction.png)