# Stax SR-L700 #5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.1; 60 -3.2; 66 -4.1; 72 -4.6; 79 -5.3; 87 -5.7; 96 -5.9; 106 -6.1; 116 -6.4; 128 -6.6; 141 -6.7; 155 -6.9; 170 -7.0; 187 -7.1; 206 -7.1; 227 -7.2; 249 -7.3; 274 -7.4; 302 -7.6; 332 -7.5; 365 -7.6; 402 -7.7; 442 -7.9; 486 -7.8; 535 -8.2; 588 -8.4; 647 -8.6; 712 -9.0; 783 -9.4; 861 -9.4; 947 -10.2; 1042 -10.3; 1146 -10.6; 1261 -10.0; 1387 -9.4; 1526 -7.9; 1678 -6.3; 1846 -5.0; 2031 -4.2; 2234 -2.8; 2457 -2.8; 2703 -2.5; 2973 -1.9; 3270 -1.4; 3597 -2.4; 3957 -2.1; 4353 -1.8; 4788 -1.1; 5267 -3.6; 5793 -8.1; 6373 -7.9; 7010 -4.8; 7711 -6.2; 8482 -6.9; 9330 -9.4; 10263 -7.1; 11289 -6.5; 12418 -10.1; 13660 -21.5; 15026 -27.2; 16529 -27.8; 18182 -27.9; 20000 -26.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.89 | 7.0 dB   |
| Peaking | 1083 Hz  | 0.83 | -6.7 dB  |
| Peaking | 9708 Hz  | 0.16 | 11.9 dB  |
| Peaking | 15924 Hz | 0.53 | -29.1 dB |
| Peaking | 19393 Hz | 0.87 | -13.5 dB |
| Peaking | 19 Hz    | 2.94 | 2.2 dB   |
| Peaking | 4907 Hz  | 3.92 | 2.6 dB   |
| Peaking | 5925 Hz  | 4.41 | -6.2 dB  |
| Peaking | 11751 Hz | 3.77 | 7.4 dB   |
| Peaking | 14028 Hz | 4.08 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB   |
| Peaking | 62 Hz    | 1.41 | 2.1 dB   |
| Peaking | 125 Hz   | 1.41 | -0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 16000 Hz | 1.41 | -29.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stax%20SR-L700%20#5/Stax%20SR-L700%20#5.png)