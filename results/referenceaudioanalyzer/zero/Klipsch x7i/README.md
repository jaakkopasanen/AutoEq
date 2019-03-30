# Klipsch x7i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.5; 28 -6.8; 31 -7.1; 34 -7.3; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.5; 54 -7.5; 60 -7.5; 66 -7.5; 72 -7.6; 79 -7.4; 87 -7.2; 96 -7.2; 106 -6.9; 116 -6.8; 128 -6.6; 141 -6.3; 155 -6.1; 170 -5.9; 187 -5.6; 206 -5.3; 227 -5.1; 249 -4.9; 274 -4.6; 302 -4.3; 332 -4.1; 365 -3.8; 402 -3.6; 442 -3.3; 486 -3.1; 535 -2.9; 588 -2.6; 647 -2.4; 712 -2.2; 783 -2.0; 861 -1.8; 947 -1.7; 1042 -1.5; 1146 -1.4; 1261 -1.4; 1387 -1.4; 1526 -1.4; 1678 -1.7; 1846 -2.0; 2031 -2.7; 2234 -3.4; 2457 -4.7; 2703 -6.7; 2973 -7.8; 3270 -7.0; 3597 -5.0; 3957 -3.2; 4353 -2.3; 4788 -2.5; 5267 -3.2; 5793 -3.0; 6373 -0.5; 7010 -0.7; 7711 -2.9; 8482 -3.2; 9330 -3.2; 10263 -3.6; 11289 -3.2; 12418 -3.2; 13660 -3.2; 15026 -3.2; 16529 -3.2; 18182 -3.2; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch x7i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch x7i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.46 | -1.3 dB |
| Peaking | 73 Hz    | 0.3  | -3.5 dB |
| Peaking | 1571 Hz  | 0.4  | 2.2 dB  |
| Peaking | 2943 Hz  | 2.63 | -6.6 dB |
| Peaking | 6652 Hz  | 8.87 | 3.9 dB  |
| Peaking | 1231 Hz  | 3.09 | 0.1 dB  |
| Peaking | 4367 Hz  | 3.91 | 2.3 dB  |
| Peaking | 4530 Hz  | 1.88 | -1.3 dB |
| Peaking | 10304 Hz | 4.44 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Klipsch%20x7i/Klipsch%20x7i.png)