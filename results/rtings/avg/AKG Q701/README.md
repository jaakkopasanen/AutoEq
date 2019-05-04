# AKG Q701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.0; 54 -1.3; 60 -1.7; 66 -2.0; 72 -2.3; 79 -2.7; 87 -3.2; 96 -3.6; 106 -4.1; 116 -4.6; 128 -5.0; 141 -5.4; 155 -5.7; 170 -5.8; 187 -5.9; 206 -6.0; 227 -6.0; 249 -6.1; 274 -6.1; 302 -6.2; 332 -6.2; 365 -6.2; 402 -6.2; 442 -6.1; 486 -5.8; 535 -5.2; 588 -4.7; 647 -4.7; 712 -4.4; 783 -4.1; 861 -3.9; 947 -4.0; 1042 -4.0; 1146 -4.0; 1261 -4.5; 1387 -4.9; 1526 -5.9; 1678 -7.4; 1846 -9.2; 2031 -10.3; 2234 -11.0; 2457 -10.1; 2703 -8.8; 2973 -7.0; 3270 -5.4; 3597 -5.9; 3957 -6.3; 4353 -6.6; 4788 -7.1; 5267 -7.5; 5793 -8.6; 6373 -10.5; 7010 -11.3; 7711 -11.6; 8482 -10.7; 9330 -6.7; 10263 -6.5; 11289 -6.8; 12418 -6.8; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -11.3; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.48 | 6.4 dB  |
| Peaking | 1038 Hz  | 0.93 | 3.0 dB  |
| Peaking | 2136 Hz  | 2.75 | -5.7 dB |
| Peaking | 7324 Hz  | 2.78 | -5.7 dB |
| Peaking | 19053 Hz | 1.48 | -6.2 dB |
| Peaking | 237 Hz   | 1.05 | -0.4 dB |
| Peaking | 2656 Hz  | 4.62 | -1.3 dB |
| Peaking | 3310 Hz  | 3.83 | 2.0 dB  |
| Peaking | 16544 Hz | 1.11 | 1.3 dB  |
| Peaking | 17732 Hz | 3.14 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20Q701/AKG%20Q701.png)