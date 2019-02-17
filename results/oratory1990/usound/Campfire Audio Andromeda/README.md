# Campfire Audio Andromeda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.0; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.5; 41 -5.7; 45 -6.0; 49 -6.2; 54 -6.5; 60 -6.8; 66 -7.2; 72 -7.5; 79 -7.9; 87 -8.3; 96 -8.7; 106 -9.0; 116 -9.3; 128 -9.6; 141 -9.8; 155 -9.9; 170 -10.0; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.7; 274 -9.8; 302 -9.8; 332 -9.6; 365 -9.4; 402 -9.0; 442 -8.7; 486 -8.4; 535 -8.0; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.1; 861 -5.8; 947 -5.7; 1042 -5.7; 1146 -5.9; 1261 -6.2; 1387 -6.3; 1526 -6.3; 1678 -6.0; 1846 -5.2; 2031 -4.2; 2234 -2.9; 2457 -1.7; 2703 -1.0; 2973 -0.9; 3270 -0.8; 3597 -0.5; 3957 -1.8; 4353 -4.0; 4788 -3.5; 5267 -2.7; 5793 -5.0; 6373 -6.3; 7010 -3.9; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -6.6; 15026 -8.2; 16529 -5.8; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  1.06 | 2.3 dB  |
| Peaking | 123 Hz   |  0.8  | -2.7 dB |
| Peaking | 300 Hz   |  0.66 | -3.5 dB |
| Peaking | 3176 Hz  |  1.55 | 5.5 dB  |
| Peaking | 14781 Hz |  3.7  | -2.9 dB |
| Peaking | 980 Hz   |  1.47 | 2.0 dB  |
| Peaking | 1394 Hz  |  0.81 | -1.9 dB |
| Peaking | 2353 Hz  |  3.18 | 1.7 dB  |
| Peaking | 5296 Hz  |  8.08 | 2.0 dB  |
| Peaking | 6105 Hz  | 12.01 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)