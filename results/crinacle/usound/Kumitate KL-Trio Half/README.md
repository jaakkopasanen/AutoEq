# Kumitate KL-Trio Half
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.2; 28 -7.2; 31 -7.3; 34 -7.3; 37 -7.4; 41 -7.4; 45 -7.5; 49 -7.5; 54 -7.6; 60 -7.7; 66 -7.8; 72 -7.9; 79 -8.0; 87 -8.1; 96 -8.4; 106 -8.7; 116 -8.5; 128 -8.5; 141 -8.4; 155 -8.2; 170 -8.0; 187 -7.6; 206 -7.3; 227 -6.8; 249 -6.3; 274 -5.9; 302 -5.4; 332 -4.8; 365 -4.2; 402 -3.7; 442 -3.2; 486 -2.7; 535 -2.2; 588 -1.8; 647 -1.3; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.6; 1042 -1.3; 1146 -2.8; 1261 -4.9; 1387 -7.6; 1526 -9.6; 1678 -9.2; 1846 -7.8; 2031 -7.3; 2234 -8.7; 2457 -10.5; 2703 -10.4; 2973 -8.0; 3270 -5.9; 3597 -5.0; 3957 -4.7; 4353 -4.2; 4788 -3.8; 5267 -4.2; 5793 -5.5; 6373 -7.7; 7010 -13.9; 7711 -19.0; 8482 -17.4; 9330 -14.7; 10263 -12.8; 11289 -9.7; 12418 -7.1; 13660 -6.5; 15026 -6.5; 16529 -10.9; 18182 -18.2; 20000 -24.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Trio Half GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Trio Half ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1524 Hz  | 2.85 | -8.2 dB  |
| Peaking | 2640 Hz  | 1.11 | -14.2 dB |
| Peaking | 3961 Hz  | 0.11 | 15.8 dB  |
| Peaking | 5096 Hz  | 0.11 | 37.1 dB  |
| Peaking | 7901 Hz  | 0.16 | -60.3 dB |
| Peaking | 61 Hz    | 2.03 | 0.8 dB   |
| Peaking | 4285 Hz  | 3.31 | -2.7 dB  |
| Peaking | 4315 Hz  | 1.51 | 1.4 dB   |
| Peaking | 10029 Hz | 4.24 | -2.2 dB  |
| Peaking | 14018 Hz | 2.15 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 3.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Trio%20Half/Kumitate%20KL-Trio%20Half.png)