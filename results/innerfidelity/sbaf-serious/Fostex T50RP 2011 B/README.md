# Fostex T50RP 2011 B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.4; 87 -2.9; 96 -4.3; 106 -5.4; 116 -6.2; 128 -7.1; 141 -7.9; 155 -8.4; 170 -8.7; 187 -9.2; 206 -9.5; 227 -9.6; 249 -9.7; 274 -9.7; 302 -9.7; 332 -9.4; 365 -8.7; 402 -9.1; 442 -9.2; 486 -9.4; 535 -9.1; 588 -9.0; 647 -8.8; 712 -9.5; 783 -9.2; 861 -10.0; 947 -9.9; 1042 -9.3; 1146 -9.4; 1261 -9.8; 1387 -10.1; 1526 -10.8; 1678 -10.3; 1846 -9.5; 2031 -8.2; 2234 -6.5; 2457 -4.4; 2703 -3.1; 2973 -2.1; 3270 -1.9; 3597 -2.3; 3957 -2.1; 4353 -1.9; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -8.5; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP 2011 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP 2011 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.32 | 8.4 dB  |
| Peaking | 168 Hz   | 0.58 | -7.2 dB |
| Peaking | 2836 Hz  | 0.37 | -8.0 dB |
| Peaking | 3047 Hz  | 1.22 | 11.0 dB |
| Peaking | 5543 Hz  | 1.59 | 9.4 dB  |
| Peaking | 18 Hz    | 0.43 | 1.3 dB  |
| Peaking | 37 Hz    | 1.56 | -1.7 dB |
| Peaking | 1099 Hz  | 7.77 | 0.8 dB  |
| Peaking | 9285 Hz  | 4.06 | -2.5 dB |
| Peaking | 10895 Hz | 1.24 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 6.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%202011%20B/Fostex%20T50RP%202011%20B.png)