# Beyerdynamic DT X 350 m
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.9; 25 -3.3; 28 -3.7; 31 -4.1; 34 -4.4; 37 -4.6; 41 -4.7; 45 -4.7; 49 -5.1; 54 -5.8; 60 -6.1; 66 -6.2; 72 -6.1; 79 -5.5; 87 -5.1; 96 -6.0; 106 -7.2; 116 -8.5; 128 -9.5; 141 -9.4; 155 -8.4; 170 -6.5; 187 -5.6; 206 -3.7; 227 -2.0; 249 -1.7; 274 -1.9; 302 -2.4; 332 -3.4; 365 -4.8; 402 -5.3; 442 -5.5; 486 -5.8; 535 -6.2; 588 -6.0; 647 -6.3; 712 -6.6; 783 -6.6; 861 -6.9; 947 -7.0; 1042 -7.0; 1146 -6.8; 1261 -6.8; 1387 -7.0; 1526 -7.0; 1678 -7.4; 1846 -7.6; 2031 -8.3; 2234 -8.0; 2457 -7.2; 2703 -6.4; 2973 -5.5; 3270 -4.1; 3597 -0.5; 3957 -4.1; 4353 -9.2; 4788 -6.6; 5267 -3.6; 5793 -4.8; 6373 -6.7; 7010 -7.6; 7711 -7.3; 8482 -8.2; 9330 -8.2; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.4; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT X 350 m GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X 350 m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.55 | 4.7 dB  |
| Peaking | 138 Hz  | 2.57 | -4.6 dB |
| Peaking | 257 Hz  | 1.76 | 5.2 dB  |
| Peaking | 2491 Hz | 0.26 | -1.3 dB |
| Peaking | 3610 Hz | 6.47 | 7.5 dB  |
| Peaking | 88 Hz   | 7.71 | 1.3 dB  |
| Peaking | 3860 Hz | 9.24 | 2.8 dB  |
| Peaking | 4258 Hz | 5.83 | -4.4 dB |
| Peaking | 5341 Hz | 5.81 | 4.2 dB  |
| Peaking | 8739 Hz | 5.4  | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X%20350%20m/Beyerdynamic%20DT%20X%20350%20m.png)