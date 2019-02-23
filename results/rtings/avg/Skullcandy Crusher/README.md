# Skullcandy Crusher
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.9; 25 -3.7; 28 -4.8; 31 -5.7; 34 -6.3; 37 -6.7; 41 -7.1; 45 -7.3; 49 -7.5; 54 -7.9; 60 -8.1; 66 -7.8; 72 -7.5; 79 -7.2; 87 -7.1; 96 -7.2; 106 -7.5; 116 -7.8; 128 -7.9; 141 -7.8; 155 -7.6; 170 -7.3; 187 -7.0; 206 -6.7; 227 -6.3; 249 -6.2; 274 -6.1; 302 -6.5; 332 -6.9; 365 -7.6; 402 -8.7; 442 -10.0; 486 -11.1; 535 -11.9; 588 -12.4; 647 -12.6; 712 -12.1; 783 -10.6; 861 -10.5; 947 -11.0; 1042 -10.6; 1146 -9.6; 1261 -8.2; 1387 -6.8; 1526 -6.4; 1678 -6.4; 1846 -6.7; 2031 -6.5; 2234 -5.8; 2457 -4.8; 2703 -5.1; 2973 -5.3; 3270 -5.3; 3597 -5.7; 3957 -7.1; 4353 -6.2; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 3.02 | 4.4 dB  |
| Peaking | 291 Hz  | 3.29 | 1.4 dB  |
| Peaking | 598 Hz  | 1.49 | -6.2 dB |
| Peaking | 1005 Hz | 3.95 | -2.9 dB |
| Peaking | 5640 Hz | 2.77 | 6.9 dB  |
| Peaking | 57 Hz   | 1.99 | -1.6 dB |
| Peaking | 129 Hz  | 2.72 | -1.3 dB |
| Peaking | 3648 Hz | 0.86 | 1.6 dB  |
| Peaking | 4094 Hz | 5.75 | -4.1 dB |
| Peaking | 8259 Hz | 2.73 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | -4.9 dB |
| Peaking | 1000 Hz  | 1.41 | -3.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher/Skullcandy%20Crusher.png)