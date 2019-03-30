# Etymotic ER-4 (triple flange)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -0.6; 25 -0.5; 28 -0.5; 31 -0.7; 34 -0.9; 37 -1.1; 41 -1.3; 45 -1.4; 49 -1.5; 54 -1.7; 60 -1.8; 66 -1.8; 72 -1.9; 79 -2.1; 87 -2.1; 96 -2.1; 106 -2.1; 116 -2.1; 128 -2.3; 141 -2.4; 155 -2.4; 170 -2.4; 187 -2.4; 206 -2.4; 227 -2.4; 249 -2.4; 274 -2.4; 302 -2.4; 332 -2.4; 365 -2.7; 402 -2.7; 442 -2.7; 486 -2.7; 535 -2.8; 588 -3.1; 647 -3.0; 712 -3.2; 783 -3.4; 861 -3.5; 947 -3.7; 1042 -4.0; 1146 -4.2; 1261 -4.6; 1387 -5.1; 1526 -5.7; 1678 -6.6; 1846 -7.7; 2031 -9.0; 2234 -10.1; 2457 -10.8; 2703 -10.5; 2973 -9.8; 3270 -9.1; 3597 -8.9; 3957 -8.9; 4353 -8.7; 4788 -8.0; 5267 -6.8; 5793 -5.2; 6373 -3.3; 7010 -1.8; 7711 -3.6; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-4 (triple flange) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4 (triple flange) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.68 | 2.8 dB  |
| Peaking | 238 Hz   | 0.13 | 1.6 dB  |
| Peaking | 1473 Hz  | 0.9  | 3.4 dB  |
| Peaking | 2403 Hz  | 0.64 | -8.8 dB |
| Peaking | 6878 Hz  | 3.38 | 3.9 dB  |
| Peaking | 2389 Hz  | 4.47 | -0.9 dB |
| Peaking | 2750 Hz  | 4.15 | -0.6 dB |
| Peaking | 3160 Hz  | 1.7  | 1.5 dB  |
| Peaking | 4384 Hz  | 2.57 | -1.3 dB |
| Peaking | 10690 Hz | 1.52 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Etymotic%20ER-4%20(triple%20flange)/Etymotic%20ER-4%20(triple%20flange).png)