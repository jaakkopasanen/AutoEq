# Hidition NT6 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.1; 25 -7.3; 28 -7.5; 31 -7.6; 34 -7.7; 37 -7.7; 41 -7.7; 45 -7.8; 49 -7.9; 54 -8.0; 60 -8.0; 66 -8.2; 72 -8.4; 79 -8.6; 87 -8.9; 96 -9.1; 106 -9.4; 116 -9.6; 128 -9.8; 141 -10.0; 155 -10.1; 170 -10.1; 187 -10.2; 206 -10.2; 227 -10.1; 249 -9.9; 274 -9.8; 302 -9.5; 332 -9.1; 365 -8.6; 402 -8.2; 442 -7.7; 486 -7.2; 535 -6.5; 588 -5.8; 647 -5.2; 712 -4.6; 783 -4.2; 861 -4.2; 947 -4.7; 1042 -5.7; 1146 -7.0; 1261 -8.0; 1387 -8.3; 1526 -8.0; 1678 -7.4; 1846 -6.6; 2031 -5.9; 2234 -5.5; 2457 -4.8; 2703 -3.5; 2973 -2.3; 3270 -1.7; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -4.8; 5793 -5.4; 6373 -2.9; 7010 -4.0; 7711 -6.9; 8482 -11.6; 9330 -12.4; 10263 -9.9; 11289 -7.0; 12418 -6.6; 13660 -11.7; 15026 -18.6; 16529 -20.4; 18182 -17.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT6 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT6 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 162 Hz   | 0.64 | -4.0 dB  |
| Peaking | 4159 Hz  | 1.27 | 6.7 dB   |
| Peaking | 9069 Hz  | 4.86 | -5.9 dB  |
| Peaking | 12324 Hz | 2.6  | 6.5 dB   |
| Peaking | 16401 Hz | 0.88 | -15.5 dB |
| Peaking | 821 Hz   | 2.05 | 3.2 dB   |
| Peaking | 1403 Hz  | 2.2  | -2.9 dB  |
| Peaking | 5569 Hz  | 5.94 | -5.1 dB  |
| Peaking | 6513 Hz  | 2.26 | 3.9 dB   |
| Peaking | 8286 Hz  | 5.16 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -15.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hidition%20NT6%20Pro/Hidition%20NT6%20Pro.png)