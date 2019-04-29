# Kumitate KL-Kanon 6-Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.4; 25 -8.3; 28 -8.3; 31 -8.3; 34 -8.3; 37 -8.3; 41 -8.4; 45 -8.5; 49 -8.7; 54 -8.9; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.2; 128 -11.5; 141 -11.7; 155 -11.8; 170 -11.8; 187 -11.8; 206 -11.6; 227 -11.4; 249 -11.2; 274 -10.9; 302 -10.4; 332 -9.9; 365 -9.3; 402 -8.7; 442 -8.2; 486 -7.5; 535 -6.7; 588 -5.9; 647 -5.1; 712 -4.1; 783 -3.1; 861 -2.2; 947 -1.4; 1042 -1.0; 1146 -0.8; 1261 -0.7; 1387 -0.6; 1526 -0.9; 1678 -1.9; 1846 -3.6; 2031 -4.7; 2234 -3.7; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -1.6; 3597 -3.7; 3957 -6.3; 4353 -9.1; 4788 -11.7; 5267 -11.5; 5793 -9.7; 6373 -10.3; 7010 -7.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.5; 15026 -12.9; 16529 -12.0; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Kanon 6-Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Kanon 6-Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 172 Hz   | 0.39 | -5.5 dB |
| Peaking | 1104 Hz  | 0.94 | 6.7 dB  |
| Peaking | 3016 Hz  | 2.43 | 6.2 dB  |
| Peaking | 5015 Hz  | 2.42 | -6.7 dB |
| Peaking | 15761 Hz | 2.37 | -7.5 dB |
| Peaking | 22 Hz    | 1.61 | -1.4 dB |
| Peaking | 1919 Hz  | 2.05 | 1.9 dB  |
| Peaking | 1993 Hz  | 4.55 | -3.7 dB |
| Peaking | 6475 Hz  | 8.81 | -2.6 dB |
| Peaking | 8966 Hz  | 0.97 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Kanon%206-Plus/Kumitate%20KL-Kanon%206-Plus.png)