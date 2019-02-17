# Etymotic MC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -1.4; 72 -1.7; 79 -2.2; 87 -2.5; 96 -3.0; 106 -3.3; 116 -3.5; 128 -3.8; 141 -4.1; 155 -4.3; 170 -4.5; 187 -4.7; 206 -4.7; 227 -5.0; 249 -5.0; 274 -5.0; 302 -4.9; 332 -4.8; 365 -4.6; 402 -4.5; 442 -4.6; 486 -4.5; 535 -4.6; 588 -4.4; 647 -4.4; 712 -4.5; 783 -4.8; 861 -5.3; 947 -6.0; 1042 -6.8; 1146 -7.6; 1261 -8.5; 1387 -9.5; 1526 -10.5; 1678 -10.4; 1846 -10.3; 2031 -9.7; 2234 -8.8; 2457 -7.6; 2703 -6.1; 2973 -4.5; 3270 -2.6; 3597 -0.9; 3957 -1.0; 4353 -2.3; 4788 -2.6; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic MC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.35 | 6.3 dB  |
| Peaking | 769 Hz  | 0.6  | 3.2 dB  |
| Peaking | 1657 Hz | 0.98 | -6.2 dB |
| Peaking | 3657 Hz | 2.03 | 6.5 dB  |
| Peaking | 5887 Hz | 3.38 | 5.8 dB  |
| Peaking | 6659 Hz | 9.12 | 1.7 dB  |
| Peaking | 7826 Hz | 2.57 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC3/Etymotic%20MC3.png)