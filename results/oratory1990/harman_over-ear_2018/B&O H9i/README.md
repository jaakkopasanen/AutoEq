# B&O H9i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -21.3; 23 -20.9; 25 -20.4; 28 -19.3; 31 -17.9; 34 -16.5; 37 -15.3; 41 -14.1; 45 -13.0; 49 -12.1; 54 -11.2; 60 -10.6; 66 -10.2; 72 -9.8; 79 -9.6; 87 -9.5; 96 -9.4; 106 -9.3; 116 -9.0; 128 -8.6; 141 -8.4; 155 -8.2; 170 -8.0; 187 -7.6; 206 -7.3; 227 -7.2; 249 -6.8; 274 -6.4; 302 -6.0; 332 -5.6; 365 -5.4; 402 -5.3; 442 -5.2; 486 -5.3; 535 -5.4; 588 -5.6; 647 -5.9; 712 -6.4; 783 -7.1; 861 -8.0; 947 -9.1; 1042 -10.3; 1146 -12.0; 1261 -14.8; 1387 -16.8; 1526 -15.4; 1678 -11.4; 1846 -7.3; 2031 -4.7; 2234 -3.6; 2457 -3.8; 2703 -5.3; 2973 -7.5; 3270 -8.1; 3597 -6.6; 3957 -5.0; 4353 -1.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -10.9; 10263 -9.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -7.4; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O H9i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O H9i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1    | -12.0 dB |
| Peaking | 28 Hz   | 0.28 | -3.0 dB  |
| Peaking | 1373 Hz | 3.44 | -11.4 dB |
| Peaking | 5512 Hz | 1.74 | 7.1 dB   |
| Peaking | 9218 Hz | 3.39 | -5.9 dB  |
| Peaking | 454 Hz  | 1.42 | 1.7 dB   |
| Peaking | 1044 Hz | 2.81 | -2.3 dB  |
| Peaking | 1623 Hz | 4.6  | -4.6 dB  |
| Peaking | 2275 Hz | 1.08 | 5.1 dB   |
| Peaking | 3178 Hz | 2.81 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -5.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/B&O%20H9i/B&O%20H9i.png)