# Kumitate KL-Trio Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.8; 25 -6.8; 28 -6.8; 31 -6.8; 34 -6.9; 37 -7.0; 41 -7.1; 45 -7.1; 49 -7.1; 54 -7.2; 60 -7.2; 66 -7.4; 72 -7.5; 79 -7.6; 87 -7.8; 96 -8.1; 106 -8.1; 116 -8.0; 128 -8.0; 141 -7.9; 155 -7.8; 170 -7.6; 187 -7.3; 206 -6.9; 227 -6.5; 249 -6.0; 274 -5.5; 302 -5.0; 332 -4.3; 365 -3.6; 402 -3.0; 442 -2.5; 486 -1.9; 535 -1.4; 588 -0.9; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.6; 1146 -2.1; 1261 -4.4; 1387 -7.7; 1526 -10.3; 1678 -10.6; 1846 -9.6; 2031 -9.0; 2234 -9.7; 2457 -11.1; 2703 -10.6; 2973 -7.8; 3270 -5.6; 3597 -4.9; 3957 -4.8; 4353 -4.9; 4788 -5.1; 5267 -5.4; 5793 -6.3; 6373 -7.9; 7010 -12.4; 7711 -18.3; 8482 -19.4; 9330 -19.1; 10263 -17.9; 11289 -13.6; 12418 -12.2; 13660 -17.0; 15026 -24.6; 16529 -32.3; 18182 -36.8; 20000 -37.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Trio Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Trio Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1542 Hz  | 0.45 | 11.5 dB  |
| Peaking | 1601 Hz  | 2.03 | -14.4 dB |
| Peaking | 2473 Hz  | 2.67 | -9.7 dB  |
| Peaking | 18111 Hz | 0.48 | -28.5 dB |
| Peaking | 19876 Hz | 1.68 | -13.8 dB |
| Peaking | 123 Hz   | 0.89 | -2.2 dB  |
| Peaking | 6206 Hz  | 1.5  | 8.5 dB   |
| Peaking | 8094 Hz  | 1.31 | -12.6 dB |
| Peaking | 12321 Hz | 2.02 | 10.2 dB  |
| Peaking | 16052 Hz | 2.87 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 16000 Hz | 1.41 | -34.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Trio%20Max/Kumitate%20KL-Trio%20Max.png)