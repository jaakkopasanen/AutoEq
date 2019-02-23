# Klipsch Reference ONE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.4; 25 -9.6; 28 -9.9; 31 -10.0; 34 -10.2; 37 -10.3; 41 -10.5; 45 -10.7; 49 -10.8; 54 -11.0; 60 -11.3; 66 -11.5; 72 -11.8; 79 -12.0; 87 -12.2; 96 -12.3; 106 -12.2; 116 -12.3; 128 -12.7; 141 -12.8; 155 -12.9; 170 -12.4; 187 -12.2; 206 -11.9; 227 -11.8; 249 -11.1; 274 -10.1; 302 -9.4; 332 -9.0; 365 -8.3; 402 -7.1; 442 -5.8; 486 -5.2; 535 -4.2; 588 -3.0; 647 -2.4; 712 -2.5; 783 -2.8; 861 -3.8; 947 -4.7; 1042 -5.5; 1146 -5.7; 1261 -5.6; 1387 -7.0; 1526 -7.6; 1678 -8.1; 1846 -8.2; 2031 -8.2; 2234 -8.5; 2457 -8.5; 2703 -8.6; 2973 -8.1; 3270 -7.0; 3597 -5.0; 3957 -2.5; 4353 -0.7; 4788 -0.5; 5267 -1.9; 5793 -2.8; 6373 -3.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 1.44 | -3.7 dB |
| Peaking | 63 Hz   | 0.38 | -3.8 dB |
| Peaking | 178 Hz  | 0.68 | -4.1 dB |
| Peaking | 649 Hz  | 1.82 | 5.4 dB  |
| Peaking | 4829 Hz | 2.82 | 6.6 dB  |
| Peaking | 1250 Hz | 1.01 | 1.5 dB  |
| Peaking | 1596 Hz | 2.48 | -1.4 dB |
| Peaking | 3309 Hz | 0.68 | -3.8 dB |
| Peaking | 3982 Hz | 2.98 | 4.8 dB  |
| Peaking | 6412 Hz | 3.36 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)