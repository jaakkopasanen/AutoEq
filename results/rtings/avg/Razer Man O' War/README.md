# Razer Man O' War
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -4.4; 25 -5.4; 28 -6.8; 31 -8.0; 34 -8.8; 37 -9.4; 41 -10.0; 45 -10.5; 49 -10.7; 54 -10.8; 60 -10.9; 66 -11.0; 72 -11.2; 79 -11.3; 87 -11.5; 96 -11.7; 106 -11.8; 116 -12.0; 128 -12.1; 141 -12.0; 155 -12.0; 170 -11.6; 187 -11.0; 206 -10.6; 227 -11.7; 249 -11.3; 274 -10.6; 302 -9.7; 332 -8.5; 365 -7.7; 402 -7.7; 442 -7.9; 486 -7.5; 535 -5.4; 588 -4.0; 647 -4.2; 712 -5.6; 783 -5.5; 861 -4.9; 947 -4.6; 1042 -4.3; 1146 -4.1; 1261 -3.8; 1387 -3.4; 1526 -3.1; 1678 -3.3; 1846 -3.1; 2031 -2.4; 2234 -0.5; 2457 -1.3; 2703 -2.9; 2973 -3.7; 3270 -3.2; 3597 -0.8; 3957 -1.2; 4353 -4.9; 4788 -4.8; 5267 -5.0; 5793 -4.9; 6373 -5.9; 7010 -4.2; 7711 -6.9; 8482 -11.0; 9330 -10.2; 10263 -6.6; 11289 -6.4; 12418 -6.4; 13660 -8.1; 15026 -11.2; 16529 -10.2; 18182 -8.2; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Man O' War GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Man O' War ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 1.37 | -3.3 dB |
| Peaking | 124 Hz   | 0.89 | -5.2 dB |
| Peaking | 251 Hz   | 2.28 | -3.2 dB |
| Peaking | 1943 Hz  | 0.76 | 4.3 dB  |
| Peaking | 3770 Hz  | 6.42 | 4.4 dB  |
| Peaking | 459 Hz   | 5.07 | -1.4 dB |
| Peaking | 588 Hz   | 5.15 | 2.7 dB  |
| Peaking | 7032 Hz  | 5.48 | 2.4 dB  |
| Peaking | 8728 Hz  | 5.09 | -5.8 dB |
| Peaking | 15741 Hz | 1.9  | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Man%20O'%20War/Razer%20Man%20O'%20War.png)