# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.3; 25 -2.4; 28 -2.5; 31 -2.7; 34 -2.8; 37 -2.8; 41 -2.9; 45 -3.1; 49 -3.2; 54 -3.4; 60 -3.7; 66 -3.9; 72 -4.2; 79 -4.5; 87 -4.8; 96 -5.1; 106 -5.3; 116 -5.4; 128 -5.6; 141 -5.8; 155 -5.9; 170 -5.9; 187 -5.9; 206 -6.0; 227 -5.8; 249 -5.8; 274 -5.7; 302 -5.5; 332 -5.4; 365 -5.3; 402 -5.2; 442 -4.9; 486 -4.8; 535 -4.8; 588 -4.5; 647 -4.6; 712 -4.7; 783 -4.7; 861 -5.1; 947 -5.6; 1042 -6.3; 1146 -6.9; 1261 -7.6; 1387 -8.4; 1526 -9.4; 1678 -9.9; 1846 -10.1; 2031 -10.1; 2234 -9.8; 2457 -8.7; 2703 -7.4; 2973 -5.3; 3270 -3.1; 3597 -2.1; 3957 -2.6; 4353 -4.4; 4788 -4.5; 5267 -2.6; 5793 -0.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.44 | 3.7 dB  |
| Peaking | 53 Hz   | 1.21 | 1.0 dB  |
| Peaking | 1967 Hz | 1.76 | -5.0 dB |
| Peaking | 3560 Hz | 3.32 | 4.7 dB  |
| Peaking | 6066 Hz | 3.86 | 6.1 dB  |
| Peaking | 670 Hz  | 1.12 | 1.8 dB  |
| Peaking | 1456 Hz | 2.08 | -1.3 dB |
| Peaking | 1960 Hz | 4.15 | 1.1 dB  |
| Peaking | 2350 Hz | 4.05 | -0.7 dB |
| Peaking | 8095 Hz | 5.33 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4XR/Etymotic%20ER4XR.png)