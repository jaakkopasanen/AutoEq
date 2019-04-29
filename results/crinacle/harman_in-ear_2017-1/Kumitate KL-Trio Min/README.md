# Kumitate KL-Trio Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.3; 25 -11.2; 28 -11.1; 31 -11.1; 34 -11.2; 37 -11.2; 41 -11.3; 45 -11.4; 49 -11.4; 54 -11.4; 60 -11.5; 66 -11.6; 72 -11.7; 79 -11.8; 87 -11.9; 96 -12.1; 106 -12.3; 116 -12.1; 128 -12.1; 141 -12.1; 155 -12.1; 170 -11.8; 187 -11.5; 206 -11.1; 227 -10.6; 249 -10.2; 274 -9.7; 302 -9.1; 332 -8.4; 365 -7.8; 402 -7.2; 442 -6.7; 486 -6.1; 535 -5.6; 588 -5.1; 647 -4.7; 712 -4.3; 783 -4.0; 861 -3.9; 947 -4.2; 1042 -4.9; 1146 -5.9; 1261 -7.1; 1387 -8.9; 1526 -10.2; 1678 -8.6; 1846 -5.7; 2031 -3.6; 2234 -3.7; 2457 -5.0; 2703 -4.6; 2973 -2.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -6.3; 7711 -10.9; 8482 -10.7; 9330 -10.6; 10263 -9.8; 11289 -6.6; 12418 -6.5; 13660 -6.9; 15026 -14.9; 16529 -25.1; 18182 -30.3; 20000 -29.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Trio Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Trio Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.29 | -4.8 dB  |
| Peaking | 159 Hz   | 0.95 | -3.8 dB  |
| Peaking | 8472 Hz  | 2.3  | -13.7 dB |
| Peaking | 9041 Hz  | 0.42 | 14.9 dB  |
| Peaking | 18520 Hz | 0.5  | -29.8 dB |
| Peaking | 787 Hz   | 1.6  | 2.7 dB   |
| Peaking | 1511 Hz  | 3.4  | -6.0 dB  |
| Peaking | 3623 Hz  | 3.81 | 1.8 dB   |
| Peaking | 5840 Hz  | 5.9  | 1.7 dB   |
| Peaking | 22049 Hz | 2    | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -19.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Trio%20Min/Kumitate%20KL-Trio%20Min.png)