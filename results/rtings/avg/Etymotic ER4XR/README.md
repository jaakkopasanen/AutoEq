# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.9; 87 -1.6; 96 -2.4; 106 -3.3; 116 -4.1; 128 -4.9; 141 -5.6; 155 -6.2; 170 -6.6; 187 -7.0; 206 -7.3; 227 -7.5; 249 -7.5; 274 -7.5; 302 -7.4; 332 -7.4; 365 -7.3; 402 -7.2; 442 -7.1; 486 -6.9; 535 -6.7; 588 -6.4; 647 -6.0; 712 -5.7; 783 -5.6; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.5; 1261 -8.3; 1387 -9.0; 1526 -9.5; 1678 -10.0; 1846 -10.5; 2031 -10.8; 2234 -10.2; 2457 -9.3; 2703 -8.7; 2973 -8.7; 3270 -9.0; 3597 -9.7; 3957 -10.4; 4353 -10.9; 4788 -9.9; 5267 -7.8; 5793 -5.3; 6373 -3.8; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.0; 15026 -13.7; 16529 -7.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.59 | 7.0 dB  |
| Peaking | 1897 Hz  | 1.74 | -4.1 dB |
| Peaking | 4357 Hz  | 2.09 | -4.6 dB |
| Peaking | 6418 Hz  | 3.15 | 4.3 dB  |
| Peaking | 15132 Hz | 3.61 | -7.9 dB |
| Peaking | 19 Hz    | 1.26 | 2.6 dB  |
| Peaking | 43 Hz    | 1.05 | -1.9 dB |
| Peaking | 79 Hz    | 1.2  | 2.6 dB  |
| Peaking | 210 Hz   | 0.67 | -1.9 dB |
| Peaking | 785 Hz   | 2.5  | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Etymotic%20ER4XR/Etymotic%20ER4XR.png)