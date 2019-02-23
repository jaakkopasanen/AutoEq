# MrSpeakers Ether C 1 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.3; 25 -5.4; 28 -5.4; 31 -5.2; 34 -5.0; 37 -4.7; 41 -4.3; 45 -3.5; 49 -3.4; 54 -4.5; 60 -5.2; 66 -5.0; 72 -4.0; 79 -4.3; 87 -5.3; 96 -5.4; 106 -5.9; 116 -5.5; 128 -5.6; 141 -4.9; 155 -4.0; 170 -4.9; 187 -5.9; 206 -6.3; 227 -6.7; 249 -7.0; 274 -7.1; 302 -7.3; 332 -7.2; 365 -6.9; 402 -6.3; 442 -5.7; 486 -5.5; 535 -6.0; 588 -6.3; 647 -6.6; 712 -6.9; 783 -7.1; 861 -7.7; 947 -8.0; 1042 -7.5; 1146 -6.8; 1261 -6.8; 1387 -7.0; 1526 -7.1; 1678 -7.7; 1846 -7.2; 2031 -6.6; 2234 -6.5; 2457 -6.5; 2703 -6.4; 2973 -6.1; 3270 -6.2; 3597 -5.9; 3957 -5.5; 4353 -5.9; 4788 -4.8; 5267 -1.7; 5793 -0.6; 6373 -0.5; 7010 -3.3; 7711 -5.6; 8482 -6.5; 9330 -6.2; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C 1 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.68 | 2.7 dB  |
| Peaking | 158 Hz   | 5.33 | 2.6 dB  |
| Peaking | 391 Hz   | 0.05 | -1.1 dB |
| Peaking | 6008 Hz  | 2.62 | 6.8 dB  |
| Peaking | 8316 Hz  | 3.15 | -1.5 dB |
| Peaking | 327 Hz   | 1.89 | -0.9 dB |
| Peaking | 467 Hz   | 2.4  | 1.7 dB  |
| Peaking | 924 Hz   | 3.98 | -0.4 dB |
| Peaking | 926 Hz   | 4.69 | -0.8 dB |
| Peaking | 10857 Hz | 2.15 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%201%20Black%20Filter/MrSpeakers%20Ether%20C%201%20Black%20Filter.png)