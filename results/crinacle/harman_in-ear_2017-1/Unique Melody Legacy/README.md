# Unique Melody Legacy
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.1; 25 -7.3; 28 -7.6; 31 -7.9; 34 -8.1; 37 -8.3; 41 -8.5; 45 -8.7; 49 -8.8; 54 -9.0; 60 -9.3; 66 -9.5; 72 -9.8; 79 -10.1; 87 -10.4; 96 -10.7; 106 -11.0; 116 -11.1; 128 -11.3; 141 -11.4; 155 -11.4; 170 -11.4; 187 -11.2; 206 -11.0; 227 -10.8; 249 -10.5; 274 -10.2; 302 -9.9; 332 -9.5; 365 -9.1; 402 -8.8; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.6; 647 -7.4; 712 -7.1; 783 -6.9; 861 -6.9; 947 -7.0; 1042 -7.6; 1146 -8.3; 1261 -9.0; 1387 -9.2; 1526 -9.0; 1678 -8.4; 1846 -7.6; 2031 -6.2; 2234 -4.5; 2457 -2.9; 2703 -1.9; 2973 -1.7; 3270 -2.4; 3597 -2.7; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.3; 6373 -3.4; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.4; 15026 -19.9; 16529 -20.4; 18182 -17.8; 20000 -16.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Legacy GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Legacy ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 143 Hz   | 0.65 | -3.7 dB  |
| Peaking | 275 Hz   | 0.08 | -1.4 dB  |
| Peaking | 4416 Hz  | 0.77 | 11.0 dB  |
| Peaking | 12831 Hz | 0.67 | 23.0 dB  |
| Peaking | 15044 Hz | 0.41 | -30.9 dB |
| Peaking | 902 Hz   | 1.23 | 3.2 dB   |
| Peaking | 1449 Hz  | 0.81 | -4.0 dB  |
| Peaking | 2606 Hz  | 1.63 | 4.0 dB   |
| Peaking | 3483 Hz  | 4.89 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -16.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%20Legacy/Unique%20Melody%20Legacy.png)