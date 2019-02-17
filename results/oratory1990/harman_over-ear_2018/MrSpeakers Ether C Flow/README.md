# MrSpeakers Ether C Flow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.1; 25 -4.9; 28 -4.4; 31 -3.7; 34 -2.8; 37 -1.7; 41 -1.6; 45 -3.6; 49 -5.3; 54 -4.0; 60 -2.0; 66 -4.5; 72 -5.7; 79 -5.5; 87 -6.0; 96 -6.4; 106 -6.2; 116 -5.7; 128 -5.0; 141 -4.7; 155 -4.7; 170 -4.9; 187 -5.5; 206 -6.0; 227 -6.6; 249 -6.9; 274 -7.0; 302 -6.8; 332 -6.3; 365 -5.8; 402 -5.4; 442 -5.0; 486 -4.4; 535 -4.6; 588 -4.9; 647 -5.8; 712 -7.3; 783 -7.8; 861 -7.1; 947 -6.6; 1042 -6.1; 1146 -6.0; 1261 -6.5; 1387 -6.0; 1526 -5.8; 1678 -4.9; 1846 -3.8; 2031 -3.0; 2234 -2.8; 2457 -2.0; 2703 -2.2; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.7; 6373 -3.7; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 1.24 | 4.2 dB  |
| Peaking | 152 Hz   | 3.5  | 1.8 dB  |
| Peaking | 525 Hz   | 2.5  | 2.4 dB  |
| Peaking | 777 Hz   | 2.77 | -2.0 dB |
| Peaking | 3765 Hz  | 0.93 | 6.7 dB  |
| Peaking | 271 Hz   | 4.53 | -1.0 dB |
| Peaking | 1367 Hz  | 5.76 | -0.8 dB |
| Peaking | 5446 Hz  | 5.94 | 2.2 dB  |
| Peaking | 8479 Hz  | 2.27 | -1.5 dB |
| Peaking | 13551 Hz | 5.3  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20C%20Flow/MrSpeakers%20Ether%20C%20Flow.png)