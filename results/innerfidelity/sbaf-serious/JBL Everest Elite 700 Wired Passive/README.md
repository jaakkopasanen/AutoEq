# JBL Everest Elite 700 Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.7; 25 -2.7; 28 -2.7; 31 -2.6; 34 -2.5; 37 -2.4; 41 -2.3; 45 -2.2; 49 -2.0; 54 -1.8; 60 -1.8; 66 -1.6; 72 -1.2; 79 -0.9; 87 -1.1; 96 -2.0; 106 -2.3; 116 -2.4; 128 -2.5; 141 -2.7; 155 -2.6; 170 -3.0; 187 -3.7; 206 -4.2; 227 -4.4; 249 -4.7; 274 -4.8; 302 -4.7; 332 -4.6; 365 -4.1; 402 -4.8; 442 -6.5; 486 -6.7; 535 -6.6; 588 -6.1; 647 -6.2; 712 -6.4; 783 -6.2; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.6; 1261 -7.2; 1387 -6.9; 1526 -7.1; 1678 -7.4; 1846 -7.6; 2031 -7.3; 2234 -6.8; 2457 -5.8; 2703 -4.6; 2973 -3.6; 3270 -1.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.61 | 3.1 dB  |
| Peaking | 75 Hz   | 0.79 | 3.9 dB  |
| Peaking | 175 Hz  | 0.66 | 1.8 dB  |
| Peaking | 1923 Hz | 1.49 | -2.4 dB |
| Peaking | 4368 Hz | 1.15 | 7.1 dB  |
| Peaking | 383 Hz  | 4.89 | 2.7 dB  |
| Peaking | 433 Hz  | 2.82 | -1.7 dB |
| Peaking | 4559 Hz | 6.18 | -1.2 dB |
| Peaking | 6396 Hz | 2.7  | 4.1 dB  |
| Peaking | 7517 Hz | 1.84 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 3.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20Everest%20Elite%20700%20Wired%20Passive/JBL%20Everest%20Elite%20700%20Wired%20Passive.png)