# Kumitate KL-Sirius
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.2; 31 -2.7; 34 -3.1; 37 -3.5; 41 -3.9; 45 -4.1; 49 -4.3; 54 -4.6; 60 -4.9; 66 -5.2; 72 -5.6; 79 -5.8; 87 -6.2; 96 -6.6; 106 -6.9; 116 -7.2; 128 -7.5; 141 -7.8; 155 -8.0; 170 -8.2; 187 -8.2; 206 -8.3; 227 -8.3; 249 -8.3; 274 -8.3; 302 -8.2; 332 -8.0; 365 -7.8; 402 -7.7; 442 -7.6; 486 -7.4; 535 -7.3; 588 -7.1; 647 -7.0; 712 -6.8; 783 -6.7; 861 -6.7; 947 -7.0; 1042 -7.7; 1146 -8.7; 1261 -9.4; 1387 -9.5; 1526 -8.7; 1678 -7.4; 1846 -5.9; 2031 -4.5; 2234 -3.1; 2457 -2.1; 2703 -1.8; 2973 -2.1; 3270 -2.6; 3597 -2.8; 3957 -3.0; 4353 -3.5; 4788 -3.4; 5267 -2.5; 5793 -2.0; 6373 -4.9; 7010 -8.9; 7711 -6.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.5; 16529 -11.7; 18182 -14.6; 20000 -15.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sirius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sirius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.27 | 6.3 dB   |
| Peaking | 550 Hz   | 0.1  | -2.1 dB  |
| Peaking | 2885 Hz  | 1.54 | 6.3 dB   |
| Peaking | 5413 Hz  | 3.68 | 4.4 dB   |
| Peaking | 19051 Hz | 0.96 | -10.3 dB |
| Peaking | 818 Hz   | 1.42 | 1.8 dB   |
| Peaking | 1349 Hz  | 2.25 | -3.1 dB  |
| Peaking | 2167 Hz  | 4    | 1.5 dB   |
| Peaking | 7108 Hz  | 9.56 | -3.7 dB  |
| Peaking | 13439 Hz | 1.86 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Sirius/Kumitate%20KL-Sirius.png)