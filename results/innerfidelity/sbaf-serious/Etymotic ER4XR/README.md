# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.9; 25 -3.0; 28 -3.2; 31 -3.3; 34 -3.4; 37 -3.5; 41 -3.6; 45 -3.7; 49 -3.9; 54 -4.1; 60 -4.3; 66 -4.6; 72 -4.8; 79 -5.1; 87 -5.5; 96 -5.8; 106 -6.0; 116 -6.1; 128 -6.3; 141 -6.5; 155 -6.6; 170 -6.6; 187 -6.6; 206 -6.6; 227 -6.5; 249 -6.5; 274 -6.4; 302 -6.2; 332 -6.1; 365 -5.9; 402 -5.8; 442 -5.6; 486 -5.5; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.3; 783 -5.3; 861 -5.8; 947 -6.3; 1042 -7.0; 1146 -7.6; 1261 -8.3; 1387 -9.1; 1526 -10.0; 1678 -10.6; 1846 -10.8; 2031 -10.7; 2234 -10.5; 2457 -9.4; 2703 -8.0; 2973 -5.9; 3270 -3.8; 3597 -2.8; 3957 -3.3; 4353 -5.0; 4788 -5.2; 5267 -3.3; 5793 -1.4; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.9; 16529 -5.9; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.22 | 3.0 dB  |
| Peaking | 48 Hz   | 1.9  | 1.6 dB  |
| Peaking | 1950 Hz | 1.42 | -5.7 dB |
| Peaking | 3532 Hz | 3.46 | 4.5 dB  |
| Peaking | 6161 Hz | 4.01 | 5.8 dB  |
| Peaking | 192 Hz  | 1.09 | -0.9 dB |
| Peaking | 694 Hz  | 1.17 | 1.2 dB  |
| Peaking | 1313 Hz | 2.6  | -0.9 dB |
| Peaking | 8027 Hz | 5.49 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4XR/Etymotic%20ER4XR.png)