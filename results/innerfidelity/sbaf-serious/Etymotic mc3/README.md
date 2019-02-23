# Etymotic mc3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.8; 31 -1.1; 34 -1.3; 37 -1.4; 41 -1.7; 45 -1.9; 49 -2.1; 54 -2.4; 60 -2.7; 66 -3.0; 72 -3.3; 79 -3.8; 87 -4.3; 96 -4.7; 106 -5.0; 116 -5.2; 128 -5.6; 141 -5.9; 155 -6.1; 170 -6.3; 187 -6.4; 206 -6.5; 227 -6.5; 249 -6.5; 274 -6.5; 302 -6.6; 332 -6.5; 365 -6.5; 402 -6.4; 442 -6.4; 486 -6.4; 535 -6.4; 588 -6.1; 647 -6.3; 712 -6.6; 783 -6.7; 861 -7.3; 947 -8.0; 1042 -8.8; 1146 -9.6; 1261 -10.4; 1387 -11.5; 1526 -12.4; 1678 -12.8; 1846 -12.1; 2031 -11.7; 2234 -10.9; 2457 -9.3; 2703 -7.9; 2973 -5.8; 3270 -4.1; 3597 -2.9; 3957 -3.0; 4353 -4.5; 4788 -4.6; 5267 -2.9; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic mc3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic mc3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.62 | 5.7 dB  |
| Peaking | 59 Hz   | 1.04 | 2.0 dB  |
| Peaking | 1739 Hz | 1.36 | -6.8 dB |
| Peaking | 3605 Hz | 2.79 | 4.8 dB  |
| Peaking | 6049 Hz | 3.66 | 6.0 dB  |
| Peaking | 215 Hz  | 1.52 | -0.3 dB |
| Peaking | 714 Hz  | 1.33 | 1.0 dB  |
| Peaking | 1138 Hz | 2.3  | -0.8 dB |
| Peaking | 6719 Hz | 8.92 | 1.4 dB  |
| Peaking | 7729 Hz | 2.9  | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20mc3/Etymotic%20mc3.png)