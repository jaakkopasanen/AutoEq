# Skullcandy Crusher
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.7; 25 -3.5; 28 -4.6; 31 -5.5; 34 -6.1; 37 -6.6; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.8; 60 -8.0; 66 -7.8; 72 -7.5; 79 -7.1; 87 -6.8; 96 -7.0; 106 -7.3; 116 -7.6; 128 -7.7; 141 -7.6; 155 -7.4; 170 -7.1; 187 -6.8; 206 -6.5; 227 -6.2; 249 -6.1; 274 -6.0; 302 -6.4; 332 -6.9; 365 -7.6; 402 -8.7; 442 -10.0; 486 -11.2; 535 -12.0; 588 -12.5; 647 -12.7; 712 -12.2; 783 -10.7; 861 -10.6; 947 -11.1; 1042 -10.7; 1146 -9.7; 1261 -8.3; 1387 -7.1; 1526 -6.7; 1678 -6.6; 1846 -6.9; 2031 -7.0; 2234 -6.7; 2457 -5.7; 2703 -5.7; 2973 -5.4; 3270 -5.0; 3597 -5.5; 3957 -6.8; 4353 -5.8; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.17 | 5.9 dB  |
| Peaking | 50 Hz   | 0.75 | -1.8 dB |
| Peaking | 602 Hz  | 1.88 | -6.4 dB |
| Peaking | 999 Hz  | 3.1  | -3.5 dB |
| Peaking | 5635 Hz | 2.76 | 6.9 dB  |
| Peaking | 135 Hz  | 3.76 | -0.9 dB |
| Peaking | 266 Hz  | 3.01 | 1.3 dB  |
| Peaking | 4018 Hz | 1.65 | 2.3 dB  |
| Peaking | 4077 Hz | 4.93 | -4.4 dB |
| Peaking | 8263 Hz | 3.3  | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -5.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher/Skullcandy%20Crusher.png)