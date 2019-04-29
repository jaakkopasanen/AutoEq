# AZLA Horizon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.7; 25 -9.7; 28 -9.7; 31 -9.7; 34 -9.7; 37 -9.6; 41 -9.5; 45 -9.4; 49 -9.3; 54 -9.2; 60 -9.2; 66 -9.1; 72 -9.1; 79 -9.1; 87 -9.1; 96 -9.1; 106 -9.1; 116 -9.1; 128 -9.1; 141 -8.9; 155 -8.7; 170 -8.5; 187 -8.2; 206 -7.9; 227 -7.5; 249 -7.1; 274 -6.7; 302 -6.2; 332 -5.6; 365 -5.1; 402 -4.7; 442 -4.2; 486 -3.8; 535 -3.3; 588 -2.9; 647 -2.5; 712 -2.1; 783 -1.7; 861 -1.4; 947 -1.5; 1042 -1.8; 1146 -2.4; 1261 -3.0; 1387 -3.3; 1526 -3.2; 1678 -3.2; 1846 -3.1; 2031 -3.0; 2234 -2.8; 2457 -2.9; 2703 -2.7; 2973 -1.9; 3270 -0.9; 3597 -0.5; 3957 -0.8; 4353 -1.8; 4788 -3.5; 5267 -5.8; 5793 -6.5; 6373 -4.9; 7010 -4.2; 7711 -4.7; 8482 -4.2; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -11.7; 15026 -22.4; 16529 -26.2; 18182 -24.5; 20000 -18.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AZLA Horizon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AZLA Horizon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.29 | -5.2 dB  |
| Peaking | 151 Hz   | 0.59 | -3.6 dB  |
| Peaking | 809 Hz   | 1.02 | 3.1 dB   |
| Peaking | 3604 Hz  | 1.79 | 4.1 dB   |
| Peaking | 17610 Hz | 1.09 | -24.6 dB |
| Peaking | 1195 Hz  | 2.12 | 0.6 dB   |
| Peaking | 1291 Hz  | 3.56 | -1.0 dB  |
| Peaking | 5576 Hz  | 5.27 | -3.2 dB  |
| Peaking | 12734 Hz | 1.24 | 10.3 dB  |
| Peaking | 15013 Hz | 1.82 | -13.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -25.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AZLA%20Horizon/AZLA%20Horizon.png)