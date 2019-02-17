# RockIt Sounds R30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -0.9; 41 -1.3; 45 -1.6; 49 -1.9; 54 -2.2; 60 -2.7; 66 -3.1; 72 -3.5; 79 -3.9; 87 -4.5; 96 -5.0; 106 -5.3; 116 -5.5; 128 -6.0; 141 -6.3; 155 -6.5; 170 -6.7; 187 -6.9; 206 -7.0; 227 -7.0; 249 -7.1; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.9; 402 -6.7; 442 -6.5; 486 -6.5; 535 -6.3; 588 -5.9; 647 -5.8; 712 -5.9; 783 -5.7; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -6.9; 1261 -7.3; 1387 -7.9; 1526 -8.3; 1678 -8.5; 1846 -8.1; 2031 -7.4; 2234 -6.4; 2457 -4.5; 2703 -2.6; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RockIt Sounds R30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RockIt Sounds R30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.35 | 6.2 dB  |
| Peaking | 182 Hz  | 0.54 | -1.3 dB |
| Peaking | 713 Hz  | 1.46 | 1.0 dB  |
| Peaking | 1771 Hz | 1.53 | -4.2 dB |
| Peaking | 3874 Hz | 0.91 | 7.4 dB  |
| Peaking | 2970 Hz | 6.46 | 1.7 dB  |
| Peaking | 3992 Hz | 3.41 | -0.8 dB |
| Peaking | 6333 Hz | 2.2  | 4.9 dB  |
| Peaking | 7206 Hz | 0.65 | -1.4 dB |
| Peaking | 7498 Hz | 2.65 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RockIt%20Sounds%20R30/RockIt%20Sounds%20R30.png)