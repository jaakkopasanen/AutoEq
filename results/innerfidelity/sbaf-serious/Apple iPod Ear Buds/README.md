# Apple iPod Ear Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -1.5; 170 -3.0; 187 -4.3; 206 -5.5; 227 -6.4; 249 -7.2; 274 -7.7; 302 -7.9; 332 -7.9; 365 -7.8; 402 -7.4; 442 -6.8; 486 -6.6; 535 -6.5; 588 -6.3; 647 -6.6; 712 -6.8; 783 -6.6; 861 -6.7; 947 -6.7; 1042 -6.7; 1146 -6.6; 1261 -6.7; 1387 -7.1; 1526 -7.6; 1678 -7.9; 1846 -7.7; 2031 -6.8; 2234 -5.7; 2457 -6.4; 2703 -9.2; 2973 -11.8; 3270 -10.8; 3597 -7.8; 3957 -6.7; 4353 -7.7; 4788 -7.9; 5267 -7.1; 5793 -9.3; 6373 -12.3; 7010 -10.2; 7711 -9.1; 8482 -9.9; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple iPod Ear Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 62 Hz   |  0.2  | 6.6 dB  |
| Peaking | 232 Hz  |  2.73 | -2.4 dB |
| Peaking | 328 Hz  |  1.16 | -4.1 dB |
| Peaking | 3034 Hz |  5.48 | -5.7 dB |
| Peaking | 6677 Hz |  2.55 | -5.0 dB |
| Peaking | 17 Hz   |  1.67 | 1.2 dB  |
| Peaking | 140 Hz  |  5.89 | 1.3 dB  |
| Peaking | 1704 Hz |  2.22 | -1.4 dB |
| Peaking | 2279 Hz |  6.14 | 2.2 dB  |
| Peaking | 8670 Hz | 10.13 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds/Apple%20iPod%20Ear%20Buds.png)