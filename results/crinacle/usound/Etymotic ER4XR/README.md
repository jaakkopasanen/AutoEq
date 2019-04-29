# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.1; 25 -1.3; 28 -1.6; 31 -1.8; 34 -2.0; 37 -2.1; 41 -2.3; 45 -2.5; 49 -2.7; 54 -2.9; 60 -3.2; 66 -3.5; 72 -3.8; 79 -4.1; 87 -4.5; 96 -4.9; 106 -5.3; 116 -5.6; 128 -5.9; 141 -6.1; 155 -6.4; 170 -6.5; 187 -6.7; 206 -6.7; 227 -6.7; 249 -6.7; 274 -6.7; 302 -6.6; 332 -6.6; 365 -6.4; 402 -6.3; 442 -6.3; 486 -6.2; 535 -6.2; 588 -6.0; 647 -5.8; 712 -5.6; 783 -5.3; 861 -5.1; 947 -5.2; 1042 -5.8; 1146 -6.9; 1261 -8.1; 1387 -8.9; 1526 -9.1; 1678 -8.9; 1846 -8.6; 2031 -8.5; 2234 -8.4; 2457 -8.4; 2703 -8.1; 2973 -7.6; 3270 -6.8; 3597 -6.0; 3957 -5.4; 4353 -4.8; 4788 -4.1; 5267 -2.9; 5793 -1.1; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.2; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -10.9; 16529 -9.7; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.93 | 4.8 dB  |
| Peaking | 55 Hz    | 1.55 | 2.1 dB  |
| Peaking | 1880 Hz  | 1.31 | -3.3 dB |
| Peaking | 5982 Hz  | 3.09 | 6.0 dB  |
| Peaking | 15604 Hz | 3.48 | -6.7 dB |
| Peaking | 182 Hz   | 2.48 | -0.7 dB |
| Peaking | 290 Hz   | 1.33 | -0.7 dB |
| Peaking | 916 Hz   | 2.11 | 1.6 dB  |
| Peaking | 1347 Hz  | 4.22 | -1.6 dB |
| Peaking | 4266 Hz  | 5.5  | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Etymotic%20ER4XR/Etymotic%20ER4XR.png)