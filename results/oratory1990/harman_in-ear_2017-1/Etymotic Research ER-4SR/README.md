# Etymotic Research ER-4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.9; 45 -1.2; 49 -1.5; 54 -1.8; 60 -2.1; 66 -2.5; 72 -2.8; 79 -3.2; 87 -3.7; 96 -4.3; 106 -4.7; 116 -5.1; 128 -5.5; 141 -6.0; 155 -6.3; 170 -6.5; 187 -6.7; 206 -6.8; 227 -7.0; 249 -7.1; 274 -7.1; 302 -7.1; 332 -7.0; 365 -7.0; 402 -7.0; 442 -7.1; 486 -7.2; 535 -7.1; 588 -7.0; 647 -7.0; 712 -6.9; 783 -7.0; 861 -7.2; 947 -7.7; 1042 -8.6; 1146 -9.3; 1261 -9.8; 1387 -9.9; 1526 -9.9; 1678 -9.8; 1846 -9.7; 2031 -9.6; 2234 -9.3; 2457 -8.9; 2703 -8.3; 2973 -7.4; 3270 -6.6; 3597 -6.2; 3957 -6.0; 4353 -6.0; 4788 -5.6; 5267 -4.2; 5793 -2.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -9.0; 11289 -8.2; 12418 -10.3; 13660 -18.6; 15026 -25.8; 16529 -20.7; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER-4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER-4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.32 | 6.2 dB   |
| Peaking | 183 Hz   | 0.7  | -1.4 dB  |
| Peaking | 1625 Hz  | 1.11 | -3.7 dB  |
| Peaking | 6200 Hz  | 2.48 | 6.3 dB   |
| Peaking | 15296 Hz | 2.12 | -21.7 dB |
| Peaking | 1676 Hz  | 5.05 | 0.3 dB   |
| Peaking | 9122 Hz  | 4.1  | 0.9 dB   |
| Peaking | 12070 Hz | 3.68 | 5.5 dB   |
| Peaking | 13118 Hz | 1.45 | -3.1 dB  |
| Peaking | 20381 Hz | 1.3  | 0.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.4 dB   |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -19.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20ER-4SR/Etymotic%20Research%20ER-4SR.png)