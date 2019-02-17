# Beyerdynamic DT 770 M 80 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -2.9; 96 -8.8; 106 -14.2; 116 -15.6; 128 -14.6; 141 -13.4; 155 -13.1; 170 -12.5; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.7; 274 -10.2; 302 -9.7; 332 -9.2; 365 -8.8; 402 -8.4; 442 -8.0; 486 -7.7; 535 -7.3; 588 -6.9; 647 -6.7; 712 -6.5; 783 -6.5; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -7.0; 1261 -7.3; 1387 -7.3; 1526 -7.5; 1678 -7.9; 1846 -8.4; 2031 -8.5; 2234 -7.9; 2457 -7.2; 2703 -6.7; 2973 -5.7; 3270 -2.3; 3597 -0.5; 3957 -0.6; 4353 -2.5; 4788 -3.0; 5267 -2.8; 5793 -2.0; 6373 -6.5; 7010 -8.5; 7711 -9.4; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -8.3; 12418 -12.3; 13660 -11.5; 15026 -7.6; 16529 -6.8; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 M 80 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 M 80 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 75 Hz    | 0.53 | 20.9 dB  |
| Peaking | 117 Hz   | 0.77 | -24.6 dB |
| Peaking | 3739 Hz  | 2.83 | 8.5 dB   |
| Peaking | 5523 Hz  | 3.25 | 6.0 dB   |
| Peaking | 7828 Hz  | 0.25 | -2.9 dB  |
| Peaking | 20 Hz    | 1.14 | 2.4 dB   |
| Peaking | 57 Hz    | 3.88 | -1.7 dB  |
| Peaking | 750 Hz   | 2.02 | 1.3 dB   |
| Peaking | 10193 Hz | 3.52 | 3.4 dB   |
| Peaking | 12787 Hz | 4.09 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 8.8 dB  |
| Peaking | 125 Hz   | 1.41 | -9.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20770%20M%2080%20Ohm/Beyerdynamic%20DT%20770%20M%2080%20Ohm.png)