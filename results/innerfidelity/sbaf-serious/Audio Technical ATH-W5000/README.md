# Audio Technical ATH-W5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.9; 49 -2.9; 54 -3.8; 60 -4.7; 66 -5.4; 72 -6.0; 79 -6.2; 87 -6.7; 96 -7.0; 106 -7.5; 116 -7.6; 128 -7.9; 141 -8.1; 155 -8.3; 170 -8.2; 187 -8.3; 206 -8.5; 227 -8.3; 249 -8.4; 274 -8.4; 302 -8.4; 332 -8.0; 365 -7.6; 402 -7.4; 442 -7.1; 486 -6.9; 535 -6.8; 588 -6.6; 647 -7.0; 712 -8.0; 783 -7.9; 861 -8.3; 947 -8.9; 1042 -9.4; 1146 -9.9; 1261 -10.6; 1387 -11.1; 1526 -11.5; 1678 -11.8; 1846 -12.3; 2031 -12.9; 2234 -11.6; 2457 -9.1; 2703 -6.4; 2973 -1.6; 3270 -0.7; 3597 -2.4; 3957 -7.1; 4353 -5.1; 4788 -4.5; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technical ATH-W5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.72 | 6.8 dB  |
| Peaking | 145 Hz  | 0.59 | -2.3 dB |
| Peaking | 2050 Hz | 0.88 | -7.2 dB |
| Peaking | 3129 Hz | 3.25 | 10.7 dB |
| Peaking | 5853 Hz | 3.1  | 7.3 dB  |
| Peaking | 292 Hz  | 3.98 | -0.7 dB |
| Peaking | 564 Hz  | 3.72 | 1.1 dB  |
| Peaking | 4021 Hz | 3    | 2.1 dB  |
| Peaking | 4053 Hz | 8.68 | -4.9 dB |
| Peaking | 8033 Hz | 5.43 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-W5000/Audio%20Technical%20ATH-W5000.png)