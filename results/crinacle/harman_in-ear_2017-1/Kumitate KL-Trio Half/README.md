# Kumitate KL-Trio Half
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.7; 25 -7.8; 28 -7.8; 31 -7.8; 34 -7.9; 37 -7.9; 41 -8.0; 45 -8.0; 49 -8.1; 54 -8.2; 60 -8.2; 66 -8.3; 72 -8.4; 79 -8.6; 87 -8.7; 96 -9.0; 106 -9.2; 116 -9.1; 128 -9.1; 141 -9.0; 155 -8.8; 170 -8.5; 187 -8.2; 206 -7.8; 227 -7.4; 249 -6.9; 274 -6.4; 302 -5.9; 332 -5.2; 365 -4.5; 402 -4.0; 442 -3.5; 486 -2.9; 535 -2.3; 588 -1.8; 647 -1.4; 712 -0.9; 783 -0.6; 861 -0.5; 947 -0.8; 1042 -1.6; 1146 -2.9; 1261 -4.8; 1387 -7.2; 1526 -8.9; 1678 -8.5; 1846 -7.0; 2031 -6.1; 2234 -6.9; 2457 -8.2; 2703 -7.8; 2973 -5.1; 3270 -3.1; 3597 -2.4; 3957 -2.5; 4353 -2.4; 4788 -2.3; 5267 -2.7; 5793 -3.8; 6373 -5.6; 7010 -11.0; 7711 -15.4; 8482 -15.1; 9330 -15.1; 10263 -14.5; 11289 -10.5; 12418 -9.0; 13660 -13.3; 15026 -21.0; 16529 -29.2; 18182 -34.0; 20000 -35.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Trio Half GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Trio Half ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 94 Hz    | 0.46 | -3.2 dB  |
| Peaking | 702 Hz   | 1.34 | 6.0 dB   |
| Peaking | 5237 Hz  | 1.41 | 7.0 dB   |
| Peaking | 7860 Hz  | 3.51 | -8.0 dB  |
| Peaking | 18978 Hz | 0.63 | -32.4 dB |
| Peaking | 1582 Hz  | 2.61 | -7.5 dB  |
| Peaking | 1701 Hz  | 0.8  | 3.6 dB   |
| Peaking | 2495 Hz  | 4.34 | -4.9 dB  |
| Peaking | 12699 Hz | 3.36 | 8.3 dB   |
| Peaking | 16865 Hz | 1.98 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 16000 Hz | 1.41 | -29.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Trio%20Half/Kumitate%20KL-Trio%20Half.png)