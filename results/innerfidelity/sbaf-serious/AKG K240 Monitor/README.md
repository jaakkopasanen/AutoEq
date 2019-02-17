# AKG K240 Monitor
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.9; 41 -2.9; 45 -3.8; 49 -4.6; 54 -5.4; 60 -6.2; 66 -6.7; 72 -6.9; 79 -7.2; 87 -7.8; 96 -8.2; 106 -8.7; 116 -9.2; 128 -9.6; 141 -9.9; 155 -10.0; 170 -9.8; 187 -10.0; 206 -10.0; 227 -9.8; 249 -9.7; 274 -9.5; 302 -9.5; 332 -9.6; 365 -9.6; 402 -9.3; 442 -8.9; 486 -8.9; 535 -8.5; 588 -7.9; 647 -7.5; 712 -7.2; 783 -6.9; 861 -6.8; 947 -6.5; 1042 -6.4; 1146 -6.2; 1261 -6.1; 1387 -6.5; 1526 -7.3; 1678 -7.9; 1846 -8.0; 2031 -7.9; 2234 -6.9; 2457 -5.3; 2703 -5.0; 2973 -3.5; 3270 -5.4; 3597 -10.2; 3957 -9.0; 4353 -6.5; 4788 -4.5; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -10.0; 10263 -8.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 Monitor GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Monitor ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.82 | 6.8 dB  |
| Peaking | 188 Hz  | 0.45 | -3.8 dB |
| Peaking | 3810 Hz | 6.75 | -5.3 dB |
| Peaking | 5890 Hz | 2.17 | 6.7 dB  |
| Peaking | 9065 Hz | 3.16 | -4.7 dB |
| Peaking | 461 Hz  | 2.36 | -0.7 dB |
| Peaking | 1299 Hz | 0.94 | 1.2 dB  |
| Peaking | 1801 Hz | 2.33 | -2.7 dB |
| Peaking | 3101 Hz | 3.71 | 4.8 dB  |
| Peaking | 3443 Hz | 4.37 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Monitor/AKG%20K240%20Monitor.png)