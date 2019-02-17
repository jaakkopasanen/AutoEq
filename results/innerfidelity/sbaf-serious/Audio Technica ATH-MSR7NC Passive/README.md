# Audio Technica ATH-MSR7NC Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.1; 31 -2.5; 34 -2.9; 37 -3.3; 41 -3.6; 45 -3.8; 49 -4.0; 54 -4.2; 60 -4.5; 66 -4.7; 72 -4.8; 79 -5.0; 87 -5.2; 96 -5.3; 106 -5.6; 116 -5.6; 128 -6.0; 141 -6.6; 155 -6.9; 170 -6.0; 187 -6.6; 206 -6.7; 227 -6.6; 249 -6.3; 274 -5.6; 302 -4.7; 332 -3.6; 365 -2.5; 402 -1.5; 442 -1.0; 486 -1.3; 535 -1.7; 588 -2.2; 647 -3.0; 712 -4.0; 783 -4.7; 861 -5.5; 947 -6.2; 1042 -6.8; 1146 -7.1; 1261 -7.4; 1387 -8.5; 1526 -9.6; 1678 -10.3; 1846 -10.4; 2031 -10.2; 2234 -9.0; 2457 -7.1; 2703 -5.2; 2973 -3.7; 3270 -2.9; 3597 -2.3; 3957 -3.0; 4353 -6.8; 4788 -7.2; 5267 -4.5; 5793 -0.8; 6373 -1.2; 7010 -4.1; 7711 -6.4; 8482 -7.1; 9330 -8.0; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7NC Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7NC Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.34 | 6.9 dB  |
| Peaking | 484 Hz  | 1.45 | 6.0 dB  |
| Peaking | 1820 Hz | 1.74 | -4.6 dB |
| Peaking | 3322 Hz | 2.82 | 5.1 dB  |
| Peaking | 6097 Hz | 5.07 | 6.6 dB  |
| Peaking | 224 Hz  | 2    | -1.1 dB |
| Peaking | 363 Hz  | 4.37 | 1.0 dB  |
| Peaking | 4612 Hz | 5.18 | -5.5 dB |
| Peaking | 4622 Hz | 2.19 | 2.8 dB  |
| Peaking | 9082 Hz | 4.79 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 6.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7NC%20Passive/Audio%20Technica%20ATH-MSR7NC%20Passive.png)