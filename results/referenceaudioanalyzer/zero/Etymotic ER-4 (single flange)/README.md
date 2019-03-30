# Etymotic ER-4 (single flange)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.4; 25 -3.7; 28 -4.0; 31 -4.2; 34 -4.4; 37 -4.5; 41 -4.7; 45 -4.9; 49 -5.1; 54 -5.3; 60 -5.4; 66 -5.3; 72 -5.3; 79 -5.3; 87 -5.3; 96 -5.3; 106 -5.3; 116 -5.3; 128 -5.3; 141 -5.3; 155 -5.4; 170 -5.3; 187 -5.0; 206 -5.0; 227 -5.2; 249 -5.8; 274 -6.3; 302 -6.1; 332 -6.0; 365 -6.0; 402 -5.8; 442 -5.7; 486 -5.7; 535 -5.7; 588 -5.8; 647 -6.0; 712 -6.0; 783 -6.0; 861 -6.0; 947 -6.0; 1042 -6.2; 1146 -6.4; 1261 -6.6; 1387 -7.0; 1526 -7.4; 1678 -7.9; 1846 -8.6; 2031 -9.3; 2234 -9.8; 2457 -10.2; 2703 -9.9; 2973 -9.0; 3270 -7.7; 3597 -6.4; 3957 -6.1; 4353 -6.7; 4788 -6.8; 5267 -5.6; 5793 -3.3; 6373 -0.5; 7010 -2.7; 7711 -4.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-4 (single flange) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4 (single flange) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.55 | 2.0 dB  |
| Peaking | 295 Hz  | 3.46 | -0.9 dB |
| Peaking | 2043 Hz | 0.28 | -0.8 dB |
| Peaking | 2388 Hz | 1.65 | -4.3 dB |
| Peaking | 6449 Hz | 5.07 | 5.8 dB  |
| Peaking | 123 Hz  | 0.45 | -0.2 dB |
| Peaking | 203 Hz  | 3.74 | 0.6 dB  |
| Peaking | 3009 Hz | 3.65 | -1.1 dB |
| Peaking | 3877 Hz | 1.77 | 1.5 dB  |
| Peaking | 4582 Hz | 4.23 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Etymotic%20ER-4%20(single%20flange)/Etymotic%20ER-4%20(single%20flange).png)