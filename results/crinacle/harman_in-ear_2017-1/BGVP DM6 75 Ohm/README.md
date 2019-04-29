# BGVP DM6 75 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.8; 34 -2.2; 37 -2.6; 41 -3.1; 45 -3.5; 49 -4.0; 54 -4.4; 60 -4.8; 66 -5.3; 72 -5.7; 79 -6.2; 87 -6.8; 96 -7.3; 106 -7.8; 116 -8.3; 128 -8.7; 141 -9.0; 155 -9.3; 170 -9.5; 187 -9.8; 206 -10.0; 227 -10.2; 249 -10.2; 274 -10.2; 302 -10.3; 332 -10.1; 365 -10.0; 402 -9.9; 442 -9.9; 486 -9.8; 535 -9.6; 588 -9.5; 647 -9.3; 712 -9.0; 783 -8.8; 861 -8.6; 947 -8.7; 1042 -9.0; 1146 -9.7; 1261 -10.2; 1387 -10.1; 1526 -9.4; 1678 -8.2; 1846 -6.7; 2031 -4.9; 2234 -3.1; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.6; 4353 -4.6; 4788 -4.4; 5267 -1.5; 5793 -0.8; 6373 -3.4; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.4; 15026 -21.6; 16529 -25.0; 18182 -18.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 75 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 75 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.24 | 6.6 dB   |
| Peaking | 489 Hz   | 0.14 | -4.2 dB  |
| Peaking | 3402 Hz  | 0.79 | 8.5 dB   |
| Peaking | 12601 Hz | 1.53 | 8.7 dB   |
| Peaking | 16162 Hz | 1.16 | -22.7 dB |
| Peaking | 1475 Hz  | 3.21 | -2.7 dB  |
| Peaking | 2534 Hz  | 3.42 | 1.9 dB   |
| Peaking | 4538 Hz  | 4.76 | -4.5 dB  |
| Peaking | 5637 Hz  | 3.91 | 3.9 dB   |
| Peaking | 19323 Hz | 1.26 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -18.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/BGVP%20DM6%2075%20Ohm/BGVP%20DM6%2075%20Ohm.png)