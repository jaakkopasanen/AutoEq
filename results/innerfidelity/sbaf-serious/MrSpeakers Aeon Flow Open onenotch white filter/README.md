# MrSpeakers Aeon Flow Open onenotch white filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.6; 25 -4.7; 28 -4.8; 31 -4.9; 34 -5.0; 37 -5.1; 41 -5.2; 45 -5.4; 49 -5.6; 54 -5.8; 60 -5.9; 66 -6.3; 72 -7.0; 79 -8.3; 87 -9.0; 96 -9.6; 106 -10.1; 116 -10.5; 128 -10.7; 141 -10.8; 155 -10.2; 170 -10.6; 187 -10.9; 206 -10.7; 227 -10.5; 249 -10.3; 274 -10.0; 302 -9.7; 332 -9.5; 365 -9.2; 402 -8.8; 442 -8.3; 486 -8.1; 535 -7.3; 588 -6.9; 647 -6.7; 712 -6.6; 783 -6.3; 861 -5.6; 947 -5.6; 1042 -5.3; 1146 -4.4; 1261 -3.1; 1387 -4.9; 1526 -6.5; 1678 -7.3; 1846 -6.8; 2031 -6.0; 2234 -5.0; 2457 -2.8; 2703 -1.3; 2973 -2.3; 3270 -0.6; 3597 -2.0; 3957 -3.5; 4353 -3.4; 4788 -3.2; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -8.2; 9330 -9.1; 10263 -6.5; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Open onenotch white filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Open onenotch white filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 185 Hz  | 0.69 | -4.7 dB |
| Peaking | 1220 Hz | 4.94 | 3.2 dB  |
| Peaking | 3107 Hz | 2.25 | 5.2 dB  |
| Peaking | 5943 Hz | 2.54 | 6.0 dB  |
| Peaking | 8866 Hz | 3.74 | -3.8 dB |
| Peaking | 24 Hz   | 0.31 | 1.9 dB  |
| Peaking | 64 Hz   | 3.36 | 0.6 dB  |
| Peaking | 95 Hz   | 1.8  | -1.9 dB |
| Peaking | 1655 Hz | 1.01 | 1.6 dB  |
| Peaking | 1739 Hz | 2.51 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Open%20onenotch%20white%20filter/MrSpeakers%20Aeon%20Flow%20Open%20onenotch%20white%20filter.png)