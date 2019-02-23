# Obravo HAMT1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.6; 34 -2.4; 37 -2.9; 41 -3.2; 45 -3.6; 49 -4.4; 54 -6.5; 60 -9.7; 66 -11.6; 72 -13.0; 79 -14.5; 87 -15.8; 96 -16.6; 106 -16.9; 116 -16.4; 128 -15.5; 141 -14.2; 155 -12.7; 170 -11.0; 187 -9.7; 206 -7.7; 227 -5.3; 249 -2.7; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.6; 402 -4.7; 442 -8.6; 486 -12.9; 535 -15.6; 588 -14.4; 647 -12.3; 712 -10.5; 783 -8.7; 861 -7.4; 947 -6.1; 1042 -4.7; 1146 -3.0; 1261 -1.4; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -1.5; 2031 -8.1; 2234 -8.9; 2457 -7.0; 2703 -6.7; 2973 -7.5; 3270 -8.4; 3597 -8.7; 3957 -8.2; 4353 -6.7; 4788 -3.7; 5267 -1.7; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.7; 9330 -13.5; 10263 -11.7; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -8.3; 16529 -9.0; 18182 -9.8; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Obravo HAMT1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Obravo HAMT1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.49 | 10.3 dB  |
| Peaking | 101 Hz  | 0.59 | -16.2 dB |
| Peaking | 320 Hz  | 1.08 | 14.1 dB  |
| Peaking | 536 Hz  | 1.91 | -13.7 dB |
| Peaking | 1418 Hz | 2.49 | 7.4 dB   |
| Peaking | 1810 Hz | 6.33 | 4.5 dB   |
| Peaking | 2111 Hz | 5.47 | -5.3 dB  |
| Peaking | 3794 Hz | 2.14 | -4.4 dB  |
| Peaking | 5870 Hz | 1.6  | 7.4 dB   |
| Peaking | 9298 Hz | 2.82 | -9.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB   |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -13.0 dB |
| Peaking | 250 Hz   | 1.41 | 10.0 dB  |
| Peaking | 500 Hz   | 1.41 | -7.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Obravo%20HAMT1/Obravo%20HAMT1.png)