# Audio Technical ATH-ES55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.0; 96 -1.3; 106 -2.0; 116 -3.0; 128 -3.8; 141 -4.6; 155 -5.0; 170 -5.3; 187 -5.9; 206 -6.2; 227 -6.4; 249 -6.6; 274 -6.2; 302 -5.9; 332 -6.0; 365 -6.6; 402 -6.6; 442 -6.2; 486 -6.4; 535 -6.4; 588 -6.3; 647 -6.9; 712 -7.9; 783 -8.4; 861 -9.2; 947 -9.6; 1042 -10.0; 1146 -10.2; 1261 -10.6; 1387 -11.3; 1526 -11.8; 1678 -12.0; 1846 -11.8; 2031 -10.8; 2234 -9.5; 2457 -7.6; 2703 -6.1; 2973 -4.8; 3270 -4.7; 3597 -4.5; 3957 -3.8; 4353 -3.6; 4788 -2.2; 5267 -1.6; 5793 -1.1; 6373 -1.0; 7010 -4.6; 7711 -7.9; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -9.6; 16529 -9.9; 18182 -10.5; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technical ATH-ES55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.49 | 6.0 dB  |
| Peaking | 81 Hz    | 1.29 | 3.8 dB  |
| Peaking | 1536 Hz  | 1.2  | -6.0 dB |
| Peaking | 5095 Hz  | 1.32 | 5.6 dB  |
| Peaking | 20116 Hz | 0.34 | -5.6 dB |
| Peaking | 2045 Hz  | 4.23 | -1.2 dB |
| Peaking | 2914 Hz  | 3.04 | 1.7 dB  |
| Peaking | 4479 Hz  | 5.64 | -1.6 dB |
| Peaking | 6432 Hz  | 4.43 | 3.2 dB  |
| Peaking | 7646 Hz  | 4.17 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-ES55/Audio%20Technical%20ATH-ES55.png)