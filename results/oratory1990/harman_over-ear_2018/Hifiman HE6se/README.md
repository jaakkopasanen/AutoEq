# Hifiman HE6se
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.7; 25 -3.7; 28 -3.7; 31 -3.8; 34 -3.9; 37 -4.0; 41 -4.0; 45 -4.1; 49 -4.1; 54 -4.2; 60 -4.4; 66 -4.6; 72 -4.8; 79 -5.1; 87 -5.4; 96 -5.8; 106 -6.2; 116 -6.5; 128 -6.8; 141 -7.0; 155 -7.2; 170 -7.5; 187 -7.8; 206 -8.2; 227 -8.4; 249 -8.5; 274 -8.4; 302 -8.2; 332 -8.1; 365 -8.1; 402 -8.2; 442 -8.3; 486 -8.0; 535 -7.5; 588 -7.5; 647 -7.8; 712 -8.1; 783 -8.9; 861 -8.9; 947 -8.4; 1042 -7.1; 1146 -4.8; 1261 -2.0; 1387 -1.2; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.7; 2234 -2.3; 2457 -4.0; 2703 -5.9; 2973 -7.7; 3270 -8.4; 3597 -8.6; 3957 -9.6; 4353 -10.3; 4788 -7.8; 5267 -5.4; 5793 -4.9; 6373 -6.5; 7010 -7.9; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.6; 18182 -14.5; 20000 -15.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman HE6se GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman HE6se ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.63 | 2.7 dB   |
| Peaking | 64 Hz    | 1.21 | 1.4 dB   |
| Peaking | 676 Hz   | 0.29 | -2.7 dB  |
| Peaking | 1697 Hz  | 1.39 | 9.1 dB   |
| Peaking | 3774 Hz  | 2.31 | -3.8 dB  |
| Peaking | 862 Hz   | 1.15 | 3.1 dB   |
| Peaking | 886 Hz   | 2.38 | -5.1 dB  |
| Peaking | 4413 Hz  | 8.23 | -2.0 dB  |
| Peaking | 5511 Hz  | 6.19 | 2.9 dB   |
| Peaking | 19242 Hz | 1.28 | -10.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20HE6se/Hifiman%20HE6se.png)