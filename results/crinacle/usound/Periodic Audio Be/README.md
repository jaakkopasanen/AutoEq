# Periodic Audio Be
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.7; 25 -6.1; 28 -6.5; 31 -6.9; 34 -7.1; 37 -7.3; 41 -7.6; 45 -7.8; 49 -7.9; 54 -8.1; 60 -8.3; 66 -8.5; 72 -8.7; 79 -8.9; 87 -9.1; 96 -9.3; 106 -9.4; 116 -9.5; 128 -9.5; 141 -9.5; 155 -9.4; 170 -9.2; 187 -9.0; 206 -8.7; 227 -8.3; 249 -7.9; 274 -7.4; 302 -6.9; 332 -6.4; 365 -5.9; 402 -5.4; 442 -4.9; 486 -4.4; 535 -3.9; 588 -3.3; 647 -2.8; 712 -2.2; 783 -1.7; 861 -1.2; 947 -1.0; 1042 -1.1; 1146 -1.5; 1261 -2.0; 1387 -2.6; 1526 -3.1; 1678 -3.8; 1846 -4.3; 2031 -4.1; 2234 -3.9; 2457 -3.6; 2703 -3.0; 2973 -2.0; 3270 -1.0; 3597 -0.5; 3957 -0.6; 4353 -1.6; 4788 -4.1; 5267 -7.4; 5793 -6.0; 6373 -2.2; 7010 -2.1; 7711 -4.4; 8482 -6.4; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -5.3; 15026 -10.3; 16529 -12.6; 18182 -12.5; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 0.52 | -2.5 dB |
| Peaking | 159 Hz   | 0.63 | -4.0 dB |
| Peaking | 907 Hz   | 1.2  | 4.0 dB  |
| Peaking | 3623 Hz  | 2.98 | 4.5 dB  |
| Peaking | 17594 Hz | 1.12 | -9.5 dB |
| Peaking | 1860 Hz  | 6.8  | -0.9 dB |
| Peaking | 5404 Hz  | 7.49 | -4.4 dB |
| Peaking | 6655 Hz  | 7.11 | 3.8 dB  |
| Peaking | 13196 Hz | 2.25 | 2.7 dB  |
| Peaking | 15230 Hz | 2.96 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)