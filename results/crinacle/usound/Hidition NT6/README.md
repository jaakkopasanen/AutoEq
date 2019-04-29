# Hidition NT6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.1; 25 -2.3; 28 -2.5; 31 -2.7; 34 -2.8; 37 -2.9; 41 -3.1; 45 -3.2; 49 -3.3; 54 -3.5; 60 -3.7; 66 -4.0; 72 -4.3; 79 -4.6; 87 -5.0; 96 -5.5; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.7; 155 -7.0; 170 -7.1; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.2; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.6; 402 -6.5; 442 -6.3; 486 -6.1; 535 -5.9; 588 -5.6; 647 -5.4; 712 -5.1; 783 -4.8; 861 -4.6; 947 -4.6; 1042 -4.8; 1146 -5.4; 1261 -6.0; 1387 -6.4; 1526 -6.3; 1678 -5.9; 1846 -5.5; 2031 -5.4; 2234 -5.4; 2457 -5.0; 2703 -4.0; 2973 -3.1; 3270 -2.3; 3597 -1.6; 3957 -0.8; 4353 -0.5; 4788 -1.9; 5267 -3.5; 5793 -2.8; 6373 -1.9; 7010 -2.8; 7711 -5.0; 8482 -6.8; 9330 -10.7; 10263 -10.4; 11289 -5.7; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.2  | 3.2 dB  |
| Peaking | 188 Hz   | 0.65 | -2.5 dB |
| Peaking | 4052 Hz  | 2.24 | 4.9 dB  |
| Peaking | 6574 Hz  | 4.2  | 3.4 dB  |
| Peaking | 9686 Hz  | 4.1  | -6.9 dB |
| Peaking | 922 Hz   | 2.32 | 1.2 dB  |
| Peaking | 1412 Hz  | 2.8  | -1.3 dB |
| Peaking | 2627 Hz  | 1.55 | -0.9 dB |
| Peaking | 2970 Hz  | 3.36 | 1.5 dB  |
| Peaking | 11848 Hz | 7.46 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hidition%20NT6/Hidition%20NT6.png)