# MrSpeakers Aeon Flow Closed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.0; 25 -5.9; 28 -5.8; 31 -5.6; 34 -5.4; 37 -5.2; 41 -4.9; 45 -4.6; 49 -4.3; 54 -3.9; 60 -3.5; 66 -3.6; 72 -4.0; 79 -4.4; 87 -4.1; 96 -4.0; 106 -3.8; 116 -3.3; 128 -3.0; 141 -2.9; 155 -2.6; 170 -2.5; 187 -2.7; 206 -3.0; 227 -3.2; 249 -3.3; 274 -3.4; 302 -3.7; 332 -4.3; 365 -4.8; 402 -5.4; 442 -5.7; 486 -5.7; 535 -5.8; 588 -5.7; 647 -5.8; 712 -6.4; 783 -6.8; 861 -7.4; 947 -7.8; 1042 -6.7; 1146 -6.6; 1261 -6.2; 1387 -5.4; 1526 -4.9; 1678 -4.2; 1846 -3.8; 2031 -2.9; 2234 -3.1; 2457 -3.8; 2703 -3.7; 2973 -0.5; 3270 -0.9; 3597 -1.5; 3957 -2.7; 4353 -4.8; 4788 -5.0; 5267 -8.2; 5793 -10.3; 6373 -6.5; 7010 -2.2; 7711 -3.9; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -7.7; 12418 -7.6; 13660 -5.0; 15026 -5.6; 16529 -9.4; 18182 -11.2; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 896 Hz   | 1.5  | -3.4 dB |
| Peaking | 3237 Hz  | 2.63 | 3.9 dB  |
| Peaking | 5678 Hz  | 6.07 | -7.0 dB |
| Peaking | 17449 Hz | 2.34 | -2.4 dB |
| Peaking | 19498 Hz | 0.56 | -6.8 dB |
| Peaking | 24 Hz    | 1.49 | -1.9 dB |
| Peaking | 167 Hz   | 1.53 | 1.9 dB  |
| Peaking | 2015 Hz  | 6.89 | 1.3 dB  |
| Peaking | 7043 Hz  | 8.8  | 3.1 dB  |
| Peaking | 11770 Hz | 6.99 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Aeon%20Flow%20Closed/MrSpeakers%20Aeon%20Flow%20Closed.png)