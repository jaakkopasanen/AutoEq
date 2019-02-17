# MrSpeakers Aeon Flow Closed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.0; 25 -4.9; 28 -4.6; 31 -4.3; 34 -4.1; 37 -3.9; 41 -3.6; 45 -3.3; 49 -3.0; 54 -2.6; 60 -2.3; 66 -2.3; 72 -2.9; 79 -3.2; 87 -3.0; 96 -2.8; 106 -2.6; 116 -2.2; 128 -2.0; 141 -1.8; 155 -1.6; 170 -1.4; 187 -1.7; 206 -2.1; 227 -2.5; 249 -2.6; 274 -2.7; 302 -2.8; 332 -3.3; 365 -3.6; 402 -4.2; 442 -4.5; 486 -4.6; 535 -4.8; 588 -4.7; 647 -4.8; 712 -5.4; 783 -5.8; 861 -6.3; 947 -6.8; 1042 -5.7; 1146 -5.7; 1261 -5.3; 1387 -4.4; 1526 -4.0; 1678 -3.2; 1846 -3.1; 2031 -1.9; 2234 -1.7; 2457 -2.0; 2703 -2.7; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -1.4; 4353 -3.7; 4788 -4.2; 5267 -7.7; 5793 -8.5; 6373 -4.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -7.0; 13660 -6.5; 15026 -6.5; 16529 -7.3; 18182 -9.3; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Closed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.82 | 2.8 dB  |
| Peaking | 184 Hz   | 0.58 | 4.5 dB  |
| Peaking | 2083 Hz  | 1.8  | 3.8 dB  |
| Peaking | 3426 Hz  | 2.38 | 5.6 dB  |
| Peaking | 19389 Hz | 0.98 | -3.8 dB |
| Peaking | 619 Hz   | 5.04 | 0.6 dB  |
| Peaking | 917 Hz   | 5.88 | -1.3 dB |
| Peaking | 4981 Hz  | 3.71 | 2.1 dB  |
| Peaking | 5527 Hz  | 5.17 | -5.5 dB |
| Peaking | 6686 Hz  | 8.48 | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.6 dB  |
| Peaking | 250 Hz   | 1.41 | 3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Aeon%20Flow%20Closed/MrSpeakers%20Aeon%20Flow%20Closed.png)