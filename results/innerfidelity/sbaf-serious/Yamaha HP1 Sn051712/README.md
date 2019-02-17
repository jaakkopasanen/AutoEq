# Yamaha HP1 Sn051712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.5; 25 -1.8; 28 -2.4; 31 -2.8; 34 -3.1; 37 -3.4; 41 -3.7; 45 -4.0; 49 -4.3; 54 -4.6; 60 -4.7; 66 -4.9; 72 -5.1; 79 -5.3; 87 -5.5; 96 -6.0; 106 -6.4; 116 -6.7; 128 -7.0; 141 -7.2; 155 -7.4; 170 -7.4; 187 -7.6; 206 -7.7; 227 -7.7; 249 -7.7; 274 -7.5; 302 -7.5; 332 -7.7; 365 -7.6; 402 -7.7; 442 -7.5; 486 -7.8; 535 -7.9; 588 -7.8; 647 -7.8; 712 -7.9; 783 -7.6; 861 -7.3; 947 -6.7; 1042 -6.1; 1146 -5.1; 1261 -3.9; 1387 -3.2; 1526 -3.2; 1678 -3.0; 1846 -3.4; 2031 -4.3; 2234 -5.6; 2457 -5.5; 2703 -4.7; 2973 -3.9; 3270 -2.5; 3597 -2.1; 3957 -2.4; 4353 -2.9; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP1 Sn051712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 Sn051712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.21 | 5.2 dB  |
| Peaking | 49 Hz   | 1.81 | 1.5 dB  |
| Peaking | 1575 Hz | 2.77 | 3.8 dB  |
| Peaking | 3560 Hz | 2.7  | 3.7 dB  |
| Peaking | 5634 Hz | 2.65 | 6.2 dB  |
| Peaking | 81 Hz   | 2.27 | 1.1 dB  |
| Peaking | 364 Hz  | 0.33 | -1.5 dB |
| Peaking | 1241 Hz | 4.04 | 1.7 dB  |
| Peaking | 6563 Hz | 7.73 | 2.1 dB  |
| Peaking | 7832 Hz | 2.59 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1%20Sn051712/Yamaha%20HP1%20Sn051712.png)