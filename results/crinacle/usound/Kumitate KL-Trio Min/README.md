# Kumitate KL-Trio Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.2; 25 -10.1; 28 -10.0; 31 -10.0; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.2; 49 -10.2; 54 -10.3; 60 -10.4; 66 -10.5; 72 -10.6; 79 -10.6; 87 -10.7; 96 -11.0; 106 -11.1; 116 -11.0; 128 -10.9; 141 -10.9; 155 -11.0; 170 -10.6; 187 -10.3; 206 -10.0; 227 -9.5; 249 -9.0; 274 -8.5; 302 -8.0; 332 -7.5; 365 -6.9; 402 -6.4; 442 -5.9; 486 -5.4; 535 -4.9; 588 -4.5; 647 -4.0; 712 -3.6; 783 -3.3; 861 -3.2; 947 -3.4; 1042 -4.1; 1146 -5.2; 1261 -6.7; 1387 -8.7; 1526 -10.3; 1678 -8.8; 1846 -5.9; 2031 -4.2; 2234 -4.9; 2457 -6.7; 2703 -6.7; 2973 -4.5; 3270 -2.8; 3597 -2.2; 3957 -1.7; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -2.8; 7010 -8.6; 7711 -13.8; 8482 -12.5; 9330 -9.6; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -13.9; 20000 -17.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Trio Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Trio Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.22 | -3.5 dB  |
| Peaking | 150 Hz  | 0.83 | -3.0 dB  |
| Peaking | 728 Hz  | 1.81 | 3.7 dB   |
| Peaking | 5350 Hz | 1.33 | 8.5 dB   |
| Peaking | 7784 Hz | 2.8  | -11.4 dB |
| Peaking | 1023 Hz | 3.47 | 1.8 dB   |
| Peaking | 1545 Hz | 3.35 | -5.3 dB  |
| Peaking | 2054 Hz | 3.41 | 3.1 dB   |
| Peaking | 2619 Hz | 3.96 | -3.0 dB  |
| Peaking | 3299 Hz | 3.23 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Trio%20Min/Kumitate%20KL-Trio%20Min.png)