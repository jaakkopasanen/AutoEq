# Kumitate KL-Sanka
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.7; 25 -6.9; 28 -7.2; 31 -7.5; 34 -7.7; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.5; 54 -8.7; 60 -9.0; 66 -9.3; 72 -9.7; 79 -10.0; 87 -10.4; 96 -10.9; 106 -11.3; 116 -11.6; 128 -11.9; 141 -12.2; 155 -12.5; 170 -12.6; 187 -12.7; 206 -12.7; 227 -12.7; 249 -12.6; 274 -12.5; 302 -12.3; 332 -12.0; 365 -11.6; 402 -11.3; 442 -11.0; 486 -10.6; 535 -10.1; 588 -9.6; 647 -9.1; 712 -8.5; 783 -7.8; 861 -7.2; 947 -6.8; 1042 -6.6; 1146 -6.6; 1261 -6.3; 1387 -5.5; 1526 -4.2; 1678 -2.9; 1846 -1.7; 2031 -1.0; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -0.6; 5793 -1.3; 6373 -5.7; 7010 -7.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.5; 15026 -20.6; 16529 -18.5; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sanka GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sanka ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 192 Hz   | 0.4  | -5.6 dB  |
| Peaking | 396 Hz   | 0.41 | -1.0 dB  |
| Peaking | 2519 Hz  | 0.95 | 6.4 dB   |
| Peaking | 4828 Hz  | 2.26 | 4.5 dB   |
| Peaking | 15739 Hz | 2.9  | -17.5 dB |
| Peaking | 5790 Hz  | 7.64 | 2.1 dB   |
| Peaking | 6188 Hz  | 5.56 | 0.9 dB   |
| Peaking | 6668 Hz  | 6    | -4.1 dB  |
| Peaking | 13469 Hz | 2.94 | 4.5 dB   |
| Peaking | 14701 Hz | 5.32 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -12.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Sanka/Kumitate%20KL-Sanka.png)