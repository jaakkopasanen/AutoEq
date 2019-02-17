# Etymotic EK5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.8; 60 -1.2; 66 -1.6; 72 -2.0; 79 -2.4; 87 -2.9; 96 -3.3; 106 -3.5; 116 -3.7; 128 -4.1; 141 -4.4; 155 -4.7; 170 -4.8; 187 -4.8; 206 -5.0; 227 -5.0; 249 -5.0; 274 -5.1; 302 -4.9; 332 -4.9; 365 -4.8; 402 -4.7; 442 -4.6; 486 -4.8; 535 -4.7; 588 -4.4; 647 -4.5; 712 -4.7; 783 -4.7; 861 -5.3; 947 -5.9; 1042 -6.9; 1146 -7.8; 1261 -8.8; 1387 -9.2; 1526 -10.2; 1678 -11.4; 1846 -12.2; 2031 -12.8; 2234 -12.5; 2457 -9.6; 2703 -9.0; 2973 -7.0; 3270 -5.5; 3597 -4.5; 3957 -4.3; 4353 -5.1; 4788 -5.3; 5267 -4.7; 5793 -3.9; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic EK5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic EK5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.37 | 6.3 dB  |
| Peaking | 679 Hz  | 0.69 | 2.7 dB  |
| Peaking | 2029 Hz | 1.06 | -7.9 dB |
| Peaking | 3488 Hz | 1.44 | 4.6 dB  |
| Peaking | 6417 Hz | 4.66 | 4.1 dB  |
| Peaking | 8033 Hz | 5.63 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20EK5/Etymotic%20EK5.png)