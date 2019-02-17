# Fostex T50RP 2011 B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.2; 106 -2.3; 116 -3.1; 128 -4.0; 141 -4.8; 155 -5.3; 170 -5.6; 187 -6.2; 206 -6.5; 227 -6.6; 249 -6.6; 274 -6.6; 302 -6.6; 332 -6.3; 365 -5.7; 402 -6.0; 442 -6.1; 486 -6.3; 535 -6.1; 588 -5.9; 647 -5.7; 712 -6.5; 783 -6.1; 861 -6.9; 947 -6.9; 1042 -6.2; 1146 -6.4; 1261 -6.7; 1387 -7.0; 1526 -7.7; 1678 -7.2; 1846 -6.4; 2031 -5.2; 2234 -3.5; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP 2011 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP 2011 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.25 | 6.8 dB  |
| Peaking | 192 Hz  | 0.87 | -3.9 dB |
| Peaking | 1521 Hz | 1.94 | -2.8 dB |
| Peaking | 1858 Hz | 4.76 | -1.3 dB |
| Peaking | 3627 Hz | 0.78 | 7.0 dB  |
| Peaking | 16 Hz   | 1.82 | 1.0 dB  |
| Peaking | 2615 Hz | 5.53 | 1.6 dB  |
| Peaking | 3624 Hz | 1.75 | -1.0 dB |
| Peaking | 6252 Hz | 2.21 | 5.4 dB  |
| Peaking | 7404 Hz | 1.47 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%202011%20B/Fostex%20T50RP%202011%20B.png)