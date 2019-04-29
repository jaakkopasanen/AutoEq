# Hidition NT6 Uni
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.0; 34 -2.2; 37 -2.3; 41 -2.5; 45 -2.7; 49 -2.9; 54 -3.1; 60 -3.3; 66 -3.5; 72 -3.8; 79 -4.1; 87 -4.4; 96 -4.7; 106 -5.1; 116 -5.4; 128 -5.6; 141 -5.8; 155 -5.9; 170 -6.1; 187 -6.2; 206 -6.3; 227 -6.3; 249 -6.2; 274 -6.1; 302 -6.1; 332 -5.9; 365 -5.8; 402 -5.6; 442 -5.5; 486 -5.4; 535 -5.3; 588 -5.1; 647 -5.0; 712 -4.8; 783 -4.7; 861 -4.6; 947 -4.8; 1042 -5.2; 1146 -5.9; 1261 -6.6; 1387 -7.0; 1526 -6.9; 1678 -6.4; 1846 -5.8; 2031 -5.5; 2234 -5.6; 2457 -5.6; 2703 -4.5; 2973 -3.3; 3270 -2.8; 3597 -2.8; 3957 -1.5; 4353 -1.3; 4788 -3.2; 5267 -5.8; 5793 -5.5; 6373 -4.2; 7010 -4.1; 7711 -7.0; 8482 -9.9; 9330 -9.5; 10263 -7.0; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT6 Uni GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT6 Uni ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.01 | 4.6 dB  |
| Peaking | 55 Hz   | 1.72 | 1.7 dB  |
| Peaking | 1467 Hz | 3.42 | -1.9 dB |
| Peaking | 3988 Hz | 2.3  | 4.2 dB  |
| Peaking | 8866 Hz | 4.28 | -5.5 dB |
| Peaking | 218 Hz  | 1.24 | -1.0 dB |
| Peaking | 818 Hz  | 2.01 | 1.1 dB  |
| Peaking | 3032 Hz | 6.1  | 1.5 dB  |
| Peaking | 3757 Hz | 0.46 | -0.5 dB |
| Peaking | 6754 Hz | 7.39 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hidition%20NT6%20Uni/Hidition%20NT6%20Uni.png)