# Hidition NT6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.5; 25 -4.7; 28 -4.9; 31 -5.1; 34 -5.2; 37 -5.3; 41 -5.5; 45 -5.6; 49 -5.7; 54 -5.9; 60 -6.1; 66 -6.3; 72 -6.7; 79 -7.0; 87 -7.4; 96 -7.9; 106 -8.2; 116 -8.5; 128 -8.9; 141 -9.1; 155 -9.4; 170 -9.5; 187 -9.6; 206 -9.6; 227 -9.6; 249 -9.6; 274 -9.5; 302 -9.3; 332 -9.1; 365 -8.7; 402 -8.6; 442 -8.3; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.3; 712 -7.0; 783 -6.7; 861 -6.6; 947 -6.6; 1042 -6.8; 1146 -7.3; 1261 -7.7; 1387 -7.8; 1526 -7.5; 1678 -7.0; 1846 -6.6; 2031 -6.0; 2234 -5.5; 2457 -4.5; 2703 -3.1; 2973 -2.1; 3270 -1.3; 3597 -0.9; 3957 -0.5; 4353 -0.6; 4788 -2.2; 5267 -3.9; 5793 -2.9; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -12.8; 10263 -13.9; 11289 -7.8; 12418 -6.5; 13660 -11.6; 15026 -23.1; 16529 -19.8; 18182 -9.8; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 231 Hz   | 0.65 | -3.3 dB  |
| Peaking | 3803 Hz  | 1.67 | 6.5 dB   |
| Peaking | 6445 Hz  | 4.35 | 4.2 dB   |
| Peaking | 9791 Hz  | 6.05 | -8.1 dB  |
| Peaking | 15670 Hz | 2.42 | -19.2 dB |
| Peaking | 22 Hz    | 1.14 | 2.1 dB   |
| Peaking | 48 Hz    | 2.18 | 0.8 dB   |
| Peaking | 1426 Hz  | 3.17 | -1.6 dB  |
| Peaking | 12602 Hz | 4.1  | 6.1 dB   |
| Peaking | 15720 Hz | 0.59 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB   |
| Peaking | 62 Hz    | 1.41 | 0.5 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -16.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hidition%20NT6/Hidition%20NT6.png)