# MrSpeakers Ether C 2 Black Filters
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.5; 28 -5.4; 31 -5.4; 34 -5.2; 37 -4.9; 41 -4.3; 45 -3.8; 49 -3.7; 54 -4.5; 60 -5.2; 66 -4.7; 72 -4.5; 79 -4.7; 87 -4.9; 96 -5.7; 106 -6.6; 116 -6.1; 128 -6.0; 141 -5.4; 155 -4.5; 170 -5.4; 187 -6.3; 206 -6.8; 227 -7.1; 249 -7.4; 274 -7.5; 302 -7.5; 332 -7.5; 365 -7.2; 402 -6.8; 442 -6.3; 486 -6.4; 535 -6.4; 588 -6.4; 647 -6.6; 712 -7.0; 783 -6.9; 861 -7.5; 947 -7.8; 1042 -7.5; 1146 -7.0; 1261 -7.2; 1387 -7.6; 1526 -7.9; 1678 -8.2; 1846 -7.7; 2031 -7.0; 2234 -6.4; 2457 -6.1; 2703 -5.7; 2973 -5.2; 3270 -5.6; 3597 -5.6; 3957 -5.4; 4353 -5.7; 4788 -4.2; 5267 -1.5; 5793 -0.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C 2 Black Filters GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 2 Black Filters ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 1.03 | 1.8 dB  |
| Peaking | 288 Hz  | 2.12 | -1.7 dB |
| Peaking | 1324 Hz | 0.92 | -1.8 dB |
| Peaking | 6092 Hz | 2.44 | 6.8 dB  |
| Peaking | 7699 Hz | 2.36 | -2.0 dB |
| Peaking | 108 Hz  | 7.07 | -1.0 dB |
| Peaking | 156 Hz  | 7.95 | 1.8 dB  |
| Peaking | 1232 Hz | 4.11 | 1.4 dB  |
| Peaking | 2143 Hz | 0.78 | -1.6 dB |
| Peaking | 2586 Hz | 1.65 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%202%20Black%20Filters/MrSpeakers%20Ether%20C%202%20Black%20Filters.png)