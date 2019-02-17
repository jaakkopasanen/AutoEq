# MrSpeakers Ether C 1 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.9; 25 -4.0; 28 -4.0; 31 -3.8; 34 -3.6; 37 -3.3; 41 -2.9; 45 -2.2; 49 -2.1; 54 -3.1; 60 -3.8; 66 -3.6; 72 -2.6; 79 -2.9; 87 -3.9; 96 -4.0; 106 -4.5; 116 -4.1; 128 -4.2; 141 -3.5; 155 -2.6; 170 -3.5; 187 -4.5; 206 -4.9; 227 -5.3; 249 -5.6; 274 -5.7; 302 -5.9; 332 -5.8; 365 -5.5; 402 -4.9; 442 -4.3; 486 -4.1; 535 -4.6; 588 -4.9; 647 -5.2; 712 -5.5; 783 -5.7; 861 -6.3; 947 -6.6; 1042 -6.1; 1146 -5.4; 1261 -5.5; 1387 -5.6; 1526 -5.8; 1678 -6.3; 1846 -5.8; 2031 -5.2; 2234 -5.1; 2457 -5.1; 2703 -5.0; 2973 -4.7; 3270 -4.9; 3597 -4.5; 3957 -4.1; 4353 -4.5; 4788 -3.5; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C 1 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.57 | 2.3 dB  |
| Peaking | 52 Hz   | 0.61 | 3.6 dB  |
| Peaking | 159 Hz  | 3.73 | 2.8 dB  |
| Peaking | 500 Hz  | 1.71 | 2.0 dB  |
| Peaking | 5637 Hz | 2.25 | 6.2 dB  |
| Peaking | 2263 Hz | 3.88 | 0.5 dB  |
| Peaking | 4809 Hz | 2.31 | -3.2 dB |
| Peaking | 5249 Hz | 0.74 | 2.9 dB  |
| Peaking | 7658 Hz | 4.93 | -1.9 dB |
| Peaking | 9034 Hz | 1.23 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | 2.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%201%20Black%20Filter/MrSpeakers%20Ether%20C%201%20Black%20Filter.png)