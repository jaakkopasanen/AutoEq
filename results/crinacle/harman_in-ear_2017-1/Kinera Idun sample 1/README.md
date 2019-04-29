# Kinera Idun sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.9; 25 -4.1; 28 -4.4; 31 -4.6; 34 -4.8; 37 -5.0; 41 -5.2; 45 -5.4; 49 -5.6; 54 -5.8; 60 -6.0; 66 -6.3; 72 -6.6; 79 -6.9; 87 -7.3; 96 -7.7; 106 -8.0; 116 -8.4; 128 -8.6; 141 -8.8; 155 -9.0; 170 -9.0; 187 -9.0; 206 -9.0; 227 -8.8; 249 -8.7; 274 -8.4; 302 -8.0; 332 -7.5; 365 -7.0; 402 -6.6; 442 -6.0; 486 -5.4; 535 -4.9; 588 -4.6; 647 -4.2; 712 -3.7; 783 -3.6; 861 -3.8; 947 -4.5; 1042 -6.4; 1146 -8.9; 1261 -10.4; 1387 -11.2; 1526 -11.0; 1678 -9.8; 1846 -8.1; 2031 -6.3; 2234 -4.6; 2457 -3.6; 2703 -3.6; 2973 -4.2; 3270 -4.8; 3597 -4.4; 3957 -3.6; 4353 -1.8; 4788 -0.5; 5267 -2.4; 5793 -3.5; 6373 -3.0; 7010 -4.4; 7711 -5.9; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.9; 13660 -9.8; 15026 -15.5; 16529 -21.5; 18182 -23.2; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Idun sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Idun sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.45 | 2.7 dB   |
| Peaking | 219 Hz   | 0.59 | -5.2 dB  |
| Peaking | 1472 Hz  | 1.64 | -10.0 dB |
| Peaking | 2959 Hz  | 0.08 | 4.9 dB   |
| Peaking | 17976 Hz | 0.67 | -20.7 dB |
| Peaking | 833 Hz   | 4.87 | 1.3 dB   |
| Peaking | 3450 Hz  | 3.95 | -2.2 dB  |
| Peaking | 4655 Hz  | 6.36 | 2.8 dB   |
| Peaking | 7961 Hz  | 3.53 | -1.9 dB  |
| Peaking | 12219 Hz | 3.64 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.0 dB   |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -17.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kinera%20Idun%20sample%201/Kinera%20Idun%20sample%201.png)