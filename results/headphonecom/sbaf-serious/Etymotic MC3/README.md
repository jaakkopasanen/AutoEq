# Etymotic MC3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.3; 45 -1.6; 49 -2.0; 54 -2.4; 60 -2.9; 66 -3.3; 72 -3.7; 79 -4.1; 87 -4.4; 96 -4.9; 106 -5.2; 116 -5.5; 128 -5.8; 141 -6.1; 155 -6.3; 170 -6.5; 187 -6.6; 206 -6.7; 227 -6.9; 249 -7.0; 274 -7.0; 302 -6.9; 332 -6.7; 365 -6.5; 402 -6.4; 442 -6.5; 486 -6.5; 535 -6.5; 588 -6.3; 647 -6.4; 712 -6.5; 783 -6.7; 861 -7.2; 947 -7.9; 1042 -8.7; 1146 -9.6; 1261 -10.5; 1387 -11.5; 1526 -12.5; 1678 -12.3; 1846 -12.3; 2031 -11.7; 2234 -10.8; 2457 -9.5; 2703 -8.0; 2973 -6.5; 3270 -4.5; 3597 -2.8; 3957 -2.9; 4353 -4.2; 4788 -4.5; 5267 -3.3; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic MC3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic MC3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.48 | 6.2 dB  |
| Peaking | 200 Hz  | 1.5  | -0.8 dB |
| Peaking | 1742 Hz | 1.35 | -6.6 dB |
| Peaking | 3682 Hz | 2.88 | 4.8 dB  |
| Peaking | 6072 Hz | 3.79 | 6.1 dB  |
| Peaking | 725 Hz  | 1.75 | 1.1 dB  |
| Peaking | 1366 Hz | 1.19 | -0.7 dB |
| Peaking | 1748 Hz | 6.42 | 1.1 dB  |
| Peaking | 6782 Hz | 9.39 | 1.3 dB  |
| Peaking | 7788 Hz | 3.2  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20MC3/Etymotic%20MC3.png)