# Beyerdynamic DT 1990
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.2; 25 -1.3; 28 -1.4; 31 -1.6; 34 -1.6; 37 -1.7; 41 -1.7; 45 -1.7; 49 -1.8; 54 -1.9; 60 -2.1; 66 -2.3; 72 -2.5; 79 -2.8; 87 -3.2; 96 -3.7; 106 -4.1; 116 -4.5; 128 -4.8; 141 -5.1; 155 -5.4; 170 -5.5; 187 -5.4; 206 -5.3; 227 -5.2; 249 -5.1; 274 -5.0; 302 -4.9; 332 -4.7; 365 -4.5; 402 -4.4; 442 -4.2; 486 -4.0; 535 -3.6; 588 -3.2; 647 -2.9; 712 -2.4; 783 -2.0; 861 -1.4; 947 -0.9; 1042 -0.5; 1146 -0.5; 1261 -0.7; 1387 -1.0; 1526 -1.2; 1678 -1.6; 1846 -2.0; 2031 -2.0; 2234 -1.7; 2457 -1.8; 2703 -1.6; 2973 -1.6; 3270 -2.3; 3597 -2.9; 3957 -2.2; 4353 -1.3; 4788 -2.7; 5267 -3.2; 5793 -3.2; 6373 -5.7; 7010 -9.8; 7711 -12.5; 8482 -12.6; 9330 -9.3; 10263 -6.3; 11289 -6.9; 12418 -7.1; 13660 -5.7; 15026 -4.6; 16529 -4.8; 18182 -7.4; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.96 | 2.8 dB   |
| Peaking | 1171 Hz  | 1.4  | 3.3 dB   |
| Peaking | 5676 Hz  | 0.73 | 4.9 dB   |
| Peaking | 7940 Hz  | 1.65 | -12.7 dB |
| Peaking | 19914 Hz | 0.82 | -6.7 dB  |
| Peaking | 69 Hz    | 1.37 | 1.3 dB   |
| Peaking | 178 Hz   | 0.75 | -1.9 dB  |
| Peaking | 3047 Hz  | 1.41 | 1.0 dB   |
| Peaking | 3560 Hz  | 4.46 | -1.8 dB  |
| Peaking | 12454 Hz | 6.03 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%201990/Beyerdynamic%20DT%201990.png)