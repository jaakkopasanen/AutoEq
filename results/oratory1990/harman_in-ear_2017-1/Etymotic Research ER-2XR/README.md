# Etymotic Research ER-2XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.3; 25 -7.3; 28 -7.3; 31 -7.3; 34 -7.3; 37 -7.2; 41 -7.2; 45 -7.2; 49 -7.2; 54 -7.2; 60 -7.3; 66 -7.3; 72 -7.5; 79 -7.6; 87 -7.8; 96 -7.9; 106 -8.1; 116 -8.2; 128 -8.3; 141 -8.4; 155 -8.4; 170 -8.4; 187 -8.3; 206 -8.2; 227 -8.1; 249 -8.0; 274 -7.8; 302 -7.6; 332 -7.3; 365 -7.1; 402 -6.9; 442 -6.7; 486 -6.5; 535 -6.2; 588 -6.0; 647 -5.7; 712 -5.4; 783 -5.1; 861 -4.8; 947 -4.9; 1042 -5.5; 1146 -6.7; 1261 -8.1; 1387 -8.9; 1526 -9.0; 1678 -8.8; 1846 -8.5; 2031 -7.9; 2234 -7.3; 2457 -6.7; 2703 -6.0; 2973 -5.0; 3270 -4.2; 3597 -3.5; 3957 -3.0; 4353 -2.7; 4788 -2.4; 5267 -2.0; 5793 -1.3; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.7; 9330 -5.8; 10263 -9.2; 11289 -11.8; 12418 -12.2; 13660 -16.4; 15026 -24.4; 16529 -29.2; 18182 -28.5; 20000 -25.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER-2XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER-2XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.28 | -1.6 dB  |
| Peaking | 178 Hz   | 0.51 | -2.7 dB  |
| Peaking | 1858 Hz  | 0.87 | -8.2 dB  |
| Peaking | 7455 Hz  | 0.23 | 19.1 dB  |
| Peaking | 16938 Hz | 0.25 | -34.0 dB |
| Peaking | 935 Hz   | 3.24 | 1.3 dB   |
| Peaking | 1338 Hz  | 5.41 | -1.4 dB  |
| Peaking | 6412 Hz  | 6.12 | 2.5 dB   |
| Peaking | 7546 Hz  | 5.17 | -2.0 dB  |
| Peaking | 12982 Hz | 6.85 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 16000 Hz | 1.41 | -32.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20ER-2XR/Etymotic%20Research%20ER-2XR.png)