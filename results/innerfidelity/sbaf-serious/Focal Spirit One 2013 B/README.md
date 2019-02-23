# Focal Spirit One 2013 B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.1; 25 -10.0; 28 -9.8; 31 -9.7; 34 -9.5; 37 -9.3; 41 -9.1; 45 -8.9; 49 -8.7; 54 -8.6; 60 -8.6; 66 -8.2; 72 -7.7; 79 -7.2; 87 -8.5; 96 -11.1; 106 -11.3; 116 -10.9; 128 -10.7; 141 -11.1; 155 -10.8; 170 -10.6; 187 -10.5; 206 -10.1; 227 -9.5; 249 -8.9; 274 -8.2; 302 -8.1; 332 -8.2; 365 -8.6; 402 -9.1; 442 -9.1; 486 -9.1; 535 -8.8; 588 -8.4; 647 -8.1; 712 -8.0; 783 -7.4; 861 -7.3; 947 -7.0; 1042 -6.6; 1146 -6.2; 1261 -6.0; 1387 -6.1; 1526 -6.3; 1678 -6.2; 1846 -5.9; 2031 -5.4; 2234 -4.8; 2457 -3.9; 2703 -3.4; 2973 -3.4; 3270 -3.9; 3597 -4.8; 3957 -3.3; 4353 -6.3; 4788 -6.6; 5267 -2.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One 2013 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One 2013 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.89 | -3.6 dB |
| Peaking | 140 Hz  | 0.97 | -4.6 dB |
| Peaking | 497 Hz  | 1.43 | -2.2 dB |
| Peaking | 2810 Hz | 2.04 | 3.2 dB  |
| Peaking | 5986 Hz | 4.23 | 6.6 dB  |
| Peaking | 80 Hz   | 5.19 | 2.3 dB  |
| Peaking | 98 Hz   | 6.24 | -2.0 dB |
| Peaking | 4684 Hz | 5.74 | -4.5 dB |
| Peaking | 4724 Hz | 2.33 | 2.4 dB  |
| Peaking | 9577 Hz | 1.86 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%202013%20B/Focal%20Spirit%20One%202013%20B.png)