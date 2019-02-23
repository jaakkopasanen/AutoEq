# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.1; 66 -2.3; 72 -3.3; 79 -4.3; 87 -5.3; 96 -6.0; 106 -6.7; 116 -7.2; 128 -7.5; 141 -7.7; 155 -7.8; 170 -7.4; 187 -7.2; 206 -7.0; 227 -6.9; 249 -6.7; 274 -6.5; 302 -6.4; 332 -6.3; 365 -6.2; 402 -6.1; 442 -6.0; 486 -5.8; 535 -5.7; 588 -5.4; 647 -5.2; 712 -4.9; 783 -4.7; 861 -4.5; 947 -4.5; 1042 -4.4; 1146 -4.5; 1261 -4.7; 1387 -5.3; 1526 -6.1; 1678 -7.0; 1846 -8.3; 2031 -9.5; 2234 -9.9; 2457 -9.4; 2703 -8.4; 2973 -8.2; 3270 -7.1; 3597 -2.0; 3957 -1.9; 4353 -6.7; 4788 -12.4; 5267 -8.3; 5793 -4.3; 6373 -4.0; 7010 -5.2; 7711 -6.5; 8482 -8.5; 9330 -9.2; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -8.0; 15026 -7.0; 16529 -6.5; 18182 -7.2; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.88 | 7.2 dB  |
| Peaking | 2351 Hz | 2.95 | -3.9 dB |
| Peaking | 3917 Hz | 4.05 | 8.3 dB  |
| Peaking | 4807 Hz | 3.2  | -8.8 dB |
| Peaking | 5867 Hz | 4.05 | 5.5 dB  |
| Peaking | 61 Hz   | 3.19 | 2.3 dB  |
| Peaking | 136 Hz  | 1.25 | -2.0 dB |
| Peaking | 1014 Hz | 0.94 | 2.4 dB  |
| Peaking | 1923 Hz | 2.96 | -1.7 dB |
| Peaking | 9091 Hz | 5.38 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20KSC75/Koss%20KSC75.png)