# Razer Man O' War
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -4.0; 25 -5.1; 28 -6.5; 31 -7.6; 34 -8.5; 37 -9.1; 41 -9.8; 45 -10.2; 49 -10.4; 54 -10.6; 60 -10.7; 66 -10.7; 72 -10.8; 79 -11.0; 87 -11.2; 96 -11.3; 106 -11.5; 116 -11.6; 128 -11.7; 141 -11.7; 155 -11.6; 170 -11.3; 187 -10.7; 206 -10.4; 227 -11.4; 249 -11.2; 274 -10.4; 302 -9.5; 332 -8.3; 365 -7.5; 402 -7.5; 442 -7.8; 486 -7.4; 535 -5.4; 588 -3.9; 647 -4.3; 712 -5.6; 783 -5.5; 861 -4.9; 947 -4.5; 1042 -4.3; 1146 -4.1; 1261 -3.8; 1387 -3.4; 1526 -3.2; 1678 -3.4; 1846 -3.3; 2031 -2.6; 2234 -0.9; 2457 -2.0; 2703 -3.4; 2973 -3.7; 3270 -2.8; 3597 -0.5; 3957 -1.1; 4353 -4.3; 4788 -5.2; 5267 -5.3; 5793 -4.9; 6373 -4.7; 7010 -3.8; 7711 -7.6; 8482 -10.5; 9330 -8.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -7.5; 15026 -10.7; 16529 -9.8; 18182 -7.8; 20000 -8.3
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
| Peaking | 53 Hz    | 1.49 | -3.1 dB |
| Peaking | 124 Hz   | 0.86 | -5.1 dB |
| Peaking | 252 Hz   | 2.27 | -3.2 dB |
| Peaking | 1872 Hz  | 0.7  | 3.7 dB  |
| Peaking | 3746 Hz  | 5.37 | 4.6 dB  |
| Peaking | 599 Hz   | 7.38 | 2.5 dB  |
| Peaking | 6885 Hz  | 5.47 | 2.9 dB  |
| Peaking | 8435 Hz  | 5.06 | -5.2 dB |
| Peaking | 15620 Hz | 2.51 | -4.7 dB |
| Peaking | 19634 Hz | 0.76 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Man%20O'%20War/Razer%20Man%20O'%20War.png)