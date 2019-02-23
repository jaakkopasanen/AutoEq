# Cypher Labs Astru IEM Bass Boo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.2; 25 -3.2; 28 -3.2; 31 -3.2; 34 -3.3; 37 -3.4; 41 -3.6; 45 -3.8; 49 -4.0; 54 -4.3; 60 -4.6; 66 -4.9; 72 -5.4; 79 -5.8; 87 -6.2; 96 -6.7; 106 -7.0; 116 -7.1; 128 -7.5; 141 -7.7; 155 -7.9; 170 -8.0; 187 -8.0; 206 -8.0; 227 -7.8; 249 -7.8; 274 -7.6; 302 -7.3; 332 -7.0; 365 -6.7; 402 -6.3; 442 -5.8; 486 -5.5; 535 -5.1; 588 -4.3; 647 -3.9; 712 -3.7; 783 -3.2; 861 -3.3; 947 -3.5; 1042 -3.8; 1146 -4.1; 1261 -4.6; 1387 -5.3; 1526 -6.2; 1678 -7.2; 1846 -8.1; 2031 -8.7; 2234 -8.3; 2457 -6.5; 2703 -5.6; 2973 -4.1; 3270 -2.3; 3597 -2.7; 3957 -5.2; 4353 -7.3; 4788 -4.8; 5267 -3.8; 5793 -3.4; 6373 -0.5; 7010 -2.9; 7711 -5.1; 8482 -5.3; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cypher Labs Astru IEM Bass Boo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cypher Labs Astru IEM Bass Boo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 29 Hz   |  0.76 | 2.4 dB  |
| Peaking | 171 Hz  |  0.95 | -3.1 dB |
| Peaking | 2057 Hz |  3.8  | -3.9 dB |
| Peaking | 3345 Hz |  5.93 | 3.8 dB  |
| Peaking | 6392 Hz |  5.76 | 5.3 dB  |
| Peaking | 94 Hz   |  5.14 | -0.5 dB |
| Peaking | 345 Hz  |  1.71 | -1.1 dB |
| Peaking | 844 Hz  |  1.06 | 2.4 dB  |
| Peaking | 1650 Hz |  3.61 | -1.5 dB |
| Peaking | 4306 Hz | 11.27 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cypher%20Labs%20Astru%20IEM%20Bass%20Boo/Cypher%20Labs%20Astru%20IEM%20Bass%20Boo.png)