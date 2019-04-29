# Kumitate KL-Kanon 6-Minus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.0; 25 -0.8; 28 -0.6; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.0; 87 -1.5; 96 -2.0; 106 -2.5; 116 -3.0; 128 -3.4; 141 -3.8; 155 -4.4; 170 -4.7; 187 -5.1; 206 -5.4; 227 -5.6; 249 -5.9; 274 -6.1; 302 -6.3; 332 -6.2; 365 -6.3; 402 -6.3; 442 -6.4; 486 -6.3; 535 -6.2; 588 -6.1; 647 -6.0; 712 -5.8; 783 -5.6; 861 -5.5; 947 -5.6; 1042 -6.1; 1146 -6.8; 1261 -7.4; 1387 -7.8; 1526 -8.0; 1678 -8.4; 1846 -9.1; 2031 -9.3; 2234 -7.7; 2457 -5.3; 2703 -3.8; 2973 -3.8; 3270 -4.9; 3597 -6.8; 3957 -9.0; 4353 -11.3; 4788 -13.5; 5267 -13.1; 5793 -11.4; 6373 -12.1; 7010 -8.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.4; 15026 -16.7; 16529 -15.3; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Kanon 6-Minus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Kanon 6-Minus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.53 | 5.1 dB   |
| Peaking | 75 Hz    | 0.8  | 3.8 dB   |
| Peaking | 2986 Hz  | 4.42 | 4.3 dB   |
| Peaking | 5057 Hz  | 2.26 | -7.5 dB  |
| Peaking | 15732 Hz | 2.48 | -12.1 dB |
| Peaking | 848 Hz   | 2.91 | 1.1 dB   |
| Peaking | 1835 Hz  | 2.74 | -3.0 dB  |
| Peaking | 6397 Hz  | 5.32 | -3.3 dB  |
| Peaking | 10770 Hz | 0.52 | 2.1 dB   |
| Peaking | 14819 Hz | 1.69 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -9.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Kanon%206-Minus/Kumitate%20KL-Kanon%206-Minus.png)