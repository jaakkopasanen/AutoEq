# Beyerdynamic DT 770 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.5; 25 -10.7; 28 -11.0; 31 -11.3; 34 -11.4; 37 -11.5; 41 -11.6; 45 -11.6; 49 -11.6; 54 -11.4; 60 -11.2; 66 -10.8; 72 -10.3; 79 -9.4; 87 -7.6; 96 -4.8; 106 -3.4; 116 -6.9; 128 -9.9; 141 -9.4; 155 -8.1; 170 -6.0; 187 -3.2; 206 -1.1; 227 -1.0; 249 -1.9; 274 -2.8; 302 -3.5; 332 -3.9; 365 -4.2; 402 -4.4; 442 -4.5; 486 -4.7; 535 -4.7; 588 -4.5; 647 -4.3; 712 -4.4; 783 -4.8; 861 -5.7; 947 -6.4; 1042 -5.8; 1146 -4.9; 1261 -4.7; 1387 -4.8; 1526 -4.9; 1678 -4.6; 1846 -4.4; 2031 -5.2; 2234 -5.7; 2457 -5.5; 2703 -4.8; 2973 -2.5; 3270 -0.5; 3597 -1.1; 3957 -3.8; 4353 -4.7; 4788 -5.2; 5267 -6.8; 5793 -9.3; 6373 -10.4; 7010 -8.4; 7711 -8.3; 8482 -8.0; 9330 -6.7; 10263 -7.4; 11289 -11.2; 12418 -13.5; 13660 -11.5; 15026 -10.1; 16529 -12.6; 18182 -14.6; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.63 | -5.7 dB |
| Peaking | 246 Hz   | 1.58 | 5.3 dB  |
| Peaking | 3386 Hz  | 2.54 | 6.5 dB  |
| Peaking | 14133 Hz | 0.33 | -3.4 dB |
| Peaking | 19539 Hz | 0.61 | -7.2 dB |
| Peaking | 103 Hz   | 5.81 | 5.8 dB  |
| Peaking | 134 Hz   | 4.03 | -4.5 dB |
| Peaking | 6172 Hz  | 7.16 | -3.3 dB |
| Peaking | 9581 Hz  | 5.9  | 3.4 dB  |
| Peaking | 22049 Hz | 2.04 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 4.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -8.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20770%20250%20Ohm/Beyerdynamic%20DT%20770%20250%20Ohm.png)