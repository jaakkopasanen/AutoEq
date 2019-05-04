# Etymotic Research hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.5; 25 -2.5; 28 -2.6; 31 -2.6; 34 -2.7; 37 -2.8; 41 -2.9; 45 -3.1; 49 -3.3; 54 -3.5; 60 -3.8; 66 -4.2; 72 -4.5; 79 -4.9; 87 -5.4; 96 -5.8; 106 -6.5; 116 -6.7; 128 -7.1; 141 -7.7; 155 -7.9; 170 -8.1; 187 -8.3; 206 -8.4; 227 -8.6; 249 -8.7; 274 -8.7; 302 -8.7; 332 -8.6; 365 -8.5; 402 -8.4; 442 -8.5; 486 -8.5; 535 -8.4; 588 -8.2; 647 -8.1; 712 -8.0; 783 -7.9; 861 -8.0; 947 -8.4; 1042 -8.9; 1146 -9.5; 1261 -9.8; 1387 -9.7; 1526 -9.4; 1678 -9.0; 1846 -8.5; 2031 -7.8; 2234 -7.0; 2457 -6.4; 2703 -6.0; 2973 -5.6; 3270 -5.2; 3597 -5.0; 3957 -4.7; 4353 -4.2; 4788 -3.3; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.8; 15026 -24.6; 16529 -22.1; 18182 -10.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.49 | 4.2 dB   |
| Peaking | 66 Hz    | 0.92 | 2.1 dB   |
| Peaking | 403 Hz   | 0.11 | -2.4 dB  |
| Peaking | 5649 Hz  | 1.19 | 6.2 dB   |
| Peaking | 15713 Hz | 2.24 | -21.3 dB |
| Peaking | 1413 Hz  | 3.11 | -1.6 dB  |
| Peaking | 2707 Hz  | 3    | 1.1 dB   |
| Peaking | 7842 Hz  | 5.23 | -2.3 dB  |
| Peaking | 12716 Hz | 2.63 | 5.7 dB   |
| Peaking | 14376 Hz | 4.13 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -17.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20hf5/Etymotic%20Research%20hf5.png)