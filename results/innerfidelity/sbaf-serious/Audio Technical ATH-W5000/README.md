# Audio Technical ATH-W5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.1; 60 -2.0; 66 -2.7; 72 -3.3; 79 -3.5; 87 -3.9; 96 -4.3; 106 -4.8; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.6; 170 -5.4; 187 -5.6; 206 -5.7; 227 -5.5; 249 -5.7; 274 -5.7; 302 -5.7; 332 -5.3; 365 -4.9; 402 -4.7; 442 -4.4; 486 -4.2; 535 -4.0; 588 -3.9; 647 -4.3; 712 -5.3; 783 -5.2; 861 -5.6; 947 -6.2; 1042 -6.7; 1146 -7.2; 1261 -7.9; 1387 -8.4; 1526 -8.8; 1678 -9.1; 1846 -9.6; 2031 -10.2; 2234 -8.9; 2457 -6.4; 2703 -3.7; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -4.4; 4353 -2.4; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technical ATH-W5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.54 | 6.5 dB  |
| Peaking | 555 Hz  | 1.2  | 2.7 dB  |
| Peaking | 2083 Hz | 1.22 | -5.5 dB |
| Peaking | 3069 Hz | 2.26 | 8.7 dB  |
| Peaking | 5614 Hz | 2.61 | 6.4 dB  |
| Peaking | 46 Hz   | 1.05 | -0.8 dB |
| Peaking | 51 Hz   | 2.8  | 1.4 dB  |
| Peaking | 6614 Hz | 7.37 | 2.2 dB  |
| Peaking | 7715 Hz | 2.24 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-W5000/Audio%20Technical%20ATH-W5000.png)