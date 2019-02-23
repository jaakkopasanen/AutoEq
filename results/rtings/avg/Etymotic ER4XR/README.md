# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.9; 96 -1.7; 106 -2.6; 116 -3.4; 128 -4.2; 141 -4.9; 155 -5.5; 170 -6.0; 187 -6.3; 206 -6.6; 227 -6.8; 249 -6.8; 274 -6.8; 302 -6.7; 332 -6.7; 365 -6.6; 402 -6.5; 442 -6.4; 486 -6.2; 535 -6.0; 588 -5.7; 647 -5.3; 712 -5.0; 783 -4.9; 861 -5.0; 947 -5.5; 1042 -6.1; 1146 -6.8; 1261 -7.6; 1387 -8.3; 1526 -8.8; 1678 -9.3; 1846 -9.8; 2031 -10.1; 2234 -9.5; 2457 -8.6; 2703 -8.0; 2973 -8.0; 3270 -8.3; 3597 -9.0; 3957 -9.7; 4353 -10.2; 4788 -9.2; 5267 -7.1; 5793 -4.6; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.4; 15026 -13.0; 16529 -7.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.5  | 6.9 dB  |
| Peaking | 1924 Hz  | 2.26 | -3.6 dB |
| Peaking | 4340 Hz  | 2.3  | -4.0 dB |
| Peaking | 6381 Hz  | 3.49 | 4.7 dB  |
| Peaking | 15112 Hz | 3.76 | -7.2 dB |
| Peaking | 18 Hz    | 1.09 | 2.4 dB  |
| Peaking | 41 Hz    | 1    | -1.6 dB |
| Peaking | 85 Hz    | 1.67 | 2.0 dB  |
| Peaking | 202 Hz   | 0.97 | -1.4 dB |
| Peaking | 764 Hz   | 2.31 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -4.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Etymotic%20ER4XR/Etymotic%20ER4XR.png)