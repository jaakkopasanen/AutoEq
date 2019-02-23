# MrSpeakers Ether Flow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.2; 25 -4.1; 28 -3.8; 31 -3.6; 34 -3.3; 37 -2.7; 41 -2.7; 45 -5.0; 49 -6.6; 54 -5.2; 60 -5.8; 66 -8.3; 72 -8.8; 79 -8.7; 87 -8.9; 96 -9.6; 106 -9.9; 116 -10.0; 128 -10.2; 141 -10.5; 155 -10.8; 170 -10.9; 187 -10.9; 206 -10.9; 227 -10.7; 249 -10.4; 274 -9.9; 302 -9.1; 332 -8.7; 365 -7.7; 402 -6.7; 442 -5.6; 486 -4.4; 535 -5.1; 588 -5.9; 647 -5.7; 712 -5.9; 783 -6.7; 861 -6.7; 947 -6.5; 1042 -6.2; 1146 -4.5; 1261 -4.6; 1387 -4.9; 1526 -4.8; 1678 -5.5; 1846 -5.3; 2031 -5.9; 2234 -5.4; 2457 -5.9; 2703 -5.6; 2973 -5.2; 3270 -3.6; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.3; 5793 -6.7; 6373 -9.5; 7010 -9.9; 7711 -8.7; 8482 -6.5; 9330 -6.5; 10263 -8.8; 11289 -7.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 1.21 | 4.4 dB  |
| Peaking | 176 Hz   | 0.5  | -4.9 dB |
| Peaking | 492 Hz   | 1.52 | 3.5 dB  |
| Peaking | 4689 Hz  | 1.49 | 9.0 dB  |
| Peaking | 6458 Hz  | 1.98 | -7.5 dB |
| Peaking | 1323 Hz  | 2.91 | 1.9 dB  |
| Peaking | 3193 Hz  | 2.02 | -1.7 dB |
| Peaking | 3602 Hz  | 5.13 | 2.5 dB  |
| Peaking | 8725 Hz  | 4.87 | 1.3 dB  |
| Peaking | 10586 Hz | 6.52 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20Flow/MrSpeakers%20Ether%20Flow.png)