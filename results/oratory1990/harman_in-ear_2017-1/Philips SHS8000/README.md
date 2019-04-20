# Philips SHS8000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -2.0; 34 -2.2; 37 -2.5; 41 -2.8; 45 -3.1; 49 -3.3; 54 -3.6; 60 -4.0; 66 -4.3; 72 -4.7; 79 -5.0; 87 -5.5; 96 -5.9; 106 -6.2; 116 -6.6; 128 -6.8; 141 -7.1; 155 -7.2; 170 -7.2; 187 -7.2; 206 -7.1; 227 -6.9; 249 -6.7; 274 -6.5; 302 -6.2; 332 -5.7; 365 -5.4; 402 -5.2; 442 -4.9; 486 -4.5; 535 -4.1; 588 -3.7; 647 -3.4; 712 -3.0; 783 -2.8; 861 -2.7; 947 -2.9; 1042 -3.3; 1146 -3.7; 1261 -3.9; 1387 -4.0; 1526 -3.9; 1678 -3.9; 1846 -4.1; 2031 -4.3; 2234 -5.0; 2457 -6.3; 2703 -7.7; 2973 -7.6; 3270 -5.8; 3597 -4.2; 3957 -3.5; 4353 -3.7; 4788 -5.9; 5267 -7.1; 5793 -4.3; 6373 -1.7; 7010 -2.4; 7711 -4.6; 8482 -5.0; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -5.1; 15026 -15.8; 16529 -19.7; 18182 -13.9; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHS8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHS8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.55 | 4.5 dB   |
| Peaking | 159 Hz   | 1.1  | -2.8 dB  |
| Peaking | 2815 Hz  | 6.33 | -3.6 dB  |
| Peaking | 13481 Hz | 0.6  | 11.4 dB  |
| Peaking | 16120 Hz | 0.93 | -24.5 dB |
| Peaking | 851 Hz   | 1.35 | 2.3 dB   |
| Peaking | 4170 Hz  | 4.69 | 2.1 dB   |
| Peaking | 5218 Hz  | 4.24 | -3.6 dB  |
| Peaking | 6554 Hz  | 3.78 | 4.6 dB   |
| Peaking | 8119 Hz  | 1.63 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB   |
| Peaking | 62 Hz    | 1.41 | 0.5 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -14.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Philips%20SHS8000/Philips%20SHS8000.png)