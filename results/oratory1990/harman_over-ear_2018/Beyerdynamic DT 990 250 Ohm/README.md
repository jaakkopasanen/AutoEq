# Beyerdynamic DT 990 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.4; 31 -3.0; 34 -3.5; 37 -4.0; 41 -4.5; 45 -5.0; 49 -5.4; 54 -5.9; 60 -6.3; 66 -6.6; 72 -7.0; 79 -7.2; 87 -7.1; 96 -7.1; 106 -7.9; 116 -8.3; 128 -8.5; 141 -8.5; 155 -8.4; 170 -8.3; 187 -8.1; 206 -8.0; 227 -7.4; 249 -7.0; 274 -6.4; 302 -5.8; 332 -5.2; 365 -4.5; 402 -4.1; 442 -4.7; 486 -4.3; 535 -3.8; 588 -3.4; 647 -3.1; 712 -3.0; 783 -3.1; 861 -3.6; 947 -4.6; 1042 -5.1; 1146 -5.4; 1261 -5.8; 1387 -5.7; 1526 -5.3; 1678 -5.1; 1846 -5.0; 2031 -5.0; 2234 -5.4; 2457 -6.2; 2703 -7.1; 2973 -7.4; 3270 -6.7; 3597 -6.2; 3957 -7.0; 4353 -7.2; 4788 -8.0; 5267 -9.9; 5793 -12.6; 6373 -10.6; 7010 -7.6; 7711 -10.4; 8482 -11.8; 9330 -9.4; 10263 -9.3; 11289 -13.7; 12418 -18.0; 13660 -16.5; 15026 -13.8; 16529 -16.2; 18182 -19.9; 20000 -20.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.68 | 4.6 dB   |
| Peaking | 134 Hz   | 0.97 | -3.9 dB  |
| Peaking | 5786 Hz  | 2.37 | -5.3 dB  |
| Peaking | 12561 Hz | 3.22 | -7.6 dB  |
| Peaking | 19553 Hz | 0.34 | -16.2 dB |
| Peaking | 241 Hz   | 1.6  | -2.2 dB  |
| Peaking | 316 Hz   | 0.74 | 2.1 dB   |
| Peaking | 713 Hz   | 2.04 | 2.5 dB   |
| Peaking | 905 Hz   | 0.29 | -0.8 dB  |
| Peaking | 17933 Hz | 3.36 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 16000 Hz | 1.41 | -18.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20990%20250%20Ohm/Beyerdynamic%20DT%20990%20250%20Ohm.png)