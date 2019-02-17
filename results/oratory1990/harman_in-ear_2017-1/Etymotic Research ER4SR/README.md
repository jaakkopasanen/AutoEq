# Etymotic Research ER4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.0; 87 -1.5; 96 -2.0; 106 -2.5; 116 -2.9; 128 -3.3; 141 -3.7; 155 -4.1; 170 -4.3; 187 -4.5; 206 -4.8; 227 -4.9; 249 -5.1; 274 -5.2; 302 -5.2; 332 -5.1; 365 -5.2; 402 -5.2; 442 -5.2; 486 -5.2; 535 -5.3; 588 -5.4; 647 -5.4; 712 -5.4; 783 -5.3; 861 -5.6; 947 -6.1; 1042 -6.8; 1146 -7.5; 1261 -8.0; 1387 -8.5; 1526 -8.7; 1678 -8.8; 1846 -8.7; 2031 -8.5; 2234 -8.1; 2457 -7.8; 2703 -7.1; 2973 -6.1; 3270 -5.3; 3597 -4.9; 3957 -4.8; 4353 -4.5; 4788 -3.8; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.3; 15026 -24.0; 16529 -21.0; 18182 -8.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.33 | 6.4 dB   |
| Peaking | 750 Hz   | 0.73 | 1.5 dB   |
| Peaking | 1594 Hz  | 1.22 | -3.3 dB  |
| Peaking | 5812 Hz  | 1.86 | 6.2 dB   |
| Peaking | 15653 Hz | 2.61 | -20.7 dB |
| Peaking | 3464 Hz  | 4.67 | 1.0 dB   |
| Peaking | 4798 Hz  | 5.99 | -0.7 dB  |
| Peaking | 7789 Hz  | 5.78 | -1.8 dB  |
| Peaking | 12976 Hz | 2.47 | 5.4 dB   |
| Peaking | 14463 Hz | 4.21 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 5.1 dB   |
| Peaking | 125 Hz   | 1.41 | 2.3 dB   |
| Peaking | 250 Hz   | 1.41 | 0.6 dB   |
| Peaking | 500 Hz   | 1.41 | 1.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -16.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20ER4SR/Etymotic%20Research%20ER4SR.png)