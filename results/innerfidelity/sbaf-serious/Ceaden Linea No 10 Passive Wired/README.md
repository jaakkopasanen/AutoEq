# Ceaden Linea No 10 Passive Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.3; 25 -8.6; 28 -9.0; 31 -9.3; 34 -9.5; 37 -9.7; 41 -9.8; 45 -9.9; 49 -10.0; 54 -10.3; 60 -10.6; 66 -10.8; 72 -10.9; 79 -11.0; 87 -11.2; 96 -11.3; 106 -11.3; 116 -11.2; 128 -11.2; 141 -11.2; 155 -10.9; 170 -10.3; 187 -9.9; 206 -9.2; 227 -8.2; 249 -7.9; 274 -7.9; 302 -7.6; 332 -7.2; 365 -6.7; 402 -6.4; 442 -5.9; 486 -5.7; 535 -5.4; 588 -5.1; 647 -5.3; 712 -5.6; 783 -5.7; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -7.2; 1526 -7.4; 1678 -7.2; 1846 -6.3; 2031 -5.1; 2234 -3.6; 2457 -1.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -3.5; 5267 -1.3; 5793 -0.5; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ceaden Linea No 10 Passive Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ceaden Linea No 10 Passive Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.46 | -3.9 dB |
| Peaking | 141 Hz  | 1.23 | -2.3 dB |
| Peaking | 558 Hz  | 2.24 | 1.7 dB  |
| Peaking | 3249 Hz | 1.72 | 6.7 dB  |
| Peaking | 5839 Hz | 3.7  | 5.3 dB  |
| Peaking | 1683 Hz | 1.26 | -4.6 dB |
| Peaking | 2698 Hz | 0.64 | 4.5 dB  |
| Peaking | 3255 Hz | 3.99 | -3.4 dB |
| Peaking | 6133 Hz | 0.93 | -2.6 dB |
| Peaking | 6609 Hz | 5.08 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ceaden%20Linea%20No%2010%20Passive%20Wired/Ceaden%20Linea%20No%2010%20Passive%20Wired.png)