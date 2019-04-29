# Earsonics Grace
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.3; 25 -8.6; 28 -9.1; 31 -9.4; 34 -9.6; 37 -9.8; 41 -10.1; 45 -10.4; 49 -10.6; 54 -10.8; 60 -11.0; 66 -11.3; 72 -11.5; 79 -11.7; 87 -11.9; 96 -12.1; 106 -12.4; 116 -12.4; 128 -12.4; 141 -12.2; 155 -11.9; 170 -11.5; 187 -11.1; 206 -10.7; 227 -10.0; 249 -9.3; 274 -8.9; 302 -8.4; 332 -8.0; 365 -7.8; 402 -7.8; 442 -7.9; 486 -8.0; 535 -8.1; 588 -8.3; 647 -8.4; 712 -8.5; 783 -8.6; 861 -8.8; 947 -9.2; 1042 -10.0; 1146 -11.0; 1261 -11.9; 1387 -12.0; 1526 -11.2; 1678 -9.6; 1846 -7.3; 2031 -4.7; 2234 -1.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.0; 3957 -2.8; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -1.9; 6373 -4.4; 7010 -8.2; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.0; 15026 -26.2; 16529 -32.8; 18182 -26.4; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Grace GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Grace ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 103 Hz   | 0.42 | -5.9 dB  |
| Peaking | 1430 Hz  | 0.66 | -19.9 dB |
| Peaking | 2518 Hz  | 0.31 | 18.8 dB  |
| Peaking | 12608 Hz | 1.54 | 14.8 dB  |
| Peaking | 16213 Hz | 0.67 | -33.3 dB |
| Peaking | 2355 Hz  | 8.57 | 1.5 dB   |
| Peaking | 3911 Hz  | 6.22 | -2.7 dB  |
| Peaking | 5293 Hz  | 3.47 | 2.5 dB   |
| Peaking | 7022 Hz  | 7.47 | -3.4 dB  |
| Peaking | 9625 Hz  | 4.05 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -26.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20Grace/Earsonics%20Grace.png)