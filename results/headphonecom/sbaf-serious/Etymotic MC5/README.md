# Etymotic MC5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.4; 31 -1.7; 34 -1.9; 37 -2.1; 41 -2.4; 45 -2.6; 49 -2.9; 54 -3.2; 60 -3.7; 66 -4.0; 72 -4.3; 79 -4.6; 87 -5.0; 96 -5.4; 106 -5.7; 116 -5.9; 128 -6.2; 141 -6.5; 155 -6.7; 170 -6.9; 187 -7.1; 206 -7.1; 227 -7.2; 249 -7.2; 274 -7.2; 302 -7.1; 332 -6.9; 365 -6.8; 402 -6.7; 442 -6.8; 486 -6.7; 535 -6.7; 588 -6.7; 647 -6.7; 712 -6.8; 783 -7.0; 861 -7.5; 947 -8.3; 1042 -9.2; 1146 -10.1; 1261 -11.2; 1387 -12.4; 1526 -13.7; 1678 -14.5; 1846 -13.8; 2031 -11.0; 2234 -10.2; 2457 -9.2; 2703 -7.7; 2973 -6.0; 3270 -4.2; 3597 -2.6; 3957 -2.7; 4353 -3.7; 4788 -3.8; 5267 -2.3; 5793 -0.7; 6373 -1.1; 7010 -4.0; 7711 -6.3; 8482 -6.5; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic MC5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.86 | 5.6 dB  |
| Peaking | 52 Hz   | 1.3  | 2.1 dB  |
| Peaking | 1660 Hz | 1.61 | -8.2 dB |
| Peaking | 3685 Hz | 2.68 | 4.7 dB  |
| Peaking | 5958 Hz | 3.44 | 6.2 dB  |
| Peaking | 84 Hz   | 2.05 | 0.5 dB  |
| Peaking | 220 Hz  | 1.12 | -0.8 dB |
| Peaking | 779 Hz  | 1.2  | 0.8 dB  |
| Peaking | 1083 Hz | 2.72 | -0.8 dB |
| Peaking | 8087 Hz | 5.03 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -7.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC5/Etymotic%20MC5.png)