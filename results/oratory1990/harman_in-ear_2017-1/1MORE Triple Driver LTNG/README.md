# 1MORE Triple Driver LTNG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.6; 28 -7.0; 31 -7.3; 34 -7.6; 37 -7.8; 41 -8.1; 45 -8.3; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.7; 79 -9.9; 87 -10.2; 96 -10.5; 106 -10.8; 116 -11.0; 128 -11.1; 141 -11.1; 155 -11.1; 170 -10.9; 187 -10.7; 206 -10.5; 227 -10.2; 249 -9.8; 274 -9.5; 302 -9.0; 332 -8.4; 365 -7.8; 402 -7.5; 442 -7.1; 486 -6.6; 535 -6.1; 588 -5.7; 647 -5.3; 712 -4.9; 783 -4.6; 861 -4.5; 947 -4.6; 1042 -5.0; 1146 -5.4; 1261 -5.5; 1387 -5.6; 1526 -5.6; 1678 -5.8; 1846 -6.0; 2031 -6.2; 2234 -6.5; 2457 -6.5; 2703 -5.9; 2973 -5.1; 3270 -4.7; 3597 -5.4; 3957 -7.4; 4353 -8.9; 4788 -6.3; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -7.4; 12418 -11.7; 13660 -20.5; 15026 -30.2; 16529 -34.5; 18182 -25.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver LTNG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver LTNG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 83 Hz    | 0.67 | -2.0 dB  |
| Peaking | 176 Hz   | 0.65 | -3.7 dB  |
| Peaking | 787 Hz   | 1.24 | 2.4 dB   |
| Peaking | 8727 Hz  | 0.67 | 9.5 dB   |
| Peaking | 16171 Hz | 1.09 | -33.0 dB |
| Peaking | 4455 Hz  | 4.16 | -6.9 dB  |
| Peaking | 5727 Hz  | 1.85 | 6.8 dB   |
| Peaking | 7755 Hz  | 2    | -4.8 dB  |
| Peaking | 11357 Hz | 4.17 | 4.2 dB   |
| Peaking | 17539 Hz | 4.81 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 16000 Hz | 1.41 | -31.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/1MORE%20Triple%20Driver%20LTNG/1MORE%20Triple%20Driver%20LTNG.png)