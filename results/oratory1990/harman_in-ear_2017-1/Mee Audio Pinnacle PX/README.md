# Mee Audio Pinnacle PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.9; 25 -4.2; 28 -4.6; 31 -4.9; 34 -5.1; 37 -5.4; 41 -5.6; 45 -5.9; 49 -6.2; 54 -6.5; 60 -6.8; 66 -7.1; 72 -7.5; 79 -7.8; 87 -8.3; 96 -8.5; 106 -8.8; 116 -9.1; 128 -9.3; 141 -9.3; 155 -9.3; 170 -10.5; 187 -10.7; 206 -10.4; 227 -10.1; 249 -9.8; 274 -9.3; 302 -8.9; 332 -8.3; 365 -8.1; 402 -7.7; 442 -7.2; 486 -6.6; 535 -5.9; 588 -5.3; 647 -4.8; 712 -4.1; 783 -3.5; 861 -3.1; 947 -3.0; 1042 -3.0; 1146 -3.2; 1261 -3.2; 1387 -2.7; 1526 -2.1; 1678 -1.3; 1846 -1.2; 2031 -1.1; 2234 -1.3; 2457 -2.2; 2703 -3.4; 2973 -4.0; 3270 -3.4; 3597 -2.9; 3957 -3.3; 4353 -4.9; 4788 -6.6; 5267 -7.0; 5793 -3.4; 6373 -0.5; 7010 -0.6; 7711 -3.3; 8482 -5.2; 9330 -3.9; 10263 -3.4; 11289 -6.2; 12418 -11.5; 13660 -20.5; 15026 -30.3; 16529 -31.1; 18182 -22.7; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Pinnacle PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Pinnacle PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 104 Hz   | 0.42 | -4.2 dB  |
| Peaking | 248 Hz   | 0.71 | -4.6 dB  |
| Peaking | 4945 Hz  | 3.17 | -6.4 dB  |
| Peaking | 8742 Hz  | 0.4  | 16.7 dB  |
| Peaking | 15740 Hz | 0.62 | -39.6 dB |
| Peaking | 2001 Hz  | 2.02 | 1.7 dB   |
| Peaking | 2926 Hz  | 2.98 | -2.4 dB  |
| Peaking | 8485 Hz  | 3.49 | -6.9 dB  |
| Peaking | 9954 Hz  | 1.09 | 4.5 dB   |
| Peaking | 14365 Hz | 3.48 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 8.8 dB   |
| Peaking | 16000 Hz | 1.41 | -36.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Mee%20Audio%20Pinnacle%20PX/Mee%20Audio%20Pinnacle%20PX.png)