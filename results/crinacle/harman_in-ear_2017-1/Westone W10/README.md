# Westone W10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.1; 25 -6.3; 28 -6.4; 31 -6.6; 34 -6.7; 37 -6.8; 41 -6.9; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.7; 66 -8.1; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.7; 106 -10.2; 116 -10.6; 128 -10.9; 141 -11.3; 155 -11.6; 170 -11.8; 187 -12.0; 206 -12.1; 227 -12.1; 249 -12.2; 274 -12.2; 302 -12.1; 332 -11.9; 365 -11.6; 402 -11.5; 442 -11.3; 486 -11.1; 535 -10.7; 588 -10.4; 647 -10.0; 712 -9.5; 783 -9.0; 861 -8.6; 947 -8.4; 1042 -8.5; 1146 -8.9; 1261 -9.3; 1387 -9.3; 1526 -8.7; 1678 -7.8; 1846 -6.8; 2031 -5.4; 2234 -3.9; 2457 -2.5; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -17.4; 18182 -22.7; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 139 Hz   | 0.83 | -2.3 dB  |
| Peaking | 332 Hz   | 0.49 | -4.9 dB  |
| Peaking | 1504 Hz  | 1.6  | -4.0 dB  |
| Peaking | 3735 Hz  | 0.67 | 7.2 dB   |
| Peaking | 18140 Hz | 1.52 | -18.4 dB |
| Peaking | 17 Hz    | 1.15 | 0.7 dB   |
| Peaking | 6330 Hz  | 2.99 | 4.6 dB   |
| Peaking | 7330 Hz  | 1.65 | -3.8 dB  |
| Peaking | 14952 Hz | 1.83 | 4.7 dB   |
| Peaking | 16779 Hz | 3.03 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -9.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20W10/Westone%20W10.png)