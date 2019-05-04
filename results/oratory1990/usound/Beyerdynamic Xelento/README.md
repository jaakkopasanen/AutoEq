# Beyerdynamic Xelento
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.1; 25 -12.0; 28 -11.9; 31 -11.8; 34 -11.7; 37 -11.6; 41 -11.5; 45 -11.3; 49 -11.2; 54 -11.1; 60 -10.9; 66 -10.8; 72 -10.7; 79 -10.6; 87 -10.5; 96 -10.5; 106 -10.4; 116 -10.3; 128 -10.2; 141 -9.9; 155 -9.7; 170 -10.1; 187 -10.3; 206 -9.7; 227 -9.1; 249 -8.6; 274 -8.1; 302 -7.6; 332 -7.2; 365 -7.1; 402 -6.7; 442 -6.3; 486 -5.9; 535 -5.6; 588 -5.4; 647 -5.1; 712 -4.7; 783 -4.4; 861 -4.2; 947 -4.4; 1042 -4.6; 1146 -5.0; 1261 -5.5; 1387 -5.7; 1526 -5.6; 1678 -5.1; 1846 -4.5; 2031 -4.1; 2234 -3.9; 2457 -3.7; 2703 -3.4; 2973 -3.1; 3270 -2.7; 3597 -2.4; 3957 -2.7; 4353 -3.8; 4788 -6.3; 5267 -8.2; 5793 -3.1; 6373 -0.5; 7010 -3.4; 7711 -5.8; 8482 -7.8; 9330 -7.6; 10263 -6.3; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.37 | -5.7 dB |
| Peaking | 92 Hz   | 0.55 | -2.5 dB |
| Peaking | 206 Hz  | 0.94 | -2.8 dB |
| Peaking | 1043 Hz | 0.18 | 1.3 dB  |
| Peaking | 3394 Hz | 2.25 | 2.7 dB  |
| Peaking | 848 Hz  | 3.09 | 0.9 dB  |
| Peaking | 1397 Hz | 4.19 | -1.3 dB |
| Peaking | 5310 Hz | 5.27 | -6.7 dB |
| Peaking | 6171 Hz | 3.14 | 7.0 dB  |
| Peaking | 8601 Hz | 2.86 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)