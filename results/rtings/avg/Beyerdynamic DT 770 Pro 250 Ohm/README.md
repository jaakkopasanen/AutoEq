# Beyerdynamic DT 770 Pro 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.6; 25 -6.9; 28 -7.2; 31 -7.5; 34 -7.5; 37 -7.5; 41 -7.3; 45 -7.0; 49 -6.7; 54 -6.2; 60 -5.9; 66 -5.8; 72 -5.8; 79 -5.8; 87 -6.0; 96 -6.2; 106 -6.4; 116 -6.4; 128 -6.1; 141 -5.5; 155 -4.6; 170 -3.5; 187 -2.5; 206 -2.1; 227 -2.5; 249 -3.0; 274 -3.8; 302 -4.4; 332 -4.8; 365 -5.1; 402 -5.5; 442 -5.9; 486 -6.0; 535 -5.9; 588 -5.9; 647 -5.7; 712 -5.6; 783 -5.6; 861 -5.5; 947 -5.3; 1042 -5.1; 1146 -5.1; 1261 -5.5; 1387 -6.0; 1526 -6.4; 1678 -6.8; 1846 -7.2; 2031 -7.9; 2234 -8.0; 2457 -7.3; 2703 -5.9; 2973 -4.1; 3270 -1.1; 3597 -0.5; 3957 -5.8; 4353 -9.0; 4788 -7.0; 5267 -5.0; 5793 -6.5; 6373 -10.3; 7010 -9.2; 7711 -10.4; 8482 -14.1; 9330 -13.8; 10263 -8.1; 11289 -6.0; 12418 -9.2; 13660 -12.8; 15026 -11.8; 16529 -11.3; 18182 -14.7; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 Pro 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 Pro 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 215 Hz   |  2.12 | 4.1 dB   |
| Peaking | 2151 Hz  |  3.5  | -2.4 dB  |
| Peaking | 3405 Hz  |  6.31 | 7.1 dB   |
| Peaking | 8577 Hz  |  3.55 | -7.8 dB  |
| Peaking | 19923 Hz |  0.37 | -11.2 dB |
| Peaking | 33 Hz    |  1.61 | -1.6 dB  |
| Peaking | 4319 Hz  | 10.16 | -3.5 dB  |
| Peaking | 11269 Hz |  5.31 | 4.0 dB   |
| Peaking | 13708 Hz |  3.86 | -3.7 dB  |
| Peaking | 22049 Hz |  1.69 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20770%20Pro%20250%20Ohm/Beyerdynamic%20DT%20770%20Pro%20250%20Ohm.png)