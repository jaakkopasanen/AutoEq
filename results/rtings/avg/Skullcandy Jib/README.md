# Skullcandy Jib
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.4; 28 -6.6; 31 -6.7; 34 -6.8; 37 -6.9; 41 -7.0; 45 -7.0; 49 -7.0; 54 -7.1; 60 -7.4; 66 -7.7; 72 -7.9; 79 -8.2; 87 -8.5; 96 -8.8; 106 -9.3; 116 -9.6; 128 -10.0; 141 -10.2; 155 -10.3; 170 -10.2; 187 -10.1; 206 -9.8; 227 -9.3; 249 -8.7; 274 -8.2; 302 -7.6; 332 -7.1; 365 -6.6; 402 -6.0; 442 -5.4; 486 -4.8; 535 -4.1; 588 -3.2; 647 -2.4; 712 -1.5; 783 -0.7; 861 -0.5; 947 -0.9; 1042 -1.8; 1146 -2.6; 1261 -3.1; 1387 -3.3; 1526 -3.3; 1678 -3.5; 1846 -3.7; 2031 -3.9; 2234 -3.5; 2457 -3.2; 2703 -3.9; 2973 -4.7; 3270 -4.4; 3597 -3.8; 3957 -3.5; 4353 -3.2; 4788 -3.0; 5267 -3.5; 5793 -3.8; 6373 -5.4; 7010 -3.6; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -5.9; 18182 -9.5; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Jib GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Jib ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.82 | -1.2 dB |
| Peaking | 162 Hz   | 0.58 | -5.4 dB |
| Peaking | 829 Hz   | 1.13 | 4.8 dB  |
| Peaking | 4546 Hz  | 1.71 | 1.7 dB  |
| Peaking | 18406 Hz | 1.97 | -5.1 dB |
| Peaking | 1180 Hz  | 6.36 | -0.5 dB |
| Peaking | 2412 Hz  | 3.76 | 1.1 dB  |
| Peaking | 3039 Hz  | 5.77 | -0.9 dB |
| Peaking | 22047 Hz | 1.54 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Jib/Skullcandy%20Jib.png)