# Hidition NT8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.3; 25 -4.5; 28 -4.6; 31 -4.7; 34 -4.6; 37 -4.6; 41 -4.6; 45 -4.5; 49 -4.5; 54 -4.5; 60 -4.5; 66 -4.6; 72 -4.7; 79 -4.8; 87 -5.1; 96 -5.3; 106 -5.6; 116 -5.8; 128 -6.0; 141 -6.2; 155 -6.4; 170 -6.4; 187 -6.6; 206 -6.7; 227 -6.8; 249 -6.8; 274 -6.8; 302 -6.9; 332 -6.9; 365 -6.9; 402 -7.0; 442 -7.0; 486 -7.1; 535 -7.2; 588 -7.3; 647 -7.3; 712 -7.4; 783 -7.4; 861 -7.7; 947 -8.1; 1042 -9.0; 1146 -10.1; 1261 -11.1; 1387 -11.5; 1526 -11.0; 1678 -10.0; 1846 -8.8; 2031 -7.7; 2234 -6.7; 2457 -5.8; 2703 -5.3; 2973 -5.3; 3270 -4.0; 3597 -1.7; 3957 -0.5; 4353 -1.4; 4788 -1.0; 5267 -0.5; 5793 -0.6; 6373 -1.3; 7010 -6.5; 7711 -11.8; 8482 -11.7; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.3; 16529 -12.5; 18182 -13.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.52 | 2.3 dB   |
| Peaking | 1431 Hz  | 1.41 | -5.7 dB  |
| Peaking | 6107 Hz  | 0.79 | 10.0 dB  |
| Peaking | 7916 Hz  | 2.44 | -13.7 dB |
| Peaking | 17647 Hz | 1.46 | -8.1 dB  |
| Peaking | 3101 Hz  | 5.07 | -1.6 dB  |
| Peaking | 3855 Hz  | 3.33 | 2.7 dB   |
| Peaking | 4471 Hz  | 4.07 | -1.6 dB  |
| Peaking | 6294 Hz  | 1.6  | -0.8 dB  |
| Peaking | 6447 Hz  | 6.89 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hidition%20NT8/Hidition%20NT8.png)