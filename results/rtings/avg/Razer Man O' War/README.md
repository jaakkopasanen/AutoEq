# Razer Man O' War
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.8; 25 -5.9; 28 -7.3; 31 -8.4; 34 -9.2; 37 -9.8; 41 -10.5; 45 -10.9; 49 -11.1; 54 -11.2; 60 -11.3; 66 -11.5; 72 -11.6; 79 -11.7; 87 -11.9; 96 -12.1; 106 -12.2; 116 -12.4; 128 -12.5; 141 -12.5; 155 -12.4; 170 -12.0; 187 -11.4; 206 -11.0; 227 -12.1; 249 -11.7; 274 -11.0; 302 -10.1; 332 -8.9; 365 -8.1; 402 -8.1; 442 -8.3; 486 -7.9; 535 -5.8; 588 -4.4; 647 -4.6; 712 -6.0; 783 -5.9; 861 -5.4; 947 -5.0; 1042 -4.7; 1146 -4.5; 1261 -4.2; 1387 -3.8; 1526 -3.5; 1678 -3.7; 1846 -3.5; 2031 -2.8; 2234 -0.5; 2457 -1.7; 2703 -3.3; 2973 -4.1; 3270 -3.6; 3597 -1.2; 3957 -1.7; 4353 -5.3; 4788 -5.2; 5267 -5.4; 5793 -5.3; 6373 -6.3; 7010 -4.3; 7711 -7.2; 8482 -11.4; 9330 -10.6; 10263 -6.4; 11289 -4.8; 12418 -4.9; 13660 -8.5; 15026 -11.7; 16529 -10.6; 18182 -8.6; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Man O' War GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Man O' War ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 1.1  | -4.7 dB |
| Peaking | 119 Hz   | 0.78 | -6.4 dB |
| Peaking | 259 Hz   | 1.31 | -4.3 dB |
| Peaking | 16071 Hz | 0.72 | -5.8 dB |
| Peaking | 20467 Hz | 1.51 | -4.3 dB |
| Peaking | 3056 Hz  | 0.75 | 3.5 dB  |
| Peaking | 7164 Hz  | 5.23 | 4.0 dB  |
| Peaking | 8796 Hz  | 3.55 | -5.5 dB |
| Peaking | 9193 Hz  | 0.51 | -4.0 dB |
| Peaking | 11525 Hz | 1.75 | 7.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -7.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Man%20O'%20War/Razer%20Man%20O'%20War.png)