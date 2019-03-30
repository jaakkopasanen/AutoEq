# Beyerdynamic DT 660 mk 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.6; 25 -4.0; 28 -4.4; 31 -4.5; 34 -4.4; 37 -4.2; 41 -4.3; 45 -5.2; 49 -6.6; 54 -8.4; 60 -10.0; 66 -11.3; 72 -12.5; 79 -13.5; 87 -13.9; 96 -13.9; 106 -13.4; 116 -12.7; 128 -11.7; 141 -10.7; 155 -9.7; 170 -8.1; 187 -5.7; 206 -2.7; 227 -0.5; 249 -0.5; 274 -1.9; 302 -3.2; 332 -4.0; 365 -4.4; 402 -4.6; 442 -5.0; 486 -5.9; 535 -6.9; 588 -7.3; 647 -6.6; 712 -5.3; 783 -4.5; 861 -4.3; 947 -3.9; 1042 -3.4; 1146 -2.8; 1261 -2.3; 1387 -2.2; 1526 -2.2; 1678 -2.4; 1846 -2.2; 2031 -2.3; 2234 -2.8; 2457 -3.4; 2703 -4.1; 2973 -4.5; 3270 -4.1; 3597 -3.5; 3957 -4.8; 4353 -7.2; 4788 -8.3; 5267 -8.6; 5793 -8.5; 6373 -6.9; 7010 -4.2; 7711 -4.9; 8482 -5.4; 9330 -6.6; 10263 -7.4; 11289 -8.5; 12418 -9.0; 13660 -8.1; 15026 -7.2; 16529 -6.6; 18182 -5.3; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 660 mk 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 660 mk 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 81 Hz    | 1.95 | -6.3 dB |
| Peaking | 125 Hz   | 1.23 | -6.1 dB |
| Peaking | 234 Hz   | 2.38 | 7.1 dB  |
| Peaking | 5302 Hz  | 4.64 | -3.9 dB |
| Peaking | 12590 Hz | 1.73 | -4.0 dB |
| Peaking | 24 Hz    | 1.12 | 2.1 dB  |
| Peaking | 586 Hz   | 3.76 | -2.8 dB |
| Peaking | 1337 Hz  | 1.22 | 2.5 dB  |
| Peaking | 2069 Hz  | 1.6  | 1.7 dB  |
| Peaking | 16213 Hz | 2.81 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | 6.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20660%20mk%202/Beyerdynamic%20DT%20660%20mk%202.png)