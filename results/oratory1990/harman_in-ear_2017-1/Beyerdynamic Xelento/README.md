# Beyerdynamic Xelento
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.8; 25 -13.7; 28 -13.6; 31 -13.6; 34 -13.5; 37 -13.4; 41 -13.2; 45 -13.1; 49 -12.9; 54 -12.8; 60 -12.7; 66 -12.6; 72 -12.5; 79 -12.4; 87 -12.2; 96 -12.2; 106 -12.1; 116 -12.1; 128 -11.9; 141 -11.6; 155 -11.4; 170 -11.9; 187 -12.0; 206 -11.5; 227 -10.9; 249 -10.4; 274 -9.8; 302 -9.3; 332 -8.8; 365 -8.5; 402 -8.1; 442 -7.7; 486 -7.3; 535 -6.9; 588 -6.6; 647 -6.3; 712 -6.0; 783 -5.6; 861 -5.6; 947 -5.8; 1042 -6.0; 1146 -6.3; 1261 -6.6; 1387 -6.5; 1526 -6.1; 1678 -5.5; 1846 -4.9; 2031 -4.2; 2234 -3.3; 2457 -2.6; 2703 -1.9; 2973 -1.4; 3270 -1.0; 3597 -1.0; 3957 -1.8; 4353 -3.2; 4788 -5.9; 5267 -8.0; 5793 -2.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -6.7; 9330 -9.2; 10263 -9.1; 11289 -7.8; 12418 -7.1; 13660 -8.6; 15026 -12.1; 16529 -13.0; 18182 -9.5; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.28 | -6.2 dB |
| Peaking | 203 Hz   | 0.93 | -2.9 dB |
| Peaking | 3240 Hz  | 1.45 | 5.3 dB  |
| Peaking | 16213 Hz | 1.2  | -7.5 dB |
| Peaking | 17 Hz    | 0.8  | -3.2 dB |
| Peaking | 4937 Hz  | 5.41 | -1.0 dB |
| Peaking | 5289 Hz  | 5.56 | -5.7 dB |
| Peaking | 6107 Hz  | 3.65 | 6.8 dB  |
| Peaking | 9577 Hz  | 4.15 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)