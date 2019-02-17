# 1MORE Triple Driver LTNG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.2; 28 -8.6; 31 -9.0; 34 -9.2; 37 -9.5; 41 -9.7; 45 -10.0; 49 -10.2; 54 -10.5; 60 -10.8; 66 -11.0; 72 -11.3; 79 -11.6; 87 -11.9; 96 -12.2; 106 -12.4; 116 -12.6; 128 -12.7; 141 -12.8; 155 -12.7; 170 -12.6; 187 -12.4; 206 -12.1; 227 -11.8; 249 -11.5; 274 -11.1; 302 -10.6; 332 -10.1; 365 -9.5; 402 -9.2; 442 -8.7; 486 -8.2; 535 -7.8; 588 -7.3; 647 -6.9; 712 -6.5; 783 -6.2; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.1; 1261 -7.2; 1387 -7.2; 1526 -7.2; 1678 -7.4; 1846 -7.6; 2031 -7.8; 2234 -8.1; 2457 -8.1; 2703 -7.6; 2973 -6.7; 3270 -6.4; 3597 -7.1; 3957 -9.0; 4353 -10.5; 4788 -7.9; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.8; 11289 -9.0; 12418 -13.3; 13660 -22.2; 15026 -31.9; 16529 -36.2; 18182 -26.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver LTNG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver LTNG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 79 Hz    | 0.42 | -3.8 dB  |
| Peaking | 192 Hz   | 0.66 | -3.8 dB  |
| Peaking | 4252 Hz  | 4.79 | -6.5 dB  |
| Peaking | 7922 Hz  | 0.72 | 10.2 dB  |
| Peaking | 16205 Hz | 1.07 | -34.3 dB |
| Peaking | 2270 Hz  | 1.95 | -2.1 dB  |
| Peaking | 5884 Hz  | 4.18 | 4.6 dB   |
| Peaking | 7911 Hz  | 2.78 | -4.2 dB  |
| Peaking | 11687 Hz | 1.75 | 4.8 dB   |
| Peaking | 14454 Hz | 2.44 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 10.0 dB  |
| Peaking | 16000 Hz | 1.41 | -34.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/1MORE%20Triple%20Driver%20LTNG/1MORE%20Triple%20Driver%20LTNG.png)