# Ceaden Linea No 10 Passive Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.7; 25 -10.0; 28 -10.4; 31 -10.7; 34 -10.9; 37 -11.1; 41 -11.2; 45 -11.3; 49 -11.4; 54 -11.7; 60 -12.0; 66 -12.2; 72 -12.3; 79 -12.4; 87 -12.6; 96 -12.7; 106 -12.6; 116 -12.6; 128 -12.6; 141 -12.6; 155 -12.3; 170 -11.7; 187 -11.3; 206 -10.6; 227 -9.6; 249 -9.3; 274 -9.3; 302 -9.0; 332 -8.6; 365 -8.1; 402 -7.7; 442 -7.3; 486 -7.1; 535 -6.8; 588 -6.5; 647 -6.7; 712 -7.0; 783 -7.1; 861 -7.5; 947 -7.7; 1042 -8.0; 1146 -8.2; 1261 -8.3; 1387 -8.6; 1526 -8.8; 1678 -8.5; 1846 -7.7; 2031 -6.5; 2234 -5.0; 2457 -3.2; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.4; 4788 -4.9; 5267 -2.7; 5793 -0.7; 6373 -3.2; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ceaden Linea No 10 Passive Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ceaden Linea No 10 Passive Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.56 | -3.0 dB |
| Peaking | 119 Hz  | 0.56 | -5.5 dB |
| Peaking | 3318 Hz | 2.3  | 7.0 dB  |
| Peaking | 5830 Hz | 4.8  | 5.1 dB  |
| Peaking | 576 Hz  | 2.01 | 1.0 dB  |
| Peaking | 1522 Hz | 1.12 | -2.7 dB |
| Peaking | 2578 Hz | 4.23 | 2.7 dB  |
| Peaking | 4100 Hz | 1.49 | 0.3 dB  |
| Peaking | 8713 Hz | 3.09 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ceaden%20Linea%20No%2010%20Passive%20Wired/Ceaden%20Linea%20No%2010%20Passive%20Wired.png)