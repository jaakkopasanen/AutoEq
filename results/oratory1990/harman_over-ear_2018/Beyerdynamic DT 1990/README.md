# Beyerdynamic DT 1990
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.7; 25 -3.0; 28 -3.3; 31 -3.6; 34 -3.8; 37 -4.0; 41 -4.3; 45 -4.5; 49 -4.7; 54 -5.0; 60 -5.3; 66 -5.6; 72 -5.9; 79 -6.2; 87 -6.6; 96 -7.0; 106 -7.4; 116 -7.8; 128 -8.3; 141 -8.7; 155 -9.1; 170 -9.3; 187 -9.5; 206 -9.6; 227 -9.6; 249 -9.6; 274 -9.4; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.3; 442 -8.1; 486 -7.9; 535 -7.6; 588 -7.2; 647 -7.0; 712 -6.8; 783 -6.6; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.8; 1261 -7.0; 1387 -7.1; 1526 -7.2; 1678 -7.1; 1846 -6.8; 2031 -6.4; 2234 -6.3; 2457 -6.9; 2703 -7.5; 2973 -6.5; 3270 -5.3; 3597 -4.5; 3957 -2.8; 4353 -0.5; 4788 -5.2; 5267 -8.3; 5793 -8.7; 6373 -7.9; 7010 -13.4; 7711 -16.8; 8482 -14.8; 9330 -9.8; 10263 -8.4; 11289 -10.5; 12418 -12.8; 13660 -15.2; 15026 -16.7; 16529 -16.1; 18182 -13.7; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 11 Hz    |  0.25 | 4.3 dB   |
| Peaking | 210 Hz   |  0.71 | -3.4 dB  |
| Peaking | 4225 Hz  |  5    | 7.1 dB   |
| Peaking | 7745 Hz  |  4.41 | -9.6 dB  |
| Peaking | 16303 Hz |  0.68 | -10.4 dB |
| Peaking | 1543 Hz  |  5.19 | -0.6 dB  |
| Peaking | 5346 Hz  | 10.01 | -1.8 dB  |
| Peaking | 10211 Hz |  5.62 | 2.9 dB   |
| Peaking | 13343 Hz |  4.02 | -1.1 dB  |
| Peaking | 14553 Hz |  5.92 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | -1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB  |
| Peaking | 16000 Hz | 1.41 | -12.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%201990/Beyerdynamic%20DT%201990.png)