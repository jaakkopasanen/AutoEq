# Fostex T50RP 2011 A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.3; 87 -2.6; 96 -3.9; 106 -5.0; 116 -5.8; 128 -6.6; 141 -7.3; 155 -7.8; 170 -8.1; 187 -8.6; 206 -9.0; 227 -9.2; 249 -9.3; 274 -9.1; 302 -8.9; 332 -8.6; 365 -8.7; 402 -8.8; 442 -8.9; 486 -9.3; 535 -9.1; 588 -8.6; 647 -9.2; 712 -9.4; 783 -9.2; 861 -9.8; 947 -10.6; 1042 -10.3; 1146 -10.1; 1261 -10.1; 1387 -10.4; 1526 -11.2; 1678 -11.4; 1846 -10.2; 2031 -8.6; 2234 -7.0; 2457 -5.2; 2703 -3.2; 2973 -1.8; 3270 -1.5; 3597 -1.9; 3957 -2.3; 4353 -3.2; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP 2011 A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP 2011 A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 0.31 | 8.0 dB  |
| Peaking | 171 Hz  | 0.6  | -6.4 dB |
| Peaking | 2168 Hz | 0.48 | -8.2 dB |
| Peaking | 3076 Hz | 1.2  | 11.9 dB |
| Peaking | 5720 Hz | 2.48 | 6.9 dB  |
| Peaking | 18 Hz   | 0.37 | 1.3 dB  |
| Peaking | 38 Hz   | 1.52 | -1.7 dB |
| Peaking | 1587 Hz | 1.87 | 1.8 dB  |
| Peaking | 1641 Hz | 3.72 | -2.7 dB |
| Peaking | 7947 Hz | 6.91 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%202011%20A/Fostex%20T50RP%202011%20A.png)