# Acoustune HS1503
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.3; 25 -13.3; 28 -13.2; 31 -13.1; 34 -13.0; 37 -12.9; 41 -12.8; 45 -12.7; 49 -12.5; 54 -12.4; 60 -12.3; 66 -12.2; 72 -12.1; 79 -12.0; 87 -12.0; 96 -12.0; 106 -11.9; 116 -11.7; 128 -11.6; 141 -11.3; 155 -11.1; 170 -10.8; 187 -10.4; 206 -9.9; 227 -9.4; 249 -8.9; 274 -8.4; 302 -7.8; 332 -7.1; 365 -6.4; 402 -5.9; 442 -5.4; 486 -4.8; 535 -4.3; 588 -3.8; 647 -3.3; 712 -2.7; 783 -2.2; 861 -1.9; 947 -1.8; 1042 -2.0; 1146 -2.5; 1261 -2.8; 1387 -2.7; 1526 -2.3; 1678 -1.8; 1846 -1.3; 2031 -0.8; 2234 -0.5; 2457 -0.9; 2703 -2.1; 2973 -4.0; 3270 -5.6; 3597 -5.7; 3957 -5.2; 4353 -5.6; 4788 -7.0; 5267 -10.6; 5793 -13.4; 6373 -9.0; 7010 -6.2; 7711 -8.6; 8482 -10.0; 9330 -6.9; 10263 -6.0; 11289 -6.0; 12418 -9.1; 13660 -16.3; 15026 -21.1; 16529 -24.2; 18182 -24.0; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1503 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1503 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.25 | -7.0 dB  |
| Peaking | 173 Hz   | 0.46 | -5.1 dB  |
| Peaking | 2726 Hz  | 0.1  | 5.0 dB   |
| Peaking | 5598 Hz  | 2.46 | -9.2 dB  |
| Peaking | 17292 Hz | 0.7  | -22.3 dB |
| Peaking | 2324 Hz  | 4.06 | 1.9 dB   |
| Peaking | 3329 Hz  | 3.85 | -3.3 dB  |
| Peaking | 8461 Hz  | 4.85 | -5.5 dB  |
| Peaking | 11927 Hz | 1.04 | 6.4 dB   |
| Peaking | 14188 Hz | 1.9  | -7.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -21.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1503/Acoustune%20HS1503.png)