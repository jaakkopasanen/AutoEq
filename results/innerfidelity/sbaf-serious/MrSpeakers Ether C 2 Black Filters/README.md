# MrSpeakers Ether C 2 Black Filters
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.1; 28 -4.1; 31 -4.0; 34 -3.8; 37 -3.5; 41 -2.9; 45 -2.4; 49 -2.3; 54 -3.1; 60 -3.8; 66 -3.3; 72 -3.1; 79 -3.3; 87 -3.6; 96 -4.3; 106 -5.2; 116 -4.7; 128 -4.6; 141 -4.0; 155 -3.1; 170 -4.0; 187 -4.9; 206 -5.4; 227 -5.7; 249 -6.1; 274 -6.1; 302 -6.1; 332 -6.1; 365 -5.8; 402 -5.4; 442 -4.9; 486 -5.0; 535 -5.0; 588 -5.0; 647 -5.2; 712 -5.6; 783 -5.5; 861 -6.1; 947 -6.5; 1042 -6.1; 1146 -5.6; 1261 -5.8; 1387 -6.2; 1526 -6.5; 1678 -6.8; 1846 -6.3; 2031 -5.6; 2234 -5.0; 2457 -4.7; 2703 -4.4; 2973 -3.9; 3270 -4.2; 3597 -4.2; 3957 -4.1; 4353 -4.3; 4788 -2.8; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C 2 Black Filters GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 2 Black Filters ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.98 | 2.2 dB  |
| Peaking | 50 Hz   | 0.47 | 3.4 dB  |
| Peaking | 158 Hz  | 5.2  | 2.2 dB  |
| Peaking | 3001 Hz | 1.67 | 2.1 dB  |
| Peaking | 5706 Hz | 2.85 | 6.4 dB  |
| Peaking | 339 Hz  | 1.18 | -1.0 dB |
| Peaking | 482 Hz  | 1.32 | 2.0 dB  |
| Peaking | 1697 Hz | 5.66 | -1.2 dB |
| Peaking | 3019 Hz | 0.34 | 0.1 dB  |
| Peaking | 8364 Hz | 3.95 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%202%20Black%20Filters/MrSpeakers%20Ether%20C%202%20Black%20Filters.png)