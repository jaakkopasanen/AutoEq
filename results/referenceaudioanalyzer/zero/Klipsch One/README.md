# Klipsch One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.6; 45 -2.4; 49 -3.0; 54 -3.7; 60 -4.3; 66 -4.7; 72 -5.0; 79 -5.1; 87 -5.3; 96 -5.6; 106 -5.8; 116 -6.0; 128 -6.2; 141 -6.4; 155 -6.5; 170 -6.3; 187 -6.1; 206 -6.1; 227 -6.0; 249 -5.8; 274 -5.8; 302 -5.8; 332 -5.8; 365 -5.6; 402 -5.2; 442 -4.8; 486 -4.1; 535 -3.1; 588 -2.2; 647 -1.8; 712 -2.0; 783 -2.8; 861 -3.9; 947 -4.7; 1042 -4.8; 1146 -5.2; 1261 -6.0; 1387 -6.4; 1526 -6.4; 1678 -6.7; 1846 -7.1; 2031 -7.5; 2234 -8.2; 2457 -9.4; 2703 -10.4; 2973 -10.7; 3270 -10.2; 3597 -8.8; 3957 -7.2; 4353 -5.8; 4788 -5.6; 5267 -7.2; 5793 -9.4; 6373 -11.7; 7010 -12.8; 7711 -11.7; 8482 -9.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 28 Hz   |  0.83 | 6.6 dB  |
| Peaking | 663 Hz  |  1.57 | 4.8 dB  |
| Peaking | 2956 Hz |  1.99 | -4.6 dB |
| Peaking | 4565 Hz |  3.24 | 3.0 dB  |
| Peaking | 6935 Hz |  2.84 | -6.8 dB |
| Peaking | 147 Hz  |  4.05 | -0.5 dB |
| Peaking | 1087 Hz | 10.82 | 0.4 dB  |
| Peaking | 8124 Hz |  5.47 | -1.7 dB |
| Peaking | 9245 Hz |  2.59 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Klipsch%20One/Klipsch%20One.png)