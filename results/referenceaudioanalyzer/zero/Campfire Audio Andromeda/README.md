# Campfire Audio Andromeda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.7; 25 -13.7; 28 -13.7; 31 -13.7; 34 -13.7; 37 -13.7; 41 -13.7; 45 -13.7; 49 -13.7; 54 -13.7; 60 -13.7; 66 -13.7; 72 -13.7; 79 -13.6; 87 -13.4; 96 -13.4; 106 -13.2; 116 -13.0; 128 -12.8; 141 -12.7; 155 -12.7; 170 -12.7; 187 -12.7; 206 -12.7; 227 -12.8; 249 -12.9; 274 -12.6; 302 -12.1; 332 -11.6; 365 -11.1; 402 -10.6; 442 -10.1; 486 -9.5; 535 -9.0; 588 -8.4; 647 -7.8; 712 -7.3; 783 -6.7; 861 -6.2; 947 -5.7; 1042 -5.3; 1146 -4.9; 1261 -4.6; 1387 -4.6; 1526 -4.6; 1678 -4.9; 1846 -4.9; 2031 -4.7; 2234 -4.3; 2457 -3.4; 2703 -2.4; 2973 -1.6; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -1.4; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.18 | -7.2 dB |
| Peaking | 291 Hz  | 0.76 | -3.6 dB |
| Peaking | 1189 Hz | 1.27 | 2.0 dB  |
| Peaking | 3640 Hz | 1.39 | 5.9 dB  |
| Peaking | 5850 Hz | 3.46 | 4.6 dB  |
| Peaking | 6615 Hz | 8.2  | 1.8 dB  |
| Peaking | 7947 Hz | 2.36 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)