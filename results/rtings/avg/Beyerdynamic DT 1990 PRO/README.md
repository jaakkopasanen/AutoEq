# Beyerdynamic DT 1990 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.5; 25 -1.6; 28 -1.8; 31 -1.9; 34 -1.9; 37 -2.0; 41 -2.0; 45 -2.0; 49 -2.1; 54 -2.2; 60 -2.4; 66 -2.6; 72 -2.9; 79 -3.2; 87 -3.6; 96 -4.0; 106 -4.4; 116 -4.8; 128 -5.2; 141 -5.5; 155 -5.7; 170 -5.8; 187 -5.8; 206 -5.6; 227 -5.4; 249 -5.3; 274 -5.2; 302 -5.0; 332 -4.9; 365 -4.7; 402 -4.5; 442 -4.3; 486 -4.1; 535 -3.7; 588 -3.3; 647 -2.9; 712 -2.4; 783 -2.0; 861 -1.4; 947 -1.0; 1042 -0.5; 1146 -0.5; 1261 -0.7; 1387 -0.9; 1526 -1.1; 1678 -1.5; 1846 -1.7; 2031 -1.7; 2234 -1.0; 2457 -0.9; 2703 -1.2; 2973 -1.6; 3270 -2.6; 3597 -3.2; 3957 -2.7; 4353 -1.7; 4788 -2.5; 5267 -2.8; 5793 -3.3; 6373 -6.7; 7010 -9.7; 7711 -11.8; 8482 -13.1; 9330 -11.1; 10263 -7.0; 11289 -6.0; 12418 -7.0; 13660 -6.6; 15026 -5.4; 16529 -5.3; 18182 -7.6; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 138 Hz   | 2.37 | -0.3 dB  |
| Peaking | 202 Hz   | 0.44 | -5.0 dB  |
| Peaking | 3506 Hz  | 5.95 | -1.5 dB  |
| Peaking | 8296 Hz  | 1.92 | -11.8 dB |
| Peaking | 20604 Hz | 0.19 | -8.8 dB  |
| Peaking | 1076 Hz  | 3.79 | 1.3 dB   |
| Peaking | 6105 Hz  | 2.3  | 2.0 dB   |
| Peaking | 6748 Hz  | 5.06 | -3.0 dB  |
| Peaking | 13014 Hz | 4.03 | -2.1 dB  |
| Peaking | 16436 Hz | 2.38 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%201990%20PRO/Beyerdynamic%20DT%201990%20PRO.png)