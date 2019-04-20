# Massdrop x MEE Audio Pinnacle PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.8; 25 -4.1; 28 -4.5; 31 -4.8; 34 -5.1; 37 -5.3; 41 -5.6; 45 -5.9; 49 -6.1; 54 -6.4; 60 -6.8; 66 -7.1; 72 -7.4; 79 -7.8; 87 -8.2; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.2; 141 -9.2; 155 -9.3; 170 -10.4; 187 -10.7; 206 -10.3; 227 -10.0; 249 -9.7; 274 -9.3; 302 -8.8; 332 -8.3; 365 -8.0; 402 -7.6; 442 -7.2; 486 -6.5; 535 -5.9; 588 -5.3; 647 -4.7; 712 -4.1; 783 -3.5; 861 -3.0; 947 -2.9; 1042 -3.0; 1146 -3.1; 1261 -3.2; 1387 -2.7; 1526 -2.0; 1678 -1.2; 1846 -1.2; 2031 -1.1; 2234 -1.3; 2457 -2.1; 2703 -3.4; 2973 -3.9; 3270 -3.4; 3597 -2.8; 3957 -3.3; 4353 -4.8; 4788 -6.6; 5267 -6.9; 5793 -3.4; 6373 -0.5; 7010 -2.8; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -6.3; 12418 -11.5; 13660 -20.5; 15026 -30.2; 16529 -31.1; 18182 -22.6; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x MEE Audio Pinnacle PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x MEE Audio Pinnacle PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 190 Hz   | 0.57 | -5.0 dB  |
| Peaking | 819 Hz   | 1.63 | 2.1 dB   |
| Peaking | 1975 Hz  | 1.02 | 4.4 dB   |
| Peaking | 9887 Hz  | 0.63 | 14.7 dB  |
| Peaking | 15726 Hz | 0.73 | -34.7 dB |
| Peaking | 23 Hz    | 1.62 | 1.9 dB   |
| Peaking | 5167 Hz  | 3.6  | -6.6 dB  |
| Peaking | 6424 Hz  | 1.54 | 7.6 dB   |
| Peaking | 7896 Hz  | 2.52 | -6.1 dB  |
| Peaking | 17196 Hz | 4.17 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 16000 Hz | 1.41 | -32.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Massdrop%20x%20MEE%20Audio%20Pinnacle%20PX/Massdrop%20x%20MEE%20Audio%20Pinnacle%20PX.png)