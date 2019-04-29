# Campfire Orion
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.7; 25 -5.8; 28 -6.0; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.7; 49 -6.9; 54 -7.1; 60 -7.4; 66 -7.7; 72 -8.0; 79 -8.4; 87 -8.8; 96 -9.3; 106 -9.7; 116 -10.1; 128 -10.4; 141 -10.8; 155 -11.0; 170 -11.2; 187 -11.3; 206 -11.4; 227 -11.4; 249 -11.4; 274 -11.3; 302 -11.1; 332 -10.8; 365 -10.5; 402 -10.2; 442 -9.9; 486 -9.6; 535 -9.2; 588 -8.8; 647 -8.3; 712 -7.7; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.8; 1146 -7.4; 1261 -7.8; 1387 -8.0; 1526 -7.8; 1678 -7.5; 1846 -7.5; 2031 -7.4; 2234 -6.6; 2457 -4.3; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.5; 5267 -7.0; 5793 -2.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -18.0; 16529 -10.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Orion GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Orion ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 222 Hz   | 0.53 | -5.1 dB  |
| Peaking | 2012 Hz  | 1.6  | -3.8 dB  |
| Peaking | 3201 Hz  | 1.31 | 7.9 dB   |
| Peaking | 6348 Hz  | 7.85 | 4.9 dB   |
| Peaking | 15265 Hz | 3.61 | -13.1 dB |
| Peaking | 22 Hz    | 0.95 | 1.0 dB   |
| Peaking | 887 Hz   | 5.29 | 1.0 dB   |
| Peaking | 4427 Hz  | 7    | 2.6 dB   |
| Peaking | 5150 Hz  | 8.99 | -3.9 dB  |
| Peaking | 13083 Hz | 7.19 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Orion/Campfire%20Orion.png)