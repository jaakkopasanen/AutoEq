# Periodic Audio Be
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.6; 25 -13.5; 28 -13.4; 31 -13.4; 34 -13.3; 37 -13.2; 41 -13.2; 45 -13.1; 49 -13.1; 54 -13.1; 60 -13.0; 66 -12.9; 72 -12.9; 79 -12.9; 87 -12.9; 96 -12.9; 106 -12.9; 116 -12.8; 128 -12.6; 141 -12.4; 155 -12.1; 170 -11.7; 187 -11.2; 206 -10.7; 227 -10.0; 249 -9.7; 274 -10.6; 302 -9.9; 332 -9.0; 365 -8.3; 402 -8.0; 442 -7.5; 486 -7.0; 535 -6.4; 588 -5.9; 647 -5.5; 712 -5.1; 783 -4.8; 861 -4.6; 947 -4.8; 1042 -5.4; 1146 -6.1; 1261 -6.5; 1387 -6.5; 1526 -6.2; 1678 -6.2; 1846 -6.5; 2031 -6.1; 2234 -5.5; 2457 -4.8; 2703 -3.7; 2973 -2.6; 3270 -1.5; 3597 -0.8; 3957 -0.5; 4353 -0.7; 4788 -1.6; 5267 -3.5; 5793 -7.1; 6373 -9.0; 7010 -4.2; 7711 -4.9; 8482 -5.1; 9330 -7.5; 10263 -6.3; 11289 -5.2; 12418 -5.2; 13660 -12.5; 15026 -22.6; 16529 -29.1; 18182 -29.8; 20000 -24.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.25 | -8.0 dB  |
| Peaking | 135 Hz   | 0.63 | -4.9 dB  |
| Peaking | 305 Hz   | 2.11 | -1.9 dB  |
| Peaking | 4034 Hz  | 1.86 | 5.8 dB   |
| Peaking | 18048 Hz | 1.03 | -28.4 dB |
| Peaking | 1741 Hz  | 2.12 | -1.7 dB  |
| Peaking | 6222 Hz  | 5.34 | -7.3 dB  |
| Peaking | 6960 Hz  | 2.01 | 3.7 dB   |
| Peaking | 12421 Hz | 2.07 | 9.6 dB   |
| Peaking | 15629 Hz | 1.68 | -9.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB  |
| Peaking | 62 Hz    | 1.41 | -5.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -27.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)