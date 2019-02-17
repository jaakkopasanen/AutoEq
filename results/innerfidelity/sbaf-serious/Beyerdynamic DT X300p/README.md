# Beyerdynamic DT X300p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.1; 96 -2.2; 106 -2.8; 116 -3.6; 128 -4.1; 141 -4.3; 155 -4.9; 170 -5.0; 187 -5.3; 206 -5.5; 227 -5.6; 249 -5.7; 274 -5.5; 302 -5.5; 332 -5.6; 365 -6.4; 402 -6.5; 442 -6.6; 486 -7.8; 535 -7.8; 588 -7.6; 647 -7.3; 712 -7.1; 783 -6.6; 861 -6.5; 947 -6.4; 1042 -6.4; 1146 -6.3; 1261 -6.2; 1387 -6.2; 1526 -5.5; 1678 -4.5; 1846 -4.1; 2031 -3.1; 2234 -1.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT X300p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X300p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.32 | 6.0 dB  |
| Peaking | 79 Hz   | 1.96 | 2.2 dB  |
| Peaking | 579 Hz  | 1.82 | -1.6 dB |
| Peaking | 2968 Hz | 1.23 | 6.2 dB  |
| Peaking | 5477 Hz | 2.28 | 5.0 dB  |
| Peaking | 1360 Hz | 3.61 | -0.9 dB |
| Peaking | 2325 Hz | 7.63 | 1.1 dB  |
| Peaking | 6517 Hz | 6.42 | 2.0 dB  |
| Peaking | 6697 Hz | 4.47 | 0.6 dB  |
| Peaking | 7720 Hz | 2.03 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X300p/Beyerdynamic%20DT%20X300p.png)