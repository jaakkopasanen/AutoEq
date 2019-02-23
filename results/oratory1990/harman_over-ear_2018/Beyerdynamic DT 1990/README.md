# Beyerdynamic DT 1990
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.4; 25 -1.6; 28 -2.0; 31 -2.2; 34 -2.5; 37 -2.7; 41 -2.9; 45 -3.2; 49 -3.4; 54 -3.7; 60 -3.9; 66 -4.2; 72 -4.5; 79 -4.9; 87 -5.2; 96 -5.6; 106 -6.0; 116 -6.5; 128 -7.0; 141 -7.4; 155 -7.7; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.3; 249 -8.3; 274 -8.1; 302 -7.8; 332 -7.6; 365 -7.2; 402 -7.0; 442 -6.8; 486 -6.6; 535 -6.2; 588 -5.9; 647 -5.7; 712 -5.5; 783 -5.3; 861 -5.1; 947 -5.1; 1042 -5.2; 1146 -5.4; 1261 -5.6; 1387 -5.8; 1526 -5.8; 1678 -5.8; 1846 -5.5; 2031 -5.0; 2234 -4.9; 2457 -5.5; 2703 -6.1; 2973 -5.2; 3270 -3.9; 3597 -3.1; 3957 -1.5; 4353 -0.5; 4788 -3.8; 5267 -7.0; 5793 -7.3; 6373 -6.5; 7010 -12.0; 7711 -15.5; 8482 -13.5; 9330 -8.5; 10263 -7.0; 11289 -9.1; 12418 -11.5; 13660 -13.8; 15026 -15.4; 16529 -14.7; 18182 -12.4; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.13 | 5.2 dB  |
| Peaking | 53 Hz    | 1.83 | 2.2 dB  |
| Peaking | 4122 Hz  | 2.57 | 6.3 dB  |
| Peaking | 7752 Hz  | 4.68 | -9.2 dB |
| Peaking | 16171 Hz | 0.83 | -9.3 dB |
| Peaking | 228 Hz   | 1.2  | -2.1 dB |
| Peaking | 879 Hz   | 1.27 | 1.5 dB  |
| Peaking | 2100 Hz  | 4.72 | 1.2 dB  |
| Peaking | 10273 Hz | 3.4  | 4.5 dB  |
| Peaking | 10790 Hz | 0.9  | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | 1.9 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 16000 Hz | 1.41 | -10.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%201990/Beyerdynamic%20DT%201990.png)