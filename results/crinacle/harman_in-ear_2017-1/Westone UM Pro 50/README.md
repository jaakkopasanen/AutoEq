# Westone UM Pro 50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.1; 25 -10.3; 28 -10.6; 31 -10.8; 34 -11.0; 37 -11.1; 41 -11.2; 45 -11.3; 49 -11.4; 54 -11.6; 60 -11.9; 66 -12.2; 72 -12.5; 79 -12.8; 87 -13.1; 96 -13.6; 106 -14.0; 116 -14.3; 128 -14.5; 141 -14.8; 155 -15.0; 170 -15.1; 187 -15.1; 206 -15.0; 227 -14.9; 249 -14.8; 274 -14.5; 302 -14.2; 332 -13.8; 365 -13.2; 402 -12.8; 442 -12.3; 486 -11.7; 535 -11.0; 588 -10.3; 647 -9.6; 712 -8.8; 783 -8.0; 861 -7.3; 947 -7.0; 1042 -7.1; 1146 -7.8; 1261 -8.7; 1387 -9.2; 1526 -9.3; 1678 -8.8; 1846 -7.7; 2031 -5.4; 2234 -2.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.3; 15026 -19.4; 16529 -21.3; 18182 -21.3; 20000 -22.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.22 | -4.0 dB  |
| Peaking | 179 Hz   | 0.61 | -5.2 dB  |
| Peaking | 390 Hz   | 0.95 | -3.2 dB  |
| Peaking | 1592 Hz  | 2.29 | -5.6 dB  |
| Peaking | 3307 Hz  | 0.79 | 7.5 dB   |
| Peaking | 912 Hz   | 6.06 | 0.8 dB   |
| Peaking | 5960 Hz  | 3.33 | 3.9 dB   |
| Peaking | 12856 Hz | 1.6  | 11.2 dB  |
| Peaking | 15214 Hz | 0.91 | -13.0 dB |
| Peaking | 19910 Hz | 0.44 | -14.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -7.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -17.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20UM%20Pro%2050/Westone%20UM%20Pro%2050.png)