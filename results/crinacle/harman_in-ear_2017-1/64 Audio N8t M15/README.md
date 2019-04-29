# 64 Audio N8t M15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.2; 25 -10.4; 28 -10.7; 31 -10.8; 34 -10.9; 37 -11.0; 41 -11.0; 45 -11.0; 49 -11.1; 54 -11.1; 60 -11.1; 66 -11.1; 72 -11.1; 79 -11.2; 87 -11.3; 96 -11.3; 106 -11.1; 116 -11.2; 128 -11.0; 141 -10.9; 155 -10.6; 170 -10.4; 187 -10.2; 206 -9.9; 227 -9.6; 249 -9.3; 274 -9.0; 302 -8.6; 332 -8.2; 365 -7.9; 402 -7.6; 442 -7.4; 486 -7.2; 535 -6.9; 588 -6.8; 647 -6.5; 712 -6.2; 783 -5.9; 861 -5.7; 947 -5.6; 1042 -5.8; 1146 -6.2; 1261 -6.7; 1387 -6.8; 1526 -6.5; 1678 -6.0; 1846 -5.5; 2031 -4.8; 2234 -3.8; 2457 -2.7; 2703 -1.6; 2973 -0.7; 3270 -0.5; 3597 -1.2; 3957 -2.3; 4353 -3.1; 4788 -4.3; 5267 -5.0; 5793 -2.0; 6373 -1.3; 7010 -3.8; 7711 -5.9; 8482 -6.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -10.9; 15026 -19.7; 16529 -27.5; 18182 -26.0; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8t M15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8t M15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.53 | -3.5 dB  |
| Peaking | 123 Hz   | 0.44 | -4.3 dB  |
| Peaking | 4496 Hz  | 0.59 | 5.2 dB   |
| Peaking | 12335 Hz | 1.89 | 8.0 dB   |
| Peaking | 17008 Hz | 0.96 | -25.2 dB |
| Peaking | 1554 Hz  | 2.34 | -1.8 dB  |
| Peaking | 3079 Hz  | 2.63 | 2.6 dB   |
| Peaking | 5222 Hz  | 2.41 | -4.0 dB  |
| Peaking | 6108 Hz  | 4.42 | 4.9 dB   |
| Peaking | 18323 Hz | 5.98 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -21.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8t%20M15/64%20Audio%20N8t%20M15.png)