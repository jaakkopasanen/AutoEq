# Skullcandy Jib
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.9; 25 -11.1; 28 -11.3; 31 -11.5; 34 -11.6; 37 -11.6; 41 -11.7; 45 -11.8; 49 -11.8; 54 -11.8; 60 -11.8; 66 -11.8; 72 -11.9; 79 -11.9; 87 -11.9; 96 -11.9; 106 -11.8; 116 -11.7; 128 -11.6; 141 -11.3; 155 -11.0; 170 -10.7; 187 -10.2; 206 -9.8; 227 -9.2; 249 -8.7; 274 -8.1; 302 -7.5; 332 -7.0; 365 -6.5; 402 -5.9; 442 -5.3; 486 -4.7; 535 -3.9; 588 -3.1; 647 -2.3; 712 -1.4; 783 -0.7; 861 -0.5; 947 -1.0; 1042 -1.8; 1146 -2.7; 1261 -3.1; 1387 -3.3; 1526 -3.4; 1678 -3.6; 1846 -3.9; 2031 -4.2; 2234 -4.2; 2457 -4.0; 2703 -4.4; 2973 -4.6; 3270 -4.1; 3597 -3.4; 3957 -3.0; 4353 -2.8; 4788 -3.2; 5267 -3.7; 5793 -3.8; 6373 -4.3; 7010 -3.5; 7711 -4.8; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.9; 18182 -9.4; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Jib GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Jib ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  0.44 | -5.2 dB |
| Peaking | 127 Hz   |  0.49 | -5.5 dB |
| Peaking | 817 Hz   |  1.19 | 5.0 dB  |
| Peaking | 4456 Hz  |  1.53 | 2.0 dB  |
| Peaking | 18269 Hz |  2.04 | -4.9 dB |
| Peaking | 2949 Hz  |  7.64 | -0.5 dB |
| Peaking | 7077 Hz  | 10.45 | 0.9 dB  |
| Peaking | 17233 Hz |  4    | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Jib/Skullcandy%20Jib.png)