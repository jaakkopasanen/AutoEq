# Cozoy Trio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.0; 25 -4.2; 28 -4.6; 31 -4.8; 34 -5.1; 37 -5.3; 41 -5.5; 45 -5.8; 49 -6.0; 54 -6.3; 60 -6.6; 66 -7.0; 72 -7.3; 79 -7.7; 87 -8.1; 96 -8.6; 106 -9.0; 116 -9.4; 128 -9.7; 141 -10.0; 155 -10.1; 170 -10.3; 187 -10.3; 206 -10.3; 227 -10.1; 249 -9.9; 274 -9.6; 302 -9.1; 332 -8.4; 365 -7.7; 402 -6.9; 442 -6.1; 486 -5.3; 535 -4.5; 588 -3.6; 647 -2.7; 712 -1.8; 783 -1.1; 861 -1.1; 947 -2.6; 1042 -4.4; 1146 -5.6; 1261 -6.9; 1387 -8.0; 1526 -8.2; 1678 -7.6; 1846 -6.2; 2031 -4.2; 2234 -2.4; 2457 -1.1; 2703 -0.8; 2973 -1.4; 3270 -2.3; 3597 -2.1; 3957 -1.6; 4353 -1.1; 4788 -0.5; 5267 -2.6; 5793 -6.2; 6373 -7.6; 7010 -9.1; 7711 -6.4; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -6.7; 13660 -11.6; 15026 -16.4; 16529 -15.1; 18182 -9.4; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cozoy Trio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cozoy Trio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 181 Hz   | 0.64 | -5.2 dB  |
| Peaking | 745 Hz   | 2.47 | 5.4 dB   |
| Peaking | 2715 Hz  | 3.45 | 5.0 dB   |
| Peaking | 4466 Hz  | 3.63 | 5.1 dB   |
| Peaking | 15794 Hz | 1.62 | -12.3 dB |
| Peaking | 22 Hz    | 1.38 | 1.8 dB   |
| Peaking | 1498 Hz  | 2.02 | -5.9 dB  |
| Peaking | 1568 Hz  | 0.69 | 2.4 dB   |
| Peaking | 6809 Hz  | 4.56 | -4.1 dB  |
| Peaking | 11080 Hz | 2.51 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -11.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Cozoy%20Trio/Cozoy%20Trio.png)