# Focal Elex
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.1; 28 -1.3; 31 -1.3; 34 -1.4; 37 -1.7; 41 -1.9; 45 -2.1; 49 -2.3; 54 -2.5; 60 -2.8; 66 -3.1; 72 -3.4; 79 -3.7; 87 -4.1; 96 -4.4; 106 -4.7; 116 -4.9; 128 -5.1; 141 -5.3; 155 -5.3; 170 -5.4; 187 -5.3; 206 -5.3; 227 -5.2; 249 -5.0; 274 -4.7; 302 -4.4; 332 -4.1; 365 -3.9; 402 -3.8; 442 -3.7; 486 -3.7; 535 -3.6; 588 -3.5; 647 -3.6; 712 -3.8; 783 -4.1; 861 -4.6; 947 -4.9; 1042 -5.5; 1146 -5.9; 1261 -6.3; 1387 -6.1; 1526 -5.6; 1678 -4.3; 1846 -2.9; 2031 -1.7; 2234 -1.2; 2457 -1.5; 2703 -2.2; 2973 -3.1; 3270 -3.6; 3597 -4.0; 3957 -2.7; 4353 -1.8; 4788 -2.9; 5267 -4.5; 5793 -6.2; 6373 -1.8; 7010 -2.7; 7711 -5.0; 8482 -5.2; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -9.5; 20000 -20.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elex GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elex ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.53 | 4.6 dB   |
| Peaking | 53 Hz    | 1.37 | 1.1 dB   |
| Peaking | 2321 Hz  | 2.56 | 4.3 dB   |
| Peaking | 4308 Hz  | 4.95 | 3.4 dB   |
| Peaking | 6643 Hz  | 8.72 | 4.2 dB   |
| Peaking | 590 Hz   | 1.03 | 2.1 dB   |
| Peaking | 1521 Hz  | 1.15 | -2.6 dB  |
| Peaking | 1829 Hz  | 2.99 | 2.5 dB   |
| Peaking | 2966 Hz  | 3.69 | 0.8 dB   |
| Peaking | 19822 Hz | 1.71 | -15.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elex/Focal%20Elex.png)