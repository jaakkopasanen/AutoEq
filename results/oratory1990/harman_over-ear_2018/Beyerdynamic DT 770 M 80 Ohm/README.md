# Beyerdynamic DT 770 M 80 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.9; 96 -7.7; 106 -12.9; 116 -14.4; 128 -13.3; 141 -12.1; 155 -11.7; 170 -11.1; 187 -10.6; 206 -10.2; 227 -9.8; 249 -9.5; 274 -9.0; 302 -8.5; 332 -8.0; 365 -7.6; 402 -7.2; 442 -6.9; 486 -6.6; 535 -6.2; 588 -5.8; 647 -5.6; 712 -5.4; 783 -5.4; 861 -5.4; 947 -5.4; 1042 -5.5; 1146 -5.9; 1261 -6.1; 1387 -6.2; 1526 -6.3; 1678 -6.7; 1846 -7.4; 2031 -7.6; 2234 -7.0; 2457 -6.3; 2703 -5.8; 2973 -4.7; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -1.6; 5267 -1.5; 5793 -1.1; 6373 -5.1; 7010 -7.4; 7711 -8.6; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -7.7; 12418 -11.7; 13660 -10.7; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 M 80 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 M 80 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 79 Hz    | 0.48 | 21.6 dB  |
| Peaking | 116 Hz   | 0.79 | -25.4 dB |
| Peaking | 3779 Hz  | 2.55 | 7.0 dB   |
| Peaking | 5469 Hz  | 3.01 | 6.1 dB   |
| Peaking | 9645 Hz  | 0.37 | -2.3 dB  |
| Peaking | 21 Hz    | 2.36 | 2.0 dB   |
| Peaking | 775 Hz   | 1.8  | 1.8 dB   |
| Peaking | 10642 Hz | 2.16 | 6.3 dB   |
| Peaking | 12650 Hz | 1.22 | -8.7 dB  |
| Peaking | 15125 Hz | 1.3  | 5.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 8.5 dB  |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20770%20M%2080%20Ohm/Beyerdynamic%20DT%20770%20M%2080%20Ohm.png)