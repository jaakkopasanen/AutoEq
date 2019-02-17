# Etymotic hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.8; 54 -1.0; 60 -1.3; 66 -1.7; 72 -2.0; 79 -2.4; 87 -2.9; 96 -3.2; 106 -4.1; 116 -4.1; 128 -4.6; 141 -5.1; 155 -5.4; 170 -5.6; 187 -5.8; 206 -5.9; 227 -6.1; 249 -6.1; 274 -6.2; 302 -6.2; 332 -6.2; 365 -6.2; 402 -6.2; 442 -6.3; 486 -6.3; 535 -6.3; 588 -6.2; 647 -6.1; 712 -6.0; 783 -5.9; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -7.4; 1261 -7.9; 1387 -8.2; 1526 -8.1; 1678 -7.8; 1846 -7.3; 2031 -7.0; 2234 -6.8; 2457 -6.8; 2703 -6.7; 2973 -6.5; 3270 -6.1; 3597 -5.6; 3957 -4.9; 4353 -4.0; 4788 -2.7; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.44 | 6.4 dB  |
| Peaking | 868 Hz  | 1.94 | 1.2 dB  |
| Peaking | 1384 Hz | 1.48 | -2.0 dB |
| Peaking | 5645 Hz | 2.54 | 6.6 dB  |
| Peaking | 6584 Hz | 7.51 | 2.1 dB  |
| Peaking | 7764 Hz | 2.39 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20hf5/Etymotic%20hf5.png)