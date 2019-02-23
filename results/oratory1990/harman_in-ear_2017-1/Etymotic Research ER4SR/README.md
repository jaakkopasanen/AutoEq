# Etymotic Research ER4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.8; 54 -1.1; 60 -1.5; 66 -1.9; 72 -2.3; 79 -2.8; 87 -3.3; 96 -3.8; 106 -4.3; 116 -4.7; 128 -5.1; 141 -5.5; 155 -5.9; 170 -6.1; 187 -6.3; 206 -6.6; 227 -6.7; 249 -6.9; 274 -7.0; 302 -7.0; 332 -6.9; 365 -7.0; 402 -7.0; 442 -7.0; 486 -7.0; 535 -7.1; 588 -7.3; 647 -7.2; 712 -7.2; 783 -7.2; 861 -7.4; 947 -8.0; 1042 -8.6; 1146 -9.3; 1261 -9.8; 1387 -10.3; 1526 -10.5; 1678 -10.6; 1846 -10.5; 2031 -10.3; 2234 -10.0; 2457 -9.6; 2703 -8.9; 2973 -7.9; 3270 -7.1; 3597 -6.8; 3957 -6.6; 4353 -6.3; 4788 -5.6; 5267 -3.9; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.1; 15026 -25.8; 16529 -22.8; 18182 -9.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.54 | 6.6 dB   |
| Peaking | 1695 Hz  | 0.98 | -4.3 dB  |
| Peaking | 6128 Hz  | 2.73 | 6.9 dB   |
| Peaking | 12193 Hz | 2.2  | 7.7 dB   |
| Peaking | 15417 Hz | 1.77 | -23.4 dB |
| Peaking | 256 Hz   | 1.42 | -0.8 dB  |
| Peaking | 7495 Hz  | 6.79 | -0.8 dB  |
| Peaking | 9436 Hz  | 4.4  | 0.9 dB   |
| Peaking | 16549 Hz | 7.16 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.9 dB   |
| Peaking | 125 Hz   | 1.41 | 0.7 dB   |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 16000 Hz | 1.41 | -18.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20ER4SR/Etymotic%20Research%20ER4SR.png)