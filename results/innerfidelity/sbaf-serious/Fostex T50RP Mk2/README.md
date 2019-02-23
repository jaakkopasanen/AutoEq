# Fostex T50RP Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -2.2; 25 -3.2; 28 -4.3; 31 -5.2; 34 -5.8; 37 -6.3; 41 -6.7; 45 -6.9; 49 -7.1; 54 -7.2; 60 -7.3; 66 -7.4; 72 -7.6; 79 -7.7; 87 -8.0; 96 -8.1; 106 -8.4; 116 -8.6; 128 -9.3; 141 -9.8; 155 -9.9; 170 -9.6; 187 -10.1; 206 -10.2; 227 -10.1; 249 -10.0; 274 -9.9; 302 -9.8; 332 -9.6; 365 -9.4; 402 -9.4; 442 -9.4; 486 -9.6; 535 -9.6; 588 -10.2; 647 -9.5; 712 -7.3; 783 -7.9; 861 -8.8; 947 -9.8; 1042 -11.1; 1146 -11.9; 1261 -11.9; 1387 -11.5; 1526 -11.0; 1678 -11.7; 1846 -10.5; 2031 -7.4; 2234 -5.2; 2457 -3.6; 2703 -1.7; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.85 | 5.7 dB  |
| Peaking | 250 Hz  | 0.4  | -3.6 dB |
| Peaking | 1197 Hz | 2.52 | -5.2 dB |
| Peaking | 1737 Hz | 3.07 | -6.0 dB |
| Peaking | 3758 Hz | 0.85 | 7.2 dB  |
| Peaking | 619 Hz  | 5.18 | -2.4 dB |
| Peaking | 701 Hz  | 5.36 | 2.3 dB  |
| Peaking | 3952 Hz | 5.24 | -1.1 dB |
| Peaking | 6259 Hz | 2.43 | 4.4 dB  |
| Peaking | 7738 Hz | 1.5  | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%20Mk2/Fostex%20T50RP%20Mk2.png)