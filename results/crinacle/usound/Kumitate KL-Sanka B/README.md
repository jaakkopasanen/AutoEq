# Kumitate KL-Sanka B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.8; 25 -8.0; 28 -8.2; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.8; 49 -8.8; 54 -8.9; 60 -9.0; 66 -9.2; 72 -9.3; 79 -9.4; 87 -9.5; 96 -9.6; 106 -9.5; 116 -9.4; 128 -9.3; 141 -9.0; 155 -8.7; 170 -8.2; 187 -7.8; 206 -7.2; 227 -6.7; 249 -6.2; 274 -5.7; 302 -5.3; 332 -4.9; 365 -4.6; 402 -4.4; 442 -4.1; 486 -3.9; 535 -3.6; 588 -3.3; 647 -2.9; 712 -2.5; 783 -2.0; 861 -1.6; 947 -1.4; 1042 -1.5; 1146 -2.2; 1261 -2.8; 1387 -3.3; 1526 -3.3; 1678 -3.0; 1846 -3.0; 2031 -3.3; 2234 -3.9; 2457 -3.9; 2703 -2.8; 2973 -1.4; 3270 -0.6; 3597 -0.5; 3957 -1.2; 4353 -2.7; 4788 -3.9; 5267 -3.7; 5793 -3.6; 6373 -5.0; 7010 -10.0; 7711 -13.1; 8482 -15.4; 9330 -17.6; 10263 -14.2; 11289 -6.0; 12418 -5.2; 13660 -6.3; 15026 -10.3; 16529 -5.7; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sanka B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sanka B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.42 | -3.3 dB  |
| Peaking | 124 Hz   | 0.95 | -2.9 dB  |
| Peaking | 872 Hz   | 0.93 | 3.5 dB   |
| Peaking | 3732 Hz  | 1.38 | 4.7 dB   |
| Peaking | 9012 Hz  | 2.42 | -13.6 dB |
| Peaking | 6127 Hz  | 4.34 | 3.2 dB   |
| Peaking | 7277 Hz  | 7.34 | -2.4 dB  |
| Peaking | 8464 Hz  | 0.6  | -0.9 dB  |
| Peaking | 12037 Hz | 3.36 | 4.2 dB   |
| Peaking | 15014 Hz | 4.15 | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Sanka%20B/Kumitate%20KL-Sanka%20B.png)