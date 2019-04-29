# Simgot EM5H
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.7; 25 -4.1; 28 -4.6; 31 -5.0; 34 -5.4; 37 -5.7; 41 -6.0; 45 -6.4; 49 -6.6; 54 -6.9; 60 -7.3; 66 -7.7; 72 -8.1; 79 -8.6; 87 -9.0; 96 -9.6; 106 -10.0; 116 -10.5; 128 -10.8; 141 -11.1; 155 -11.5; 170 -11.7; 187 -11.8; 206 -12.0; 227 -12.0; 249 -12.0; 274 -12.0; 302 -11.9; 332 -11.7; 365 -11.5; 402 -11.4; 442 -11.3; 486 -11.1; 535 -10.8; 588 -10.5; 647 -10.2; 712 -9.8; 783 -9.3; 861 -8.8; 947 -8.4; 1042 -8.2; 1146 -8.1; 1261 -8.0; 1387 -7.6; 1526 -7.1; 1678 -6.5; 1846 -5.9; 2031 -5.3; 2234 -4.7; 2457 -4.5; 2703 -4.3; 2973 -2.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -4.5; 5793 -3.3; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -11.7; 16529 -6.8; 18182 -6.6; 20000 -18.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EM5H GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EM5H ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 254 Hz   | 0.35 | -5.7 dB  |
| Peaking | 3778 Hz  | 1.52 | 6.8 dB   |
| Peaking | 6380 Hz  | 7.8  | 4.3 dB   |
| Peaking | 20069 Hz | 1.66 | -12.7 dB |
| Peaking | 17 Hz    | 0.76 | 3.8 dB   |
| Peaking | 58 Hz    | 1.45 | 0.6 dB   |
| Peaking | 2083 Hz  | 5.66 | 0.7 dB   |
| Peaking | 14869 Hz | 3.67 | -6.0 dB  |
| Peaking | 18141 Hz | 1.45 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Simgot%20EM5H/Simgot%20EM5H.png)