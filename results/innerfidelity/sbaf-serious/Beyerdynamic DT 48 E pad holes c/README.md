# Beyerdynamic DT 48 E pad holes c
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.4; 72 -8.3; 79 -12.5; 87 -9.8; 96 -8.5; 106 -10.8; 116 -10.2; 128 -9.6; 141 -9.1; 155 -8.3; 170 -9.1; 187 -8.9; 206 -8.4; 227 -7.6; 249 -7.0; 274 -6.3; 302 -5.7; 332 -5.1; 365 -4.5; 402 -3.6; 442 -2.4; 486 -1.4; 535 -0.5; 588 -0.5; 647 -0.5; 712 -2.2; 783 -3.9; 861 -5.9; 947 -7.6; 1042 -9.3; 1146 -10.3; 1261 -10.7; 1387 -11.3; 1526 -12.2; 1678 -13.3; 1846 -13.6; 2031 -13.5; 2234 -12.3; 2457 -9.3; 2703 -6.6; 2973 -5.2; 3270 -4.9; 3597 -3.7; 3957 -2.3; 4353 -1.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -11.6; 8482 -16.0; 9330 -13.3; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -7.2; 15026 -13.0; 16529 -15.2; 18182 -12.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 E pad holes c GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E pad holes c ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.51 | 7.5 dB   |
| Peaking | 1811 Hz  | 0.95 | -18.2 dB |
| Peaking | 4051 Hz  | 0.14 | 11.1 dB  |
| Peaking | 8619 Hz  | 3.02 | -17.7 dB |
| Peaking | 16382 Hz | 0.88 | -13.7 dB |
| Peaking | 62 Hz    | 2.34 | 7.0 dB   |
| Peaking | 76 Hz    | 4.76 | -9.7 dB  |
| Peaking | 112 Hz   | 2.7  | -4.0 dB  |
| Peaking | 192 Hz   | 1.51 | -3.0 dB  |
| Peaking | 560 Hz   | 2.79 | 4.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 7.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -9.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -8.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20E%20pad%20holes%20c/Beyerdynamic%20DT%2048%20E%20pad%20holes%20c.png)