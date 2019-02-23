# Beyerdynamic DT X300p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.6; 79 -2.9; 87 -4.2; 96 -5.3; 106 -5.8; 116 -6.7; 128 -7.1; 141 -7.3; 155 -7.9; 170 -8.1; 187 -8.4; 206 -8.6; 227 -8.7; 249 -8.8; 274 -8.6; 302 -8.6; 332 -8.7; 365 -9.5; 402 -9.6; 442 -9.7; 486 -10.9; 535 -10.8; 588 -10.6; 647 -10.4; 712 -10.1; 783 -9.7; 861 -9.6; 947 -9.5; 1042 -9.5; 1146 -9.4; 1261 -9.3; 1387 -9.3; 1526 -8.6; 1678 -7.6; 1846 -7.2; 2031 -6.2; 2234 -4.6; 2457 -2.8; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -4.0; 5267 -2.5; 5793 -3.4; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT X300p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X300p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.28 | 7.8 dB  |
| Peaking | 126 Hz  | 0.86 | -5.0 dB |
| Peaking | 1129 Hz | 0.16 | -4.9 dB |
| Peaking | 3293 Hz | 0.96 | 10.7 dB |
| Peaking | 6440 Hz | 4.72 | 3.9 dB  |
| Peaking | 63 Hz   | 1.26 | -1.1 dB |
| Peaking | 65 Hz   | 3.38 | 1.9 dB  |
| Peaking | 524 Hz  | 5.7  | -0.9 dB |
| Peaking | 853 Hz  | 4.08 | 0.7 dB  |
| Peaking | 7819 Hz | 6.57 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X300p/Beyerdynamic%20DT%20X300p.png)