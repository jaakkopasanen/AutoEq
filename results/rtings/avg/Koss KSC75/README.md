# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -2.1; 72 -3.2; 79 -4.2; 87 -5.1; 96 -5.8; 106 -6.4; 116 -6.9; 128 -7.3; 141 -7.5; 155 -7.6; 170 -7.3; 187 -7.1; 206 -7.0; 227 -6.8; 249 -6.7; 274 -6.5; 302 -6.4; 332 -6.3; 365 -6.1; 402 -6.0; 442 -5.9; 486 -5.8; 535 -5.7; 588 -5.5; 647 -5.2; 712 -5.0; 783 -4.7; 861 -4.5; 947 -4.4; 1042 -4.5; 1146 -4.6; 1261 -5.0; 1387 -5.6; 1526 -6.4; 1678 -7.2; 1846 -8.6; 2031 -10.0; 2234 -10.7; 2457 -10.3; 2703 -8.9; 2973 -8.5; 3270 -6.4; 3597 -1.8; 3957 -1.7; 4353 -6.4; 4788 -12.6; 5267 -8.8; 5793 -4.1; 6373 -3.2; 7010 -5.2; 7711 -7.3; 8482 -8.2; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.2; 15026 -6.6; 16529 -6.5; 18182 -7.0; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.84 | 7.1 dB  |
| Peaking | 2356 Hz | 2.91 | -4.9 dB |
| Peaking | 3860 Hz | 4.41 | 7.3 dB  |
| Peaking | 4822 Hz | 5.34 | -8.2 dB |
| Peaking | 6076 Hz | 5.35 | 4.7 dB  |
| Peaking | 61 Hz   | 3.2  | 2.2 dB  |
| Peaking | 138 Hz  | 1.22 | -1.8 dB |
| Peaking | 982 Hz  | 0.97 | 2.3 dB  |
| Peaking | 1907 Hz | 3.02 | -1.6 dB |
| Peaking | 8475 Hz | 5.2  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20KSC75/Koss%20KSC75.png)