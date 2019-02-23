# AKG K240 Monitor
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.2; 41 -2.1; 45 -3.0; 49 -3.8; 54 -4.6; 60 -5.4; 66 -5.9; 72 -6.1; 79 -6.4; 87 -7.0; 96 -7.4; 106 -7.9; 116 -8.4; 128 -8.8; 141 -9.1; 155 -9.2; 170 -9.0; 187 -9.2; 206 -9.2; 227 -9.0; 249 -8.9; 274 -8.7; 302 -8.7; 332 -8.8; 365 -8.8; 402 -8.5; 442 -8.1; 486 -8.1; 535 -7.7; 588 -7.1; 647 -6.7; 712 -6.4; 783 -6.1; 861 -6.0; 947 -5.7; 1042 -5.6; 1146 -5.4; 1261 -5.3; 1387 -5.7; 1526 -6.5; 1678 -7.1; 1846 -7.2; 2031 -7.1; 2234 -6.1; 2457 -4.5; 2703 -4.2; 2973 -2.7; 3270 -4.6; 3597 -9.4; 3957 -8.2; 4353 -5.7; 4788 -3.7; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -9.2; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 Monitor GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Monitor ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.8  | 6.7 dB  |
| Peaking | 177 Hz   | 0.61 | -3.1 dB |
| Peaking | 2838 Hz  | 3.54 | 5.1 dB  |
| Peaking | 5372 Hz  | 0.74 | -5.8 dB |
| Peaking | 5774 Hz  | 2.09 | 12.7 dB |
| Peaking | 1104 Hz  | 2.31 | 1.7 dB  |
| Peaking | 3712 Hz  | 6.37 | -5.3 dB |
| Peaking | 3743 Hz  | 2.37 | 2.2 dB  |
| Peaking | 9298 Hz  | 3.81 | -3.5 dB |
| Peaking | 10318 Hz | 1.3  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Monitor/AKG%20K240%20Monitor.png)