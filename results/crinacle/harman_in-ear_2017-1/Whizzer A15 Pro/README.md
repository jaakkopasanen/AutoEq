# Whizzer A15 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.7; 54 -1.0; 60 -1.3; 66 -1.8; 72 -2.2; 79 -2.6; 87 -3.0; 96 -3.5; 106 -4.1; 116 -4.6; 128 -5.1; 141 -5.5; 155 -5.9; 170 -6.2; 187 -6.5; 206 -6.8; 227 -7.0; 249 -7.2; 274 -7.4; 302 -7.4; 332 -7.4; 365 -7.3; 402 -7.3; 442 -7.1; 486 -7.1; 535 -7.1; 588 -7.1; 647 -7.1; 712 -6.9; 783 -6.7; 861 -6.5; 947 -6.6; 1042 -6.9; 1146 -7.6; 1261 -8.3; 1387 -8.6; 1526 -8.6; 1678 -8.3; 1846 -7.9; 2031 -7.5; 2234 -6.9; 2457 -6.6; 2703 -6.5; 2973 -6.4; 3270 -6.3; 3597 -6.1; 3957 -6.3; 4353 -6.8; 4788 -7.0; 5267 -6.3; 5793 -4.4; 6373 -2.4; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -16.2; 15026 -27.6; 16529 -30.4; 18182 -28.5; 20000 -23.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Whizzer A15 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Whizzer A15 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.55 | 6.7 dB   |
| Peaking | 1448 Hz  | 3.5  | -1.6 dB  |
| Peaking | 7080 Hz  | 0.42 | 16.9 dB  |
| Peaking | 12421 Hz | 1.56 | 17.7 dB  |
| Peaking | 15511 Hz | 0.29 | -35.3 dB |
| Peaking | 84 Hz    | 1.99 | 0.8 dB   |
| Peaking | 270 Hz   | 1.06 | -1.2 dB  |
| Peaking | 5123 Hz  | 2.41 | -5.2 dB  |
| Peaking | 6351 Hz  | 1.23 | 5.4 dB   |
| Peaking | 7773 Hz  | 2.67 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB   |
| Peaking | 62 Hz    | 1.41 | 4.1 dB   |
| Peaking | 125 Hz   | 1.41 | 0.9 dB   |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 16000 Hz | 1.41 | -29.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Whizzer%20A15%20Pro/Whizzer%20A15%20Pro.png)