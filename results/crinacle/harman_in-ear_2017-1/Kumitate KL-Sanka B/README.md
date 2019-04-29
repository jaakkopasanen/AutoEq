# Kumitate KL-Sanka B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.3; 25 -10.5; 28 -10.7; 31 -10.9; 34 -11.0; 37 -11.1; 41 -11.2; 45 -11.3; 49 -11.3; 54 -11.4; 60 -11.5; 66 -11.7; 72 -11.8; 79 -11.9; 87 -12.0; 96 -12.1; 106 -12.0; 116 -11.9; 128 -11.8; 141 -11.5; 155 -11.2; 170 -10.7; 187 -10.3; 206 -9.7; 227 -9.2; 249 -8.7; 274 -8.2; 302 -7.7; 332 -7.3; 365 -6.9; 402 -6.6; 442 -6.3; 486 -6.0; 535 -5.6; 588 -5.3; 647 -4.9; 712 -4.5; 783 -4.0; 861 -3.6; 947 -3.5; 1042 -3.7; 1146 -4.2; 1261 -4.7; 1387 -4.8; 1526 -4.6; 1678 -4.2; 1846 -4.1; 2031 -4.1; 2234 -4.1; 2457 -3.5; 2703 -2.0; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -2.9; 4788 -4.3; 5267 -4.2; 5793 -3.8; 6373 -4.8; 7010 -9.0; 7711 -11.5; 8482 -15.0; 9330 -19.9; 10263 -17.8; 11289 -8.2; 12418 -6.5; 13660 -16.3; 15026 -27.9; 16529 -24.8; 18182 -12.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sanka B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sanka B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.38 | -4.4 dB  |
| Peaking | 131 Hz   | 0.88 | -3.5 dB  |
| Peaking | 5601 Hz  | 0.21 | 5.2 dB   |
| Peaking | 9181 Hz  | 2.84 | -15.8 dB |
| Peaking | 15673 Hz | 1.96 | -26.9 dB |
| Peaking | 2145 Hz  | 1.95 | -2.1 dB  |
| Peaking | 3260 Hz  | 2.56 | 2.9 dB   |
| Peaking | 11500 Hz | 0.86 | -3.5 dB  |
| Peaking | 12349 Hz | 2.96 | 10.7 dB  |
| Peaking | 14489 Hz | 5.89 | -6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 16000 Hz | 1.41 | -20.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Sanka%20B/Kumitate%20KL-Sanka%20B.png)