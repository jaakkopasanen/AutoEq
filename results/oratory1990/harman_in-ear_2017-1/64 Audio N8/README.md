# 64 Audio N8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -7.1; 25 -7.5; 28 -7.6; 31 -7.6; 34 -7.8; 37 -7.8; 41 -8.0; 45 -8.1; 49 -8.2; 54 -8.6; 60 -8.8; 66 -9.2; 72 -9.2; 79 -9.4; 87 -9.6; 96 -9.1; 106 -9.6; 116 -9.4; 128 -9.5; 141 -9.6; 155 -9.5; 170 -9.6; 187 -9.7; 206 -9.7; 227 -9.7; 249 -9.7; 274 -9.7; 302 -9.5; 332 -9.3; 365 -9.1; 402 -8.9; 442 -8.8; 486 -8.6; 535 -8.3; 588 -8.0; 647 -7.7; 712 -7.2; 783 -6.8; 861 -6.4; 947 -6.3; 1042 -6.6; 1146 -7.2; 1261 -8.0; 1387 -8.5; 1526 -8.5; 1678 -8.3; 1846 -8.1; 2031 -7.4; 2234 -6.4; 2457 -5.0; 2703 -3.6; 2973 -2.4; 3270 -1.9; 3597 -2.0; 3957 -2.7; 4353 -3.7; 4788 -4.5; 5267 -4.0; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -16.3; 15026 -26.2; 16529 -25.4; 18182 -18.3; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 143 Hz   | 0.45 | -1.8 dB  |
| Peaking | 352 Hz   | 0.09 | -1.7 dB  |
| Peaking | 5862 Hz  | 0.58 | 7.9 dB   |
| Peaking | 12178 Hz | 1.99 | 11.8 dB  |
| Peaking | 15436 Hz | 0.81 | -25.4 dB |
| Peaking | 945 Hz   | 1.2  | 4.5 dB   |
| Peaking | 1522 Hz  | 0.56 | -4.5 dB  |
| Peaking | 3206 Hz  | 1.29 | 5.3 dB   |
| Peaking | 5224 Hz  | 1.6  | -5.4 dB  |
| Peaking | 5966 Hz  | 3.89 | 6.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 16000 Hz | 1.41 | -22.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/64%20Audio%20N8/64%20Audio%20N8.png)