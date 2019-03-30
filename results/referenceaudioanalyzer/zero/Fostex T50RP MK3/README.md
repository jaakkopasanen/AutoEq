# Fostex T50RP MK3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.5; 41 -2.6; 45 -3.5; 49 -4.3; 54 -5.1; 60 -6.0; 66 -6.6; 72 -7.1; 79 -7.5; 87 -7.8; 96 -7.8; 106 -7.8; 116 -7.8; 128 -7.5; 141 -7.1; 155 -6.7; 170 -6.3; 187 -5.9; 206 -5.5; 227 -5.1; 249 -4.8; 274 -5.0; 302 -5.2; 332 -4.8; 365 -4.3; 402 -4.2; 442 -4.2; 486 -4.4; 535 -4.9; 588 -5.4; 647 -5.8; 712 -6.3; 783 -6.8; 861 -7.3; 947 -7.7; 1042 -7.8; 1146 -7.6; 1261 -7.1; 1387 -6.2; 1526 -5.0; 1678 -4.0; 1846 -3.2; 2031 -3.0; 2234 -3.6; 2457 -4.4; 2703 -5.6; 2973 -6.6; 3270 -7.7; 3597 -8.8; 3957 -9.9; 4353 -10.9; 4788 -10.9; 5267 -10.1; 5793 -9.7; 6373 -9.8; 7010 -9.4; 7711 -8.0; 8482 -6.5; 9330 -6.5; 10263 -7.1; 11289 -7.8; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP MK3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP MK3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 1.49 | 7.0 dB  |
| Peaking | 249 Hz  | 3.9  | 1.4 dB  |
| Peaking | 421 Hz  | 2.4  | 2.5 dB  |
| Peaking | 2096 Hz | 2.35 | 4.5 dB  |
| Peaking | 4806 Hz | 1.25 | -4.6 dB |
| Peaking | 28 Hz   | 0.17 | 0.7 dB  |
| Peaking | 95 Hz   | 1.12 | -2.7 dB |
| Peaking | 684 Hz  | 0.05 | 0.3 dB  |
| Peaking | 1029 Hz | 2.43 | -2.1 dB |
| Peaking | 6859 Hz | 7.21 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T50RP%20MK3/Fostex%20T50RP%20MK3.png)