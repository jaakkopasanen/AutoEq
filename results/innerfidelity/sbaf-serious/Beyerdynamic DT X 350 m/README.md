# Beyerdynamic DT X 350 m
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.2; 25 -2.6; 28 -3.1; 31 -3.4; 34 -3.7; 37 -3.9; 41 -4.0; 45 -4.1; 49 -4.5; 54 -5.1; 60 -5.4; 66 -5.5; 72 -5.5; 79 -4.9; 87 -4.5; 96 -5.3; 106 -6.6; 116 -7.8; 128 -8.9; 141 -8.7; 155 -7.7; 170 -5.9; 187 -4.9; 206 -3.1; 227 -1.4; 249 -1.0; 274 -1.3; 302 -1.7; 332 -2.8; 365 -4.1; 402 -4.7; 442 -4.9; 486 -5.2; 535 -5.5; 588 -5.4; 647 -5.6; 712 -6.0; 783 -6.0; 861 -6.2; 947 -6.3; 1042 -6.3; 1146 -6.2; 1261 -6.2; 1387 -6.3; 1526 -6.3; 1678 -6.8; 1846 -6.9; 2031 -7.7; 2234 -7.4; 2457 -6.5; 2703 -5.7; 2973 -4.8; 3270 -3.4; 3597 -0.5; 3957 -3.4; 4353 -8.6; 4788 -5.9; 5267 -2.9; 5793 -4.1; 6373 -6.1; 7010 -6.9; 7711 -6.7; 8482 -7.5; 9330 -7.6; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT X 350 m GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X 350 m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 137 Hz   | 2.76 | -4.3 dB |
| Peaking | 258 Hz   | 1.58 | 5.7 dB  |
| Peaking | 3598 Hz  | 6.69 | 6.5 dB  |
| Peaking | 19974 Hz | 2.32 | -2.5 dB |
| Peaking | 17 Hz    | 0.56 | 4.7 dB  |
| Peaking | 87 Hz    | 5.31 | 1.7 dB  |
| Peaking | 2078 Hz  | 5.4  | -1.6 dB |
| Peaking | 4378 Hz  | 9.79 | -3.8 dB |
| Peaking | 5385 Hz  | 6.71 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 5.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X%20350%20m/Beyerdynamic%20DT%20X%20350%20m.png)