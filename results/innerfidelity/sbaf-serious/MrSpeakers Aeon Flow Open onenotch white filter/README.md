# MrSpeakers Aeon Flow Open onenotch white filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.1; 31 -5.2; 34 -5.3; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.8; 54 -6.1; 60 -6.2; 66 -6.6; 72 -7.3; 79 -8.5; 87 -9.3; 96 -9.9; 106 -10.4; 116 -10.8; 128 -11.0; 141 -11.0; 155 -10.5; 170 -10.9; 187 -11.2; 206 -11.0; 227 -10.7; 249 -10.6; 274 -10.3; 302 -10.0; 332 -9.8; 365 -9.5; 402 -9.0; 442 -8.5; 486 -8.4; 535 -7.6; 588 -7.1; 647 -6.9; 712 -6.9; 783 -6.5; 861 -5.9; 947 -5.9; 1042 -5.5; 1146 -4.6; 1261 -3.3; 1387 -5.2; 1526 -6.7; 1678 -7.5; 1846 -7.1; 2031 -6.3; 2234 -5.3; 2457 -3.1; 2703 -1.5; 2973 -2.6; 3270 -0.9; 3597 -2.3; 3957 -3.7; 4353 -3.7; 4788 -3.5; 5267 -1.9; 5793 -0.5; 6373 -0.5; 7010 -3.2; 7711 -5.4; 8482 -8.4; 9330 -9.3; 10263 -6.1; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Open onenotch white filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Open onenotch white filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 195 Hz  |  0.51 | -5.6 dB |
| Peaking | 1881 Hz |  1.94 | -7.8 dB |
| Peaking | 2258 Hz |  0.81 | 6.7 dB  |
| Peaking | 6161 Hz |  3.53 | 5.0 dB  |
| Peaking | 8972 Hz |  4.1  | -5.0 dB |
| Peaking | 56 Hz   |  0.41 | 1.5 dB  |
| Peaking | 102 Hz  |  1.62 | -2.2 dB |
| Peaking | 1244 Hz |  5.85 | 3.3 dB  |
| Peaking | 1255 Hz |  2.09 | -1.4 dB |
| Peaking | 4142 Hz | 11.63 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Open%20onenotch%20white%20filter/MrSpeakers%20Aeon%20Flow%20Open%20onenotch%20white%20filter.png)