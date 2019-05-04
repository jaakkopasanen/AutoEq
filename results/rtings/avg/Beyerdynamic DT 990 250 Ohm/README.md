# Beyerdynamic DT 990 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.3; 31 -2.9; 34 -3.4; 37 -3.8; 41 -4.2; 45 -4.5; 49 -4.8; 54 -5.1; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.4; 87 -6.8; 96 -7.1; 106 -7.3; 116 -7.5; 128 -7.7; 141 -7.8; 155 -7.7; 170 -7.6; 187 -7.4; 206 -7.1; 227 -6.7; 249 -6.3; 274 -5.9; 302 -5.6; 332 -5.2; 365 -4.8; 402 -4.5; 442 -4.6; 486 -5.1; 535 -4.7; 588 -4.1; 647 -3.7; 712 -3.4; 783 -3.2; 861 -3.1; 947 -3.2; 1042 -3.2; 1146 -3.1; 1261 -3.2; 1387 -3.3; 1526 -3.6; 1678 -4.3; 1846 -5.3; 2031 -5.8; 2234 -5.8; 2457 -5.4; 2703 -5.6; 2973 -5.5; 3270 -4.9; 3597 -3.4; 3957 -1.4; 4353 -4.7; 4788 -7.0; 5267 -5.7; 5793 -5.4; 6373 -7.4; 7010 -7.0; 7711 -7.9; 8482 -10.9; 9330 -10.3; 10263 -7.2; 11289 -7.5; 12418 -9.9; 13660 -11.1; 15026 -10.1; 16529 -8.7; 18182 -10.8; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.94 | 5.0 dB  |
| Peaking | 996 Hz   | 1.14 | 2.8 dB  |
| Peaking | 3880 Hz  | 5.98 | 5.2 dB  |
| Peaking | 12632 Hz | 0.46 | -3.8 dB |
| Peaking | 19886 Hz | 1.16 | -9.9 dB |
| Peaking | 139 Hz   | 1.22 | -2.6 dB |
| Peaking | 5671 Hz  | 8.64 | 1.8 dB  |
| Peaking | 8848 Hz  | 5.73 | -3.7 dB |
| Peaking | 10726 Hz | 3.3  | 3.0 dB  |
| Peaking | 13473 Hz | 3.58 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20990%20250%20Ohm/Beyerdynamic%20DT%20990%20250%20Ohm.png)