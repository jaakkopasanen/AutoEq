# MrSpeakers Ether Flow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.0; 25 -3.9; 28 -3.6; 31 -3.4; 34 -3.1; 37 -2.5; 41 -2.5; 45 -4.7; 49 -6.3; 54 -4.9; 60 -5.6; 66 -8.1; 72 -8.6; 79 -8.4; 87 -8.7; 96 -9.4; 106 -9.7; 116 -9.8; 128 -10.0; 141 -10.3; 155 -10.5; 170 -10.7; 187 -10.7; 206 -10.7; 227 -10.5; 249 -10.2; 274 -9.6; 302 -8.9; 332 -8.5; 365 -7.5; 402 -6.5; 442 -5.3; 486 -4.2; 535 -4.8; 588 -5.7; 647 -5.5; 712 -5.7; 783 -6.5; 861 -6.5; 947 -6.3; 1042 -6.0; 1146 -4.3; 1261 -4.4; 1387 -4.7; 1526 -4.6; 1678 -5.3; 1846 -5.1; 2031 -5.7; 2234 -5.2; 2457 -5.7; 2703 -5.4; 2973 -5.0; 3270 -3.4; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.1; 5793 -6.5; 6373 -9.3; 7010 -9.6; 7711 -8.5; 8482 -6.5; 9330 -6.5; 10263 -8.6; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 1.19 | 4.6 dB  |
| Peaking | 240 Hz   | 0.45 | -7.1 dB |
| Peaking | 455 Hz   | 0.64 | 5.8 dB  |
| Peaking | 4661 Hz  | 1.5  | 8.6 dB  |
| Peaking | 6495 Hz  | 2.09 | -7.0 dB |
| Peaking | 486 Hz   | 7.09 | 1.6 dB  |
| Peaking | 971 Hz   | 1.56 | -3.1 dB |
| Peaking | 1173 Hz  | 1.8  | 3.5 dB  |
| Peaking | 2702 Hz  | 4.75 | -1.1 dB |
| Peaking | 22050 Hz | 1.81 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20Flow/MrSpeakers%20Ether%20Flow.png)