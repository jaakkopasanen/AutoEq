# Etymotic ER4P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.8; 31 -1.0; 34 -1.2; 37 -1.5; 41 -1.7; 45 -2.0; 49 -2.2; 54 -2.5; 60 -2.9; 66 -3.3; 72 -3.6; 79 -4.0; 87 -4.5; 96 -5.0; 106 -5.5; 116 -5.9; 128 -6.3; 141 -6.7; 155 -7.0; 170 -7.2; 187 -7.5; 206 -7.6; 227 -7.7; 249 -7.8; 274 -7.9; 302 -7.9; 332 -8.0; 365 -7.9; 402 -7.9; 442 -7.9; 486 -7.8; 535 -7.7; 588 -7.7; 647 -7.5; 712 -7.2; 783 -7.0; 861 -6.8; 947 -6.9; 1042 -7.3; 1146 -8.3; 1261 -9.4; 1387 -10.2; 1526 -10.4; 1678 -10.1; 1846 -9.7; 2031 -9.4; 2234 -9.2; 2457 -9.2; 2703 -9.0; 2973 -8.4; 3270 -7.6; 3597 -6.8; 3957 -5.8; 4353 -4.8; 4788 -3.4; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4P GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.67 | 5.5 dB  |
| Peaking | 57 Hz   | 0.82 | 2.2 dB  |
| Peaking | 250 Hz  | 0.7  | -1.7 dB |
| Peaking | 1834 Hz | 1.05 | -3.7 dB |
| Peaking | 5741 Hz | 2.67 | 6.8 dB  |
| Peaking | 950 Hz  | 3.7  | 1.1 dB  |
| Peaking | 1401 Hz | 3    | -1.6 dB |
| Peaking | 2582 Hz | 0.98 | 2.1 dB  |
| Peaking | 2805 Hz | 2    | -2.7 dB |
| Peaking | 8159 Hz | 3.88 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Etymotic%20ER4P/Etymotic%20ER4P.png)