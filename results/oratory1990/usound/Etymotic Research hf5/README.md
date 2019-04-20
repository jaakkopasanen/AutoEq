# Etymotic Research hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.2; 25 -1.2; 28 -1.3; 31 -1.4; 34 -1.5; 37 -1.5; 41 -1.7; 45 -1.8; 49 -2.0; 54 -2.2; 60 -2.5; 66 -2.9; 72 -3.3; 79 -3.7; 87 -4.2; 96 -4.5; 106 -5.3; 116 -5.4; 128 -5.9; 141 -6.4; 155 -6.6; 170 -6.8; 187 -7.0; 206 -7.2; 227 -7.3; 249 -7.4; 274 -7.4; 302 -7.5; 332 -7.5; 365 -7.5; 402 -7.5; 442 -7.5; 486 -7.6; 535 -7.5; 588 -7.5; 647 -7.3; 712 -7.2; 783 -7.1; 861 -7.2; 947 -7.5; 1042 -8.0; 1146 -8.6; 1261 -9.2; 1387 -9.4; 1526 -9.4; 1678 -9.0; 1846 -8.6; 2031 -8.2; 2234 -8.1; 2457 -8.0; 2703 -8.0; 2973 -7.7; 3270 -7.4; 3597 -6.8; 3957 -6.2; 4353 -5.3; 4788 -4.0; 5267 -2.3; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -8.1; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.58 | 4.3 dB  |
| Peaking | 55 Hz    | 0.67 | 2.9 dB  |
| Peaking | 231 Hz   | 0.57 | -1.4 dB |
| Peaking | 1633 Hz  | 0.89 | -2.8 dB |
| Peaking | 5877 Hz  | 3.1  | 6.7 dB  |
| Peaking | 902 Hz   | 1.83 | 1.5 dB  |
| Peaking | 1172 Hz  | 0.77 | -1.2 dB |
| Peaking | 1907 Hz  | 3    | 1.1 dB  |
| Peaking | 8099 Hz  | 6    | -1.0 dB |
| Peaking | 14841 Hz | 5.4  | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20Research%20hf5/Etymotic%20Research%20hf5.png)