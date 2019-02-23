# JBL Endurance Sprint
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.3; 25 -4.3; 28 -4.3; 31 -4.3; 34 -4.4; 37 -4.4; 41 -4.4; 45 -4.4; 49 -4.3; 54 -4.2; 60 -4.3; 66 -4.4; 72 -4.3; 79 -4.3; 87 -4.1; 96 -4.0; 106 -3.8; 116 -3.5; 128 -3.4; 141 -3.2; 155 -2.8; 170 -2.3; 187 -1.7; 206 -1.2; 227 -0.9; 249 -0.7; 274 -0.7; 302 -0.7; 332 -0.9; 365 -1.1; 402 -1.2; 442 -1.3; 486 -1.3; 535 -1.1; 588 -0.9; 647 -0.6; 712 -0.5; 783 -0.5; 861 -0.8; 947 -1.4; 1042 -2.1; 1146 -2.7; 1261 -3.2; 1387 -3.4; 1526 -2.9; 1678 -2.5; 1846 -2.8; 2031 -3.0; 2234 -2.5; 2457 -1.8; 2703 -2.0; 2973 -3.0; 3270 -3.8; 3597 -4.1; 3957 -4.7; 4353 -5.4; 4788 -6.0; 5267 -7.5; 5793 -9.0; 6373 -8.0; 7010 -6.7; 7711 -7.2; 8482 -7.4; 9330 -4.9; 10263 -3.0; 11289 -3.0; 12418 -4.0; 13660 -10.2; 15026 -17.7; 16529 -20.7; 18182 -16.5; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Endurance Sprint GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Endurance Sprint ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.23 | -1.6 dB  |
| Peaking | 260 Hz   | 0.91 | 3.2 dB   |
| Peaking | 729 Hz   | 1.75 | 2.3 dB   |
| Peaking | 5854 Hz  | 2.41 | -5.4 dB  |
| Peaking | 16877 Hz | 1.27 | -19.6 dB |
| Peaking | 1317 Hz  | 5.69 | -0.9 dB  |
| Peaking | 2533 Hz  | 5.37 | 1.6 dB   |
| Peaking | 8305 Hz  | 4.12 | -3.3 dB  |
| Peaking | 11689 Hz | 1.65 | 5.3 dB   |
| Peaking | 14905 Hz | 2.89 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB   |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -18.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Endurance%20Sprint/JBL%20Endurance%20Sprint.png)