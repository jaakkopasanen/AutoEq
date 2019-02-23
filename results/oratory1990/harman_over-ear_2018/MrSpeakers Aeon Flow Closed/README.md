# MrSpeakers Aeon Flow Closed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.1; 25 -6.0; 28 -5.7; 31 -5.4; 34 -5.2; 37 -5.0; 41 -4.7; 45 -4.4; 49 -4.1; 54 -3.7; 60 -3.5; 66 -3.5; 72 -4.0; 79 -4.3; 87 -4.1; 96 -4.0; 106 -3.8; 116 -3.3; 128 -3.1; 141 -2.9; 155 -2.7; 170 -2.6; 187 -2.9; 206 -3.3; 227 -3.6; 249 -3.7; 274 -3.8; 302 -4.0; 332 -4.4; 365 -4.8; 402 -5.4; 442 -5.7; 486 -5.7; 535 -5.9; 588 -5.8; 647 -5.9; 712 -6.5; 783 -6.9; 861 -7.5; 947 -7.9; 1042 -6.8; 1146 -6.9; 1261 -6.4; 1387 -5.6; 1526 -5.2; 1678 -4.4; 1846 -4.2; 2031 -3.1; 2234 -2.9; 2457 -3.1; 2703 -3.8; 2973 -0.5; 3270 -1.2; 3597 -1.9; 3957 -2.6; 4353 -4.9; 4788 -5.4; 5267 -8.8; 5793 -9.7; 6373 -5.8; 7010 -2.1; 7711 -4.1; 8482 -4.4; 9330 -4.4; 10263 -4.5; 11289 -7.8; 12418 -8.1; 13660 -5.5; 15026 -5.4; 16529 -8.4; 18182 -10.4; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  2.29 | -1.8 dB |
| Peaking | 914 Hz   |  1.42 | -3.4 dB |
| Peaking | 3179 Hz  |  1.79 | 3.5 dB  |
| Peaking | 5530 Hz  |  6.22 | -7.1 dB |
| Peaking | 19485 Hz |  0.51 | -6.9 dB |
| Peaking | 60 Hz    |  4.3  | 1.0 dB  |
| Peaking | 163 Hz   |  1.64 | 1.9 dB  |
| Peaking | 6901 Hz  | 11.2  | 3.1 dB  |
| Peaking | 11941 Hz |  3.21 | -6.1 dB |
| Peaking | 12680 Hz |  1.25 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Aeon%20Flow%20Closed/MrSpeakers%20Aeon%20Flow%20Closed.png)