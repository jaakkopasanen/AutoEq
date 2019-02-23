# RockIt Sounds R30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.6; 25 -2.9; 28 -3.4; 31 -3.7; 34 -4.0; 37 -4.3; 41 -4.6; 45 -4.9; 49 -5.2; 54 -5.6; 60 -6.0; 66 -6.4; 72 -6.9; 79 -7.3; 87 -7.9; 96 -8.3; 106 -8.6; 116 -8.9; 128 -9.3; 141 -9.6; 155 -9.9; 170 -10.1; 187 -10.2; 206 -10.4; 227 -10.4; 249 -10.5; 274 -10.5; 302 -10.3; 332 -10.3; 365 -10.2; 402 -10.1; 442 -9.8; 486 -9.8; 535 -9.7; 588 -9.3; 647 -9.2; 712 -9.3; 783 -9.1; 861 -9.3; 947 -9.6; 1042 -10.0; 1146 -10.3; 1261 -10.7; 1387 -11.3; 1526 -11.7; 1678 -11.9; 1846 -11.4; 2031 -10.7; 2234 -9.8; 2457 -7.9; 2703 -6.0; 2973 -3.5; 3270 -1.3; 3597 -0.5; 3957 -0.9; 4353 -2.7; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RockIt Sounds R30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RockIt Sounds R30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.29 | 4.6 dB  |
| Peaking | 226 Hz  | 0.41 | -4.1 dB |
| Peaking | 1785 Hz | 0.96 | -5.8 dB |
| Peaking | 3454 Hz | 1.97 | 7.6 dB  |
| Peaking | 5690 Hz | 2.75 | 6.0 dB  |
| Peaking | 6620 Hz | 7.72 | 2.1 dB  |
| Peaking | 7729 Hz | 2.33 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RockIt%20Sounds%20R30/RockIt%20Sounds%20R30.png)