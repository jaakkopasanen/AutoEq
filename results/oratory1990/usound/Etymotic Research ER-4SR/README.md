# Etymotic Research ER-4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.0; 66 -1.3; 72 -1.7; 79 -2.1; 87 -2.6; 96 -3.1; 106 -3.6; 116 -4.0; 128 -4.4; 141 -4.8; 155 -5.1; 170 -5.4; 187 -5.5; 206 -5.7; 227 -5.8; 249 -5.9; 274 -6.0; 302 -6.0; 332 -6.1; 365 -6.1; 402 -6.1; 442 -6.3; 486 -6.4; 535 -6.4; 588 -6.3; 647 -6.3; 712 -6.3; 783 -6.3; 861 -6.5; 947 -7.0; 1042 -7.8; 1146 -8.6; 1261 -9.3; 1387 -9.8; 1526 -10.0; 1678 -9.9; 1846 -9.9; 2031 -10.1; 2234 -10.4; 2457 -10.6; 2703 -10.4; 2973 -9.7; 3270 -8.9; 3597 -8.1; 3957 -7.6; 4353 -7.1; 4788 -6.4; 5267 -5.0; 5793 -3.1; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.7; 11289 -6.8; 12418 -7.7; 13660 -9.7; 15026 -9.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER-4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER-4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.41 | 6.5 dB  |
| Peaking | 1428 Hz  | 2.46 | -2.5 dB |
| Peaking | 2478 Hz  | 1.4  | -4.0 dB |
| Peaking | 6327 Hz  | 3.86 | 5.6 dB  |
| Peaking | 14312 Hz | 2.89 | -4.0 dB |
| Peaking | 38 Hz    | 3.05 | -0.2 dB |
| Peaking | 771 Hz   | 3.57 | 0.7 dB  |
| Peaking | 5471 Hz  | 6.74 | 0.7 dB  |
| Peaking | 7743 Hz  | 5.32 | -0.8 dB |
| Peaking | 16435 Hz | 4.87 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20Research%20ER-4SR/Etymotic%20Research%20ER-4SR.png)