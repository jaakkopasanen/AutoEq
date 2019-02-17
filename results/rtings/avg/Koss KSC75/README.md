# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.8; 60 -3.1; 66 -4.3; 72 -5.4; 79 -6.3; 87 -7.3; 96 -8.1; 106 -8.7; 116 -9.2; 128 -9.6; 141 -9.8; 155 -9.8; 170 -9.4; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.7; 274 -8.6; 302 -8.5; 332 -8.4; 365 -8.2; 402 -8.1; 442 -8.0; 486 -7.9; 535 -7.7; 588 -7.5; 647 -7.2; 712 -6.9; 783 -6.7; 861 -6.6; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.8; 1387 -7.4; 1526 -8.2; 1678 -9.0; 1846 -10.3; 2031 -11.6; 2234 -11.9; 2457 -11.4; 2703 -10.5; 2973 -10.2; 3270 -9.1; 3597 -4.0; 3957 -3.9; 4353 -8.7; 4788 -14.4; 5267 -10.3; 5793 -6.4; 6373 -6.1; 7010 -7.2; 7711 -8.5; 8482 -10.6; 9330 -11.2; 10263 -8.9; 11289 -6.5; 12418 -7.6; 13660 -10.0; 15026 -9.1; 16529 -8.3; 18182 -9.2; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.42 | 10.2 dB |
| Peaking | 103 Hz   | 0.49 | -8.3 dB |
| Peaking | 2266 Hz  | 2.06 | -5.7 dB |
| Peaking | 8905 Hz  | 4.03 | -4.2 dB |
| Peaking | 19061 Hz | 0.26 | -3.1 dB |
| Peaking | 3141 Hz  | 6.96 | -4.4 dB |
| Peaking | 3816 Hz  | 3.17 | 6.3 dB  |
| Peaking | 4834 Hz  | 4.58 | -9.9 dB |
| Peaking | 5968 Hz  | 4.47 | 2.9 dB  |
| Peaking | 6404 Hz  | 0.1  | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20KSC75/Koss%20KSC75.png)