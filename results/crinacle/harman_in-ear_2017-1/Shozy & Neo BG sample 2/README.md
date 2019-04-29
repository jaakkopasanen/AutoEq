# Shozy & Neo BG sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.4; 28 -5.8; 31 -6.1; 34 -6.4; 37 -6.5; 41 -6.8; 45 -7.1; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.4; 79 -8.7; 87 -9.1; 96 -9.4; 106 -9.9; 116 -10.2; 128 -10.4; 141 -10.6; 155 -10.6; 170 -10.7; 187 -10.8; 206 -10.9; 227 -10.7; 249 -10.5; 274 -10.4; 302 -10.1; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.1; 535 -7.6; 588 -7.1; 647 -6.6; 712 -6.1; 783 -5.6; 861 -5.3; 947 -5.3; 1042 -5.8; 1146 -6.6; 1261 -7.4; 1387 -8.0; 1526 -8.4; 1678 -8.9; 1846 -9.0; 2031 -7.3; 2234 -3.8; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -1.9; 3597 -1.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -4.5; 6373 -7.5; 7010 -5.9; 7711 -7.1; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.7; 15026 -19.5; 16529 -26.2; 18182 -25.1; 20000 -16.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy & Neo BG sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy & Neo BG sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 221 Hz   | 0.45 | -5.0 dB  |
| Peaking | 1831 Hz  | 1.25 | -11.2 dB |
| Peaking | 2504 Hz  | 1.45 | 7.0 dB   |
| Peaking | 4957 Hz  | 0.13 | 6.0 dB   |
| Peaking | 17407 Hz | 0.75 | -25.1 dB |
| Peaking | 21 Hz    | 1.28 | 2.1 dB   |
| Peaking | 5100 Hz  | 2.44 | 6.5 dB   |
| Peaking | 6032 Hz  | 1.59 | -6.3 dB  |
| Peaking | 12617 Hz | 2.02 | 5.4 dB   |
| Peaking | 15424 Hz | 3.14 | -4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -20.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shozy%20&%20Neo%20BG%20sample%202/Shozy%20&%20Neo%20BG%20sample%202.png)