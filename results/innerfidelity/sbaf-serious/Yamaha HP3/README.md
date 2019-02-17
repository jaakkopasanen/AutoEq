# Yamaha HP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.1; 60 -1.8; 66 -2.4; 72 -2.9; 79 -3.5; 87 -4.0; 96 -4.7; 106 -5.2; 116 -5.4; 128 -5.9; 141 -6.4; 155 -6.7; 170 -6.9; 187 -7.1; 206 -7.2; 227 -7.2; 249 -7.1; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.8; 402 -6.7; 442 -6.5; 486 -6.7; 535 -6.6; 588 -6.4; 647 -6.3; 712 -6.4; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -5.8; 1387 -5.5; 1526 -4.8; 1678 -3.5; 1846 -1.6; 2031 -0.5; 2234 -0.5; 2457 -0.8; 2703 -2.4; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -1.3; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.57 | 6.9 dB  |
| Peaking | 989 Hz  | 0.05 | -0.8 dB |
| Peaking | 2079 Hz | 2    | 5.7 dB  |
| Peaking | 3567 Hz | 1.7  | 5.0 dB  |
| Peaking | 5679 Hz | 2.38 | 5.8 dB  |
| Peaking | 21 Hz   | 0.37 | 1.9 dB  |
| Peaking | 32 Hz   | 1.47 | -2.4 dB |
| Peaking | 174 Hz  | 1.07 | -0.8 dB |
| Peaking | 564 Hz  | 1.3  | 0.6 dB  |
| Peaking | 7942 Hz | 6.78 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP3/Yamaha%20HP3.png)